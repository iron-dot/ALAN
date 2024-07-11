'''연결기관을 통해 여러 기관이 협력해야하는상황일때 방법을 생각해야한다
연결기관이 action  에 있으면 액션에서 필요하다 판단한 기관들은 연결기관에서 보낸것들을 받는다 (연결기관은 그걸 보내는 코드까지 구현하고 나머지는 액션에 연결기관있으면 나머지기관들이 필요한거  받는 코드 구현하기)
'''

import json
import time


import torch


from openai import OpenAI # OpenAI official Python package
from langdetect import detect

#[{\"situation\": \"Summary of the input paper PDF file, organize it briefly in ppt, and explain the summarized content using voice AI.A situation where you have to make a video and upload it to YouTube \", \"visual recognition\": \"None\", \"auditory recognition\": \"Look at this file, summarize and brieflyOrganize it in ppt. Oh, please make a YouTube video script (explaining it) and upload it to YouTube. The file is 2402.13616v1.pdf\", \"judgment\": \"As a result of my judgment, first of all, Find the pdf file, check it, summarize the contents, organize the summarized contents into a ppt using the ppt creation function at the creation agency, and then make the summary into a script.Create shorts by applying the script as is through the shorts creation function in the creation agency. At this time, it must be a short that directly explains through the AI voice function. Next, the macroThrough this function, you can directly connect to YouTube and automatically upload the video to your account channel \", \"decision\": \"Accepted the command\", \"number of actions\":6, \"action 1\": {\"action description\": \"Search for pdf file\",\"required organ\": \"search organ\"}, \"action 2\": {\"action description\":\"Read pdf file\",\"required organ\": \"auto organ\"}, \"action 3\": {\"action description\": \"Summary PDF contents\",\"required organ\": \"Language organ\"}, \"action 4\": {\"action description\": \"Create ppt based on the summary\",\"required organ\": \" imagination organ\"},\"action 5\": {\"action description\": \"Make the summary into a script\",\"required organ\": \"Language organ\"},\"action 6 \": {\"action description\": \"Creates shorts\",\"required organ\": \"imagination organ\"},\"motor organ command delivery\": {\"command content\":\"None\"}, \"visual organ command delivery\":{\"command content\": \"None\"}, \"Language organ command delivery\": {\"command content\": \"Summary PDF files and create scripts pdf file is {2402.13616v1.pdf}\"}, \"imagination organ command delivery\": {\"command content\": \"Receive the summary from the language institute as a txt file, read it, and create the contents as a ppt (collaboration)\"} }]

client = OpenAI(
                api_key="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")

