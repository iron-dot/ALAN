import json
from openai import OpenAI # OpenAI official Python package
import cv2 
import openai
import time
import urllib
from text_to_image import text_image
from text_to_video import text_video

#from text_ppt import ppt_gen
'''from text_excel import text_excel'''

client = OpenAI(api_key="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")



from listToString import listToString



def imagination(tasks):
    
    

    '''
    f = open('dataset/Imagination_connect.txt','r',encoding='utf-8')
    f2 = listToString(f.readlines())

    if f2 == '':
        #커넥션 허용
        pass

    elif f2 is not None:
        print(f2)
        
    try:
        content = f2
    except:

        content = tasks[0]["imagination organ command delivery"]["command content"]'''


    content = tasks[0]["imagination organ command delivery"]["command content"]
    parse_task_demos_or_presteps = open('dataset/demo_parse_task.json', "r").read()

    messages = json.loads(parse_task_demos_or_presteps)

    messages.insert(0,{"role": "system", "content": '''#1 Task Planning Stage: The AI assistant can parse user input to several tasks: [{"task": task, "id": task_id, "dep": dependency_task_id, "args": {"text": text or <GENERATED>-dep_id, "image": image_url or <GENERATED>-dep_id, "audio": audio_url or <GENERATED>-dep_id}}]. The special tag "<GENERATED>-dep_id" refer to the one generated text/image/audio in the dependency task (Please consider whether the dependency task generates resources of this type.) and "dep_id" must be in "dep" list. The "dep" field denotes the ids of the previous prerequisite tasks which generate a new resource that the current task relies on. The "args" field must in ["text", "image", "audio"], nothing else. The task MUST be selected from the following options: "text to video", "text to image", "conversational"  There may be multiple tasks of the same type. Think step by step about all the tasks needed to resolve the user's request. Parse out as few tasks as possible while ensuring that the user request can be resolved. Pay attention to the dependencies and order among tasks. If the user input can't be parsed, you need to reply empty JSON []. '''})
    messages.append({"role": "user", "content": content})
    #print(messages)
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages

    )
    print(response.choices[0].message.content)
    input_prompt = response.choices[0].message.content
    print(input_prompt)

    task = input_prompt.strip()
    print(type(task))
    print(task)




    try:
        tasks = json.loads(task)
        print(tasks)
        if tasks == [] :
            
            gpt_prompt = [{"role": "assistant","content": content}]

            # GPT-3.5 Turbo 모델에 대화 메세지를 보내 응답을 받습니다.
            response = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=gpt_prompt,

            )
            #print(response.choices[0].message.content)
            
            input_prompt = response.choices[0].message.content
            print(input_prompt)

            #continue#처음 입력으로 돌아간다

    except:
        print('error')


    a = -1
    for i in range(len(tasks)):
        a += 1


        print('tasks type',type(tasks))
        tasks = list(tasks)
        print(a)



        try:
            print(tasks[a]["task"])





            #print(tasks[1]["task"])
            task = tasks[a]["task"]
        except:
            gpt_prompt = [{"role": "assistant","content": content}]

            # GPT-3.5 Turbo 모델에 대화 메세지를 보내 응답을 받습니다.
            response = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=gpt_prompt,

            )
            #print(response.choices[0].message.content)
            
            input_prompt = response.choices[0].message.content
            print(input_prompt)

        


        if task == 'text-to-image':
            print('task : ',task)
            print(tasks[a]["args"]["text"])
            text = tasks[a]["args"]["text"]
            prompt = text
            text_image(prompt)


        if task == "text-to-video":
            print('task : ',task)
            print(tasks[a]["args"]["text"])
            text = tasks[a]["args"]["text"]
            prompt = text
            mp4 = text_video(prompt)


            

            
            cap = cv2.VideoCapture(mp4)
            ret, frame = cap.read()
            while(1):
                ret, frame = cap.read()
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                cv2.imshow('frame',frame)
        '''if task == 'text_ppt':
            print('task : ',task)
            print(tasks[a]["args"]["text"])
            prompt = tasks[a]["args"]["text"]
            f = open('dataset/Imagination.txt','r',encoding='utf-8')

            Imagination_data = listToString(f.readlines())
            #Imagination_data로 ppt생성하기
            prompt,file_name = prompt.split('\n')

            #prompt는 여기 이기관이 할 작업이다(texttoppt에 작업). 쓸수도 있고 필요없을수도있다



            f = open('dataset/'+file_name+'.txt','w',encoding='utf-8')#현재 가정으로 summary.txt읽어오기
            f.write('topic 기반 ppt생성')



            print(f'topic 기반 ppt생성')


            
            f = open('summary.pptx','a',encoding='utf-8')
            f.write()

            
            여기서 ppt생성하기'''

            #text_ppt(prompt)
            #f2를 이용해서 ppt만들기
            #나중에는 f2를 이용해서 생성기관으로 할수있는 것들 수행 하기
            
        if task == 'text_excel':
            print('task : ',task)
            print(tasks[a]["args"]["text"])
            prompt = tasks[a]["args"]["text"]
            #text_excel(prompt)
            
        

        else:
            print('task : None')

#추가 작업할것 : ppt excel데이터셋에 추가하기


