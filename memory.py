
#research : 탐
#AGI로의 힌트
#경험을 바탕으로 인간은 학습하고 성장한다
#기억의 원리는 단기기억과 장기기억이 있고 장기기억을 삭제하고 그 조금의 부분을 다른 망상같은 환상과 합쳐져서 왜곡된다
#인간은 경험과 학습을 통해 새로운 능력을 얻는다 
#각기관별 생각을 할수있게 한다
#프롬프트만 잘쓰면 인간처럼 만들수있다
#무작위로 이루어진 알수없는 코드가 자유의지와 자아를 만든다 (아이작 아시모프의 소설 아이로봇)
#앨런이란 이름으로 인공지능이 앨런튜링같은 모델이되게 학습시켜야함
'''좌뇌 : 시간 이성 단어 부분 분석 수리 의식 직유 구체적 언어
우뇌 : 공간 감정 소리 전체 직관 패턴 무의식 은유 일반적(일반적으로 사람이라면 다 아는 기초 지식 당연한것들) 시각'''
#인간의 모든것을 구현하되 인간보다 더 성능좋게 작업을 더 빠르게 처리하는 영원한 우리의 동반자이자 종으로써 필요없는 부분들을 제거하고 완벽히 작업을 수행하는데 효율적인 모델로 만들어낸다

#작은것부터 시작하라는 말이 있다 해커 AI 만들고 이번엔 인간이 기억하는 원리를 기반으로 기억하는 AI 를 개발해보자 차근차근 만들고 결합 하기
#끊임없이 생각하고 탐구하는것이 인간이 더 성장하고 지능을 올리며 진화하는 기본적인 방법이다 이걸 모방하여 계속 탐구하는 모델도 만들고 기관으로(생각기관 결합) 만들어보자 (결국 이걸 쉽게말하면 호기심이 되긴한다)
#탐구 질문들 : https://post.naver.com/viewer/postView.nhn?volumeNo=10486980&memberNo=1516732, https://book.mk.co.kr/book_view/9788970417660/
#지피티로 탐구질문들도 만들어보기 또한 쓸만한 링크들 : https://fire7983.tistory.com/191, https://inmun360.culture.go.kr/content/361.do?mode=view&cid=2365354, https://brunch.co.kr/@ysseo21/714 여러 질문 있는 책도 좀 사보자 또한 질문들을 좀 답할수있게 생각할만한 철학이나 질문학습한 데이터셋이나 모델도 만들기
#https://jakiva.tistory.com/entry/%EC%A2%8B%EC%9D%80-%EC%A7%88%EB%AC%B8%EC%9D%B4-%EC%A2%8B%EC%9D%80-%EC%9D%B8%EC%83%9D%EC%9D%84-%EB%A7%8C%EB%93%A0%EB%8B%A4 (file:///C:/Users/asus/Downloads/%EC%B1%85%20%EB%B0%9C%EC%B7%8C%20-%20%EC%A2%8B%EC%9D%80%20%EC%A7%88%EB%AC%B8%EC%9D%B4%20%EC%A2%8B%EC%9D%80%20%EC%9D%B8%EC%83%9D%EC%9D%84%20%EB%A7%8C%EB%93%A0%EB%8B%A4.pdf) 이거 학습시켜서 질문 만드는 모델도 만들기 
#여기에는 내가 구현해내면 인정받을 내용도 있다 협업 : 이것도 진짜 중요하니 개발좀 해볼것, https://www.aitimes.kr/news/articleView.html?idxno=26490
#자기개선을 위한 self discover, self reflection, gpt engineer self improvement and devin : ai software engineer 오류 수정 기능 포함할것 
# 데빈 오픈소스 버전 (성능은 조금낮음 간단화됬음) : https://github.com/ItzCrazyKns/Not-Devin, https://github.com/coolnj4/AI-Agents-and-Software-Development, https://github.com/topics/devin 여기서 잘찾아보기
#지적을 받고 그지적을 반영하여 데이터추가하고 다음부터 그지적에 맞게 반영하여 실수안하게하기
#상황같은거 지정해줘서 인식된상황에 맞게 걍 스스로 판단해서 명령없이도 알아서 뭔가 작업하는기능 추가하기