def connection(input_text,input_prompt):
    
  prompt = "Look at this file, summarize it, and organize it briefly in a ppt, etc. Please make an audio file (explaining) the script. The thesis file is 2402.13616v1.pdf."

  commend = input_text


  input_prompt = input_prompt
  # 중앙뇌 brain 기관 출력 결과 : input_prompt

  #데이터셋 수정해야한다 커넥션(각기관들 협력 판단여부)이
  #true이면 어떤기관들끼리 협력해야하는지 판단한거 action 판단 한것처럼 만들어서 첫번째
  #connection이런식으로 단 한번 커넥션에는 두개의 기관들끼리 차례차례 연결되게 진행하게하고 커넥션
  #사항 을 판단해서 가져오고 다른 기관들 그러니까 협력될 기관들은 커넥션이 트루면 파일 읽기를 시작하게하여
  #커넥션기관을 통한 협력및 복잡한 작업 해결능력이 구현된다

  ex_situation = "[{\"situation\": \"Summary of the input paper PDF file, organize it briefly in ppt, and explain the summarized content using voice AI.A situation where you have to make a video and upload it to YouTube \", \"visual recognition\": \"None\", \"auditory recognition\": \"Look at this file, summarize and brieflyOrganize it in ppt. Oh, please make a YouTube video script (explaining it) and upload it to YouTube. The file is 2402.13616v1.pdf\", \"judgment\": \"As a result of my judgment, first of all, Find the pdf file, check it, summarize the contents, organize the summarized contents into a ppt using the ppt creation function at the creation agency, and then make the summary into a script.Create shorts by applying the script as is through the shorts creation function in the creation agency. At this time, it must be a short that directly explains through the AI voice function. Next, the macroThrough this function, you can directly connect to YouTube and automatically upload the video to your account channel (connection의 필요성을 확인함)\", \"decision\": \"Accepted the command\", \"number of actions\":7, \"action 1\": {\"action description\": \"연결시작\",\"required organ\": \"connection organ\"},\"action 2\": {\"action description\": \"Search for pdf file\",\"required organ\": \"search organ\"}, \"action 3\": {\"action description\":\"Read pdf file\",\"required organ\": \"auto organ\"}, \"action 4\": {\"action description\": \"Summary PDF contents\",\"required organ\": \"Language organ\"}, \"action 5\": {\"action description\": \"Create ppt based on the summary\",\"required organ\": \" imagination organ\"},\"action 6\": {\"action description\": \"Make the summary into a script\",\"required organ\": \"Language organ\"},\"action 7 \": {\"action description\": \"Creates shorts\",\"required organ\": \"imagination organ\"},\"motor organ command delivery\": {\"command content\":\"None\"}, \"visual organ command delivery\":{\"command content\": \"None\"}, \"Language organ command delivery\": {\"command content\": \"Summary PDF files and create scripts pdf file is {2402.13616v1.pdf}\"}, \"imagination organ command delivery\": {\"command content\": \"Receive the summary from the language institute as a txt file, read it, and create the contents as a ppt (collaboration)\"} }]"



  gpt_prompt = [{"role": "assistant","content": f'''
  예시를 먼저보여주겠다 예시랑 비슷하게 하면된다
  전체 명령은 "재밌는 프로젝트 아이디어 아무거나 하나 생성하고 ppt를 생성해줘"이고 언어기관은 아무거나 재밌는 아이디어 생성해줘라는 액션이 주어지며그걸 수행하여 생성기관애 전송해주어야한다 여기까지는 기본 판단이고

  이걸 정리해서
  만약
  전체 입력 : "재밌는 프로젝트 아이디어 아무거나 하나 생성하고 ppt를 생성해줘"
  입력 예시 : "재밌는 프로젝트 아이디어 생성(Language), ppt생성(Imagination)"

  출력 예시:

  자동화된 정원 관리 시스템
  Language->Imagination

  만약 길고 복잡한 작업일경우 :

  전체 입력 : {prompt}
  예시 입력: {ex_situation}


  출력 예시: 아래것들 전부 출력해야하는것들이다

  Search for pdf file 2402.13616v1.pdf,search organ->auto organ
  Read pdf file,auto organ->Language organ
  Summary PDF contents,Language organ->Imagination organ
  Create ppt based on the summary,Imagination organ->Language organ
  Make the summary into a script based on summary,Language organ->Imagination organ
  Creates shorts based on script,Imagination organ
  6


  두번째 예시:
    

  출력 예시 그대로 형식 대로 그대로 딱 저것들만 출력해야만한다 다른 어떠한 부가설명도필요없고 다른 출력도 절대 할수없다'''},


  {"role": "user","content": f'입력 : {input_prompt}, 전체 입력 : {commend}'}]


  #나중에 저 형식을 출력하는 원리에 대해 설명하고 학습시켜서 규칙을 스스로 찾아내어 다른 일에도 적용할수있게 만들기
  response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=gpt_prompt

  )


  input_prompt = response.choices[0].message.content


  input_prompt = input_prompt.split('\n')

  num_con = len(input_prompt)

  a = 0
  connection_n = int(input_prompt[num_con-1])
  for i in range(connection_n):
      
      sent_infor = input_prompt[a]
      a += 1
      out_list = sent_infor.split(',')
      print(out_list)
      
        
      sent_message = out_list[0]
      try:
          con_judge = out_list[1]
      
          sent,receive = con_judge.split('->')
          print('보내는곳:',sent)
          print('전달사항:',sent_message)
          print('받는곳:',receive)

      except:
          sent = con_judge
          print(sent_message)
          print(sent)

      if 'search organ' in sent:

          print('checking')
          f = open('dataset/search_connect.txt','w',encoding='utf-8')
          f.write(sent_message)
          f.write('\n')
          f.write(receive)
          print('search connect 전달 완료')
          
      if 'auto organ' in sent:
          
          print('checking')
          f = open('dataset/auto_connect.txt','w',encoding='utf-8')
          f.write(sent_message)
          f.write('\n')
          f.write(receive)
          print('auto connect 전달 완료')


      if 'Language organ' in sent:
          print('checking')
          f = open('dataset/Language_connect.txt','w',encoding='utf-8')
          f.write(sent_message)
          f.write('\n')
          f.write(receive)
          print('Language connect 전달 완료')

      if 'Imagination organ' in sent:
          print('checking')
          f = open('dataset/Imagination_connect.txt','w',encoding='utf-8')
          f.write(sent_message)
          f.write('\n')
          f.write(receive)
          print('Imagination connect 전달 완료')
      if 'speech organ' in sent:
          print('checking')
          f = open('dataset/Imagination_connect.txt','a',encoding='utf-8')
          #f.write('\n')
          f.write(sent_message)
          f.write('\n')
          f.write(receive)

          

          lang = detect(sent_message) 
          f.write(lang)
        

      print('되돌아간다')



#나중에 스마트 홈 자동화 구현하기 위해 준비하고 연결 능력 더 만들기 지금은 이정도로 만족하기



  '''
  from openai import OpenAI # OpenAI official Python package

  client = OpenAI(api_key="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")

  # 가상의 커넥션 상태 (True 또는 False)를 가정합니다.
  connections = {
      'translate': False,
      'auto': False,
      'visual': False,
      'motor': False,
      'search': False,
      'research': False,
      'Imagination': False,
      'Language': False,
      'Calculation': False,
      'audiory': False,
      'hacking': False,
      'memory': False,
      'improve': False,
      'imitation': False,
      'speech': False,
      'connect': False,
  }



  # 커넥션 상태가 True인 기관들끼리 협력하도록 설정합니다.
  for org, connected in connections.items():
      if connected:
          # ChatGPT API 호출
          gpt_prompt = [{"role": "assistant","content": f""}]
          response = client.chat.completions.create(
              model="gpt-4-1106-preview",
              messages=gpt_prompt
              
          )
          # 생성된 대화 출력
          input_prompt = response.choices[0].message.content
          print(input_prompt)

          # 여기에 파일 읽기 작업을 추가하세요 (예: 파일 열기, 데이터 읽기 등)

  # 다른 기관들은 협력되지 않습니다.

  '''