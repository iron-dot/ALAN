# -*- coding: utf-8 -*-
#@title Import the necessary modules
# TensorFlow and TF-Hub modules.
from absl import logging

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow_docs.vis import embed

logging.set_verbosity(logging.ERROR)

# Some modules to help with reading the UCF101 dataset.
import random
import re
import os
import tempfile
import ssl

import numpy as np

# Some modules to display an animation using imageio.
import imageio

from gtts import gTTS

from urllib import request  # requires python3
#@title Helper functions for the UCF101 dataset

from pytube import YouTube

import json
from diffusers import TextToVideoZeroPipeline

import time
import whisper

import moviepy.editor as mp
import requests
import openai

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import urllib.request

from moviepy.editor import VideoFileClip
from openai import OpenAI # OpenAI official Python package
from playsound import playsound
from listToString import listToString
import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
'''import input_real
input_real.input_real()'''

# Utilities to fetch videos from UCF101 dataset
UCF_ROOT = "https://www.crcv.ucf.edu/THUMOS14/UCF101/UCF101/"
_VIDEO_LIST = None
_CACHE_DIR = tempfile.mkdtemp()
# As of July 2020, crcv.ucf.edu doesn't use a certificate accepted by the
# default Colab environment anymore.
unverified_context = ssl._create_unverified_context()

f = open('mp4.txt','r',encoding='utf-8')
mp4_file = listToString(f.readlines())

print(mp4_file)

if  mp4_file == "True":#mp4_file이 있다는건 카메라 함수에서 영상을 녹화해서 저장했다는거고 그게 여기로 온다고 가정했을때 영상이 있으면 아크원을 작동시켜 행동인식해서 할 작업을 선택하고 영상이 없으면 자유롭게 활동하며 알아서 계속 자율적으로 유니티나 아님 인터넷ㅇ[서 자유롭게 놀고 활동하며 학습하게 한다 또한 영상파일을어떻게 저장해서 어떻게 여기로가져오고 뭐 어쩔지에대한거 제발 이거는 해결할것 나중에 충분한 gpu를 가진 컴에서 사용할때 그걸 해결하고 다른 오류나 문제들 해결할것 지금으로써 생각이 안나므로 알아서 방법생각나면 해결하고 지금부터는 그냥 기능이나 추가할것



    
    def list_ucf_videos():
        """Lists videos available in UCF101 dataset."""
        global _VIDEO_LIST
        if not _VIDEO_LIST:
            index = request.urlopen(UCF_ROOT, context=unverified_context).read().decode("utf-8")
            videos = re.findall("(v_[\w_]+\.avi)", index)
            _VIDEO_LIST = sorted(set(videos))
        return list(_VIDEO_LIST)

    def fetch_ucf_video(video):
        """Fetchs a video and cache into local filesystem."""
        import os
        cache_path = os.path.join(_CACHE_DIR, video)
        if not os.path.exists(cache_path):
            urlpath = request.urljoin(UCF_ROOT, video)
            print("Fetching %s => %s" % (urlpath, cache_path))
            data = request.urlopen(urlpath, context=unverified_context).read()
            open(cache_path, "wb").write(data)
        return cache_path

    # Utilities to open video files using CV2
    def crop_center_square(frame):
        y, x = frame.shape[0:2]
        min_dim = min(y, x)
        start_x = (x // 2) - (min_dim // 2)
        start_y = (y // 2) - (min_dim // 2)
        return frame[start_y:start_y+min_dim,start_x:start_x+min_dim]

    def load_video(path, max_frames=0, resize=(224, 224)):

        cap = cv2.VideoCapture(path)
        frames = []
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = crop_center_square(frame)
                frame = cv2.resize(frame, resize)
                frame = frame[:, :, [2, 1, 0]]
                frames.append(frame)

                if len(frames) == max_frames:
                    break
        finally:
            cap.release()
        return np.array(frames) / 255.0

    def to_gif(images):
        converted_images = np.clip(images * 255, 0, 255).astype(np.uint8)
        imageio.mimsave('./animation.gif', converted_images, fps=25)
        return embed.embed_file('./animation.gif')

    #@title Get the kinetics-400 labels
    # Get the kinetics-400 action labels from the GitHub repository.
    KINETICS_URL = "https://raw.githubusercontent.com/deepmind/kinetics-i3d/master/data/label_map_600.txt"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
    req = request.Request(KINETICS_URL, headers)
    with request.urlopen(req) as obj:
        labels = [line.decode("utf-8").strip() for line in obj.readlines()]

    print("Found %d labels." % len(labels))
    # Get the list of videos in the dataset.
    ucf_videos = list_ucf_videos()

    categories = {}
    for video in ucf_videos:
        category = video[2:-12]
        if category not in categories:
            categories[category] = []
        categories[category].append(video)
        print("Found %d videos in %d categories." % (len(ucf_videos), len(categories)))

    for category, sequences in categories.items():
        summary = ", ".join(sequences[:2])
        print("%-20s %4d videos (%s, ...)" % (category, len(sequences), summary))


    # Get a sample cricket video.


    f = open('avi.txt','r',encoding='utf-8')
    avi_file = listToString(f.readlines())
    
    
    print(avi_file)


    video_path = fetch_ucf_video(avi_file)
    sample_video = load_video(video_path)
    sample_video.shape
    i3d = hub.load("https://tfhub.dev/deepmind/i3d-kinetics-600/1").signatures['default']
    def predict(sample_video):
        # Add a batch axis to the sample video.
        model_input = tf.constant(sample_video, dtype=tf.float32)[tf.newaxis, ...]

        logits = i3d(model_input)['default'][0]
        probabilities = tf.nn.softmax(logits)

        print("Top 5 actions:")
        for i in np.argsort(probabilities)[::-1][:5]:
            print(f"  {labels[i]:22}: {probabilities[i] * 100:5.2f}%")



    a = predict(sample_video)

    print(a)









    # 여기서 동영상 파일에 음성이 있으면 계속 가고 없으면 행동만 인식하는걸로 가게 만든다
        
    clip = VideoFileClip("input.avi")
    clip.write_videofile("input.mp4")

    clip = VideoFileClip("input.mp4")
    clip.audio.write_audiofile("input.mp3")

    model = whisper.load_model("large")
    result = model.transcribe("input.mp3")
    result["text"][:300]
    result["segments"][:3]
    len(result["text"])

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
    )

    docs = [Document(page_content=x) for x in text_splitter.split_text(result["text"])]

    split_docs = text_splitter.split_documents(docs)

    len(split_docs)
    split_docs
    

    client = OpenAI(
        api_key="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")
    gpt_prompt = [{"role": "system", "content": f' 예시 : {split_docs}에 대한 상황판단: 상황: 사용자가 화이트캣(백색 고양이)를 생성하라는 요청을 했음, A(사용자, 주인님): hello generate the white cat, '}]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=gpt_prompt,

    )
    print(response.choices[0].message.content)
    input_prompt = response.choices[0].message.content
    print(input_prompt)#텍스트 대본
    f = open('situation.txt','w',encoding='utf-8')
    f.write(input_prompt)