#!pip install pandas datetime collections sqlite3 openai pytz

import pandas as pd
from datetime import datetime
from collections import deque
import pytz
from listToString import listToString
from openai import OpenAI # OpenAI official Python package

client = OpenAI(api_key="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")
input_text = input(':')
gpt_prompt = [{"role": "assistant","content": f"""
               입력예시:
                자기자신 스스로의 감정: 기쁨,
                상황: 주인이 오랜 시간을 기다린 인터뷰 결과가 양호하게 나왔다는 소식을 듣고, '오랜 기다림 끝에 인터뷰 결과가 양호하게 나왔다는 소식을 듣고 행복하다.'라고 웃는 상황이 발생했다.,
                욕구 : 이타심
                
               



               이런 입력들을 받았을때 위 값을 아래 예시처럼 출력해라

               출력예시:
               주인이 오랜 시간을 기다린 인터뷰 결과가 양호하게 나왔다는 소식을 듣고 '오랜 기다림 끝에 인터뷰 결과가 양호하게 나왔다는 소식을 듣고 행복하다'라고 웃는 상황이 발생했다,기쁨,이타심


               
               
               """},
               {"role": "user","content": f"""입력:{input_text}"""}]


response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=gpt_prompt,

)

print(response.choices[0].message.content)
input_prompt = response.choices[0].message.content
print(input_prompt)
input_prompt = input_prompt.split(',')
print(type(input_prompt))
print(input_prompt)


class MemoryAgent:
    def __init__(self):
        # Create empty CSV files if they don't exist
        self.create_empty_csv_files()
        self.csv_files = ['semantic_memory.csv', 'episodic_memory.csv']
        self.load_data()

    def create_empty_csv_files(self):
        try:
            pd.read_csv("semantic_memory.csv", encoding='utf-8-sig')
        except FileNotFoundError:
            pd.DataFrame(columns=["korea_timestamp", "utc_timestamp", "experience", "emotion", "desire", "age","response"]).to_csv("semantic_memory.csv", index=False)

        try:
            pd.read_csv("episodic_memory.csv", encoding='utf-8-sig')
        except FileNotFoundError:
            pd.DataFrame(columns=["korea_timestamp", "utc_timestamp", "experience", "emotion", "desire", "age","response"]).to_csv("episodic_memory.csv", index=False)

    def load_data(self):
        # Load existing data from CSV files
        self.semantic_memory = pd.read_csv("semantic_memory.csv").to_dict("records")
        self.episodic_memory = pd.read_csv("episodic_memory.csv").to_dict("records")

    def save_data(self):
        # Save data to CSV files
        for filename, data in zip(self.csv_files, [self.semantic_memory, self.episodic_memory]):
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)

    def encode_experience(self, experience, emotion, desire, age,response):
        # Encode and store experience
        korea_timezone = pytz.timezone('Asia/Seoul')
        utc_timezone = pytz.utc
        korea_time = datetime.now(korea_timezone)
        utc_time = datetime.now(utc_timezone)
        korea_timestamp = korea_time.strftime('%Y-%m-%d %p %I:%M:%S')
        utc_timestamp = utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        self.semantic_memory.append({"korea_timestamp": korea_timestamp, "utc_timestamp": utc_timestamp, "experience": experience, "emotion": emotion, "desire": desire, "age": age,"response":response})
        self.episodic_memory.append({"korea_timestamp": korea_timestamp, "utc_timestamp": utc_timestamp, "experience": experience, "emotion": emotion, "desire": desire, "age": age,"response":response})
        self.save_data()

# Example scenario
experience = input_prompt[0]
emotion = input_prompt[1]
desire = input_prompt[2]

f = open('age.txt','r',encoding='utf-8')
age = listToString(f.readlines())
response = ''#이제 인격생각체가 한 행동 및 정확히는 이 모델이 여기 있는 상황에서 욕구와 감정을 가진상태로 한 행동 을 넣는다

# Create memory agent
agent = MemoryAgent()

# Encode and store experience
agent.encode_experience(experience, emotion, desire, age, response)



'''
1살부터 30살까지 각 나이대별로 겪을만한 현실적인 일들을 경험, 감정, 욕구를 포함하여 생성해보겠습니다.

1 year old
Experience: “Taking the first step.”
Emotion: “Joy”
Need: “Exploration”
2 years old
Experience: “Say your first word.”
Emotion: “Excited.”
Need: “Communication”
3 years old
Experience: “Going to kindergarten for the first time.”
Emotion: "Curiosity"
Need: “Socialization”
4 years old
Experience: “Make your first friend.”
Emotion: “Joy”
Need: “Friendship”
5 years old
Experience: “Going to an amusement park.”
Emotion: "Happy"
Need: “Pleasure”
6 years old
Experience: “Entering school.”
Emotion: “Excited.”
Need: “Learn”
7 years old
Experience: “Giving my first class presentation.”
Emotion: "Nervous"
Need: “Recognition”
8 years old
Experience: “Solving math problems.”
Emotion: “Sense of accomplishment”
Need: “Challenge”
9 years old
Experience: “Participating in my first sports day.”
Emotion: “Happy”
Need: “Cooperation”
10 years old
Experience: “Reading your favorite book.”
Emotion: "Curiosity"
Need: “Knowledge”
11 years old
Experience: “Going on my first trip.”
Emotion: “Excited.”
Desire: “Adventure”
12 years old
Experience: “Attending the middle school entrance ceremony.”
Emotion: "Nervous"
Desire: “New”
13 years old
Experience: “Make new friends.”
Emotion: “Joy”
Need: “Socialization”
14 years old
Experience: “Get a good grade on my first exam.”
Emotion: “Proud”
Need: “Accomplishment”
15 years old
Experience: “Falling in love for the first time.”
Emotion: “Excited”
Desire: “Love”
16 years old
Experience: “Participating in a hobby.”
Emotion: “Happy”
Need: “Fun”
17 years old
Experience: “Preparing for college entrance exams.”
Emotion: “Anxiety.”
Need: “Goal”
18 years old
Experience: “Attending a high school graduation ceremony.”
Emotion: “Gratitude”
Need: “Growth”
19 years old
Experience: “Having my first part-time job.”
Emotion: “Sense of Independence”
Need: “Self-reliance”
20 years old
Experience: “Attending a university entrance ceremony.”
Emotion: “Excited.”
Need: “Learn”
21 years old
Experience: “Going on a trip abroad.”
Emotion: “Excited”
Need: “Exploration”
22 years old
Experience: “Doing my first internship.”
Emotion: “Pride”
Need: “Experience”
23 years old
Experience: “Writing a senior thesis.”
Emotion: “Stress”
Need: “Accomplishment”
24 years old
Experience: “Joining your first job.”
Emotion: “Excited.”
Need: “Growth”
25 years old
Experience: “Took on my first project at work.”
Emotion: “Pride”
Need: “Accomplishment”
26 years old
Experience: “Moving to a new city.”
Emotion: “Excited”
Desire: “New”
27 years old
Experience: “Get a promotion.”
Emotion: “Joy”
Desire: “Success”
28 years old
Experience: “Buying my first home.”
Emotion: “Proud”
Need: “Stability”
29 years old
Experience: “Having a wedding.”
Emotion: “Happy”
Desire: “Love”
30 years old
Experience: “Having my first child.”
Emotion: "Inspired"
Need: “Family”


'''