class bigbrain:
    """
    대뇌: 감정을 처리하고 감정을 결정하는 역할
    """
    def __init__(self,a,prompt):
        self.a = a
        self.prompt = prompt
    def judge_con(input_prompt):

        from openai import OpenAI # OpenAI official Python package
        client = OpenAI(
            api_key="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")
        f = open ('dataset/judge_con.json','r',encoding = 'utf-8')
        judge_con = f.readlines()
        #input_prompt = input(':')
        gpt_prompt = [{"role": "system", "content": f'''
        `         {judge_con}을 바탕으로 {input_prompt}를 판단해줘 출력예시만 출력해야만한다 그 어떠한 추가설명없이 출력예시 밑부분만 판단하고 출력해야만한다

                    입력예시:

                    뱀을 보고 트라우마가 떠오른 상황

                    출력예시:

                    "brain": "right"


                    '''}]

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=gpt_prompt,

        )

        input_prompt = response.choices[0].message.content
        print(input_prompt)
        if 'right' in input_prompt:
            con = 'subconsciousness'
            print(con)
        if 'left' in input_prompt:
            con = 'consciousness'
            print(con)

        f = open('con.txt','w',encoding='utf-8')
        f.write(con)    

        return con


    def emotion(self):
        
        parse_task_demos_or_presteps = open('emotion.json', "r",encoding='utf-8').read()

        messages = json.loads(parse_task_demos_or_presteps)
        messages.insert(0,{"role": "system", "content": f'''{self.a}라는행동이 인식되었고  {self.prompt}라는 상황이 인식 되었다 이 두가지 들을 보고 현재 인식된감정까지 고려할때 너 자신이 인간이었다면 지금 상황에서 어떤 감정을 느꼈을지 출력해라
                            출력예시 : 
                            인식된상황: 주인님이 분노로 휩싸이셔서 해킹하라고 하시며 분노를 주체하지못하고 의자를 부숴버린상황
                            인식감정:분노,흥분
                            인식언어:해킹해 당장 저놈
                            인식행동:의자를 부숨
                            지정할 감정:불안
                            이런식으로 형식을 비슷하게 너 자신의 감정을 정한다 그리고 어떠한 설명도 금지하고 저 형식만 한번만 출력하여야만한다'''})




        # GPT-3.5 Turbo 모델에 대화 메세지를 보내 응답을 받습니다.
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=messages,

        )
        print(response.choices[0].message.content)
        input_prompt = response.choices[0].message.content
        print(input_prompt)
        f = open('recognize_con.txt','w',encoding='utf-8')
        f.write(input_prompt)


        gpt_prompt = [{"role": "system", "content": f'''{input_prompt}라는 감정,상황,행동,언어등이 인식되어 감정을 느꼈다 이모든걸 고려해서 너가 다음으로 취해야하는 행동을 출력해라
                    입력예시: 
                    인식된상황: 주인님이 분노로 휩싸이셔서 해킹하라고 하시며 분노를 주체하지못하고 의자를 부숴버린상황
                    인식감정:분노,흥분
                    인식언어:해킹해 당장 저놈
                    인식행동:의자를 부숨
                    지정할 감정:불안

                    출력예시:
                    화가난 인간을 진정시키기위한 말들을 한다 
                    어떤문제로 지금 이상황까지 왔는지 원인을 찾고 대안을 제시한다

                    

                    이 위 예시 그대로 그어떤 추가및부가 설명없이 예시처럼 비슷한 형식으로만 출력해야만한다
                    
                    
                    
                    '''}]


        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=gpt_prompt,

        )

        input_prompt = response.choices[0].message.content
        print(input_prompt)
        f = open('bigbrainemotion.txt','w',encoding='utf-8')
        f.write(input_prompt)
        
        return input_prompt
        
    def judge(self,prompt):
        



        #prompt 라는 최종 결정을 기반으로 해야하는 행동 및 필요 기관 을 판단하여 일을 수행한다
        #여기서부터 수정다하기

        
        parse_task_demos_or_presteps = open('brain.json', "r",encoding='utf-8').read()
        #prompt = '화가난 인간을 진정시키기위한 말들을 한다, 어떤문제로 지금 이상황까지 왔는지 원인을 찾고 대안을 제시한다'
        messages = json.loads(parse_task_demos_or_presteps)
        messages.insert(0,{"role": "system", "content": f'''#1 Task Planning Stage: The AI assistant can parse user input to several tasks:
        Based on the decision called {prompt}, select and list the tasks and actions that must be performed along with the necessary organizations and print them out as an example. (To connect and list each organization and action together, output them in pairs based on the list of organizations (and explanations) below. do it)
        If you need a capability that is not in the organization list, print None first.
        List of institutions and capabilities:


        Right brain: unconscious (memory, experience, intuition), pattern recognition, metaphor, general, whole, space
        Left Brain: Language, Mathematics, Consciousness, Time, Reason, Simile, Concrete, Exploration
        Cerebrum: vision, hearing, emotions, desires
        Cerebellum: Motor and actual movement control

        Additional organizations:
        Voice agency, search agency, automation agency, imitation agency, connection agency, interpretation agency (programming language), hacking agency, improvement agency,
        If it is determined that an additional institution is necessary, select the necessary institution from the list of additional institutions above.

        Additional organization name: Need

        It is output along with the output in this format.

        If there is no need for additional institutions
        Additional organization: None
        Print in this format


        example :
        Prompt: Says words to calm an angry person. Finds the cause of the problem that has led to the current situation and suggests an alternative.

        thought :

        Left Brain: Say things to calm down an angry person
        Left brain: Find the cause of what problem led to this current situation and suggest an alternative (requires awareness)

        Print :
        Left-brain language skills, you need to say things to calm down angry people,
        Left-brain consciousness, we need to find the cause of what problem has led to this current situation and suggest an alternative.
        Additional organization: None
        '''})
        messages.append({"role": "user", "content": f'Output: Print only the bottom part (Output: You must print only the bottom without this part)'})



        # GPT-3.5 Turbo 모델에 대화 메세지를 보내 응답을 받습니다.
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=messages,

        )

        input_prompt = response.choices[0].message.content
        print(input_prompt)

        print(input_prompt.strip())
        print(input_prompt.split(','))
        input_prompt = input_prompt.split(',')

        print(len(input_prompt))
        num_prompt = len(input_prompt)
        num = num_prompt#6
        for i in range(num_prompt):
            
            print(input_prompt[num_prompt-num])#6-6=0

            f = open('judgement.txt','a',encoding='utf-8')
            f.write(input_prompt[num_prompt-num])
            f.write('\n')
            num -= 1#5,4,3,2,1
            print(num)


        f = open('judgement.txt','r',encoding='utf-8')
                    
        action_list = f.read().splitlines()
        print(action_list)
        action_list = list(map(lambda s : s.strip(), action_list))
        print(action_list)
        plusorgan = action_list[-1]#마지막 요소인 추가기관 부분을 가져온다
        print(plusorgan)

        action_list.remove(plusorgan)

        print(action_list)
        action_num = len(action_list) #5-1=4
        action_num = action_num-1
        action_num = int(action_num/2)
        print(action_num)

        for i in range(action_num):
            

            
            print(action_list)
            actionname = action_list[0]#첫번째 요소를 가져온다
            print(actionname)
            action = action_list[1]
            print(action)
            action_list = list(map(lambda s : s.strip(), action_list))
            f = open('action.txt','w',encoding='utf-8')
            f.write(actionname)

            f.write('\n')
            f.write(action)


            action_list = list(map(lambda s : s.strip(), action_list))
            print(action_list)
            action_list.remove(action)
            action_list.remove(actionname)
            action_list = list(map(lambda s : s.strip(), action_list))
            print(action_list)


            try:
                action_list.remove('')
                print(action_list)

                action_list.remove('')
                print(action_list)
            except:
                print('error')

            print(len(action_list))

            num = len(action_list)

            f = open('judgement.txt','w',encoding='utf-8')
                            
            f.truncate()

            for i in range(num):
                
                
                f = open('judgement.txt','a',encoding='utf-8')
                f.write(action_list[num-num])
                f.write('\n')
                action_list.remove(action_list[num-num])
                print(action_list)



            f = open('action.txt','r',encoding='utf-8')
                            
            action_list = f.read().splitlines()
            print(action_list)
            action_list = list(map(lambda s : s.strip(), action_list))
            print(action_list)

            
            actionname = action_list[0]#첫번째 요소를 가져온다
            print(actionname)
            action = action_list[1]
            print(action)



            if 'smallbrain' in action_list:
                print(action)
                
            if 'leftbrain' in action_list:
                print(action)
                f = open('leftbrain.txt','w',encoding='utf-8')
                f.write(action)
                
            if 'rightbrain' in action_list:
                print(action)
                
            if 'bigbrain' in action_list:
                print(action)

                
            if plusorgan == 'None' :
                print('plusorgan : ',plusorgan)
            if not plusorgan == 'None' :
                print('plusorgan : ',plusorgan)




                parse_task_demos_or_presteps = open('action.json', "r",encoding='utf-8').read()

                input_text = input_prompt
                messages = json.loads(parse_task_demos_or_presteps)
                messages.insert(0,{"role": "system", "content": f'''#1 Task Planning Stage: The AI assistant can parse user input to several tasks:  if user input : {plusorgan}  을 참고하여 예시형식으로 출력해라  또는 행동을 제대로 해라 예시 형식을 그대로 적용해서 제대로 출력해라'''})
                messages.append({"role": "user", "content": f'{input_text}너를 기준으로하여라, 예시 입력한대로 제대로 해라 입력해준 형식대로 적용해서 출력해라'})



                # GPT-3.5 Turbo 모델에 대화 메세지를 보내 응답을 받습니다.
                response = client.chat.completions.create(
                    model="gpt-4-1106-preview",
                    messages=messages,

                )
                print(response.choices[0].message.content)
                input_prompt = response.choices[0].message.content
                print(input_prompt)



                task = input_prompt.strip()
                tasks = json.loads(task)
                tasks = list(tasks)
                num_action = tasks[0]["number of actions"]
                print(num_action)




                for i in range(1,num_action+1):

                    action = tasks[0][f"action {i}"]["required organ"]
                    print(action)
                    if action == 'search':
                        print(action)
                        


                    if action == '':
                        print(action)
                        
                    if action == '':
                        print(action)
                        



                    if action == '':
                        print(action)
                        


                    if action == '':
                        print(action)
                        
                    if action == '':
                        print(action)
                    if action == '':
                        print(action)
                        


                        #여기를 원래 기관판단 기존 코드를 사용해서 나머지 남은 기관들을 판단해서 일을 수행하게 하는 그런부분으로 만들기


            time.sleep(30)
            f = open('judgement.txt','r',encoding='utf-8')
                            
            action_list = f.read().splitlines()
            print(action_list)
            action_list = list(map(lambda s : s.strip(), action_list))
            print(action_list)
            continue



        f = open('action.txt','w',encoding='utf-8')
        f.truncate()




