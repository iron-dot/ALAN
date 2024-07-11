import random
from openai import OpenAI # OpenAI official Python package


#!pip install pandas datetime collections sqlite3 openai pytz
#!pip install openai
import pandas as pd
from datetime import datetime
from collections import deque
import pytz
#from listToString import listToString
from openai import OpenAI # OpenAI official Python package
import random
class MemoryAgent:
    def __init__(self):
        self.create_empty_csv_files()
        self.csv_files = ['semantic_memory.csv', 'episodic_memory.csv']
        self.load_data()
        self.intuition = Intuition(self.semantic_memory, self.episodic_memory)
        self.subconsciousness = Subconsciousness(self.semantic_memory, self.episodic_memory)


    def create_empty_csv_files(self):
        try:
            pd.read_csv("semantic_memory.csv", encoding='UTF-8-sig')
        except FileNotFoundError:
            pd.DataFrame(columns=["korea_timestamp", "utc_timestamp", "experience", "emotion", "desire", "age","response"]).to_csv("semantic_memory.csv", encoding='UTF-8-sig', index=False)
            
        try:
            pd.read_csv("episodic_memory.csv", encoding='UTF-8-sig')
        except FileNotFoundError:
            pd.DataFrame(columns=["korea_timestamp", "utc_timestamp", "experience", "emotion", "desire", "age","response"]).to_csv("episodic_memory.csv", encoding='UTF-8-sig', index=False)

    def load_data(self):
        # Load existing data from CSV files
        self.semantic_memory = pd.read_csv("semantic_memory.csv", encoding='UTF-8-sig').to_dict("records")
        self.episodic_memory = pd.read_csv("episodic_memory.csv", encoding='UTF-8-sig').to_dict("records")
        print(self.episodic_memory)
    def save_data(self):
        # Save data to CSV files
        for filename, data in zip(self.csv_files, [self.semantic_memory, self.episodic_memory]):
            df = pd.DataFrame(data)
            df.to_csv(filename, encoding='UTF-8-sig',index=False)

    def encode_experience(self, experience, emotion, desire, age,response):
        # Encode and store experience
        korea_timezone = pytz.timezone('Asia/Seoul')
        utc_timezone = pytz.utc
        korea_time = datetime.now(korea_timezone)
        utc_time = datetime.now(utc_timezone)
        korea_timestamp = korea_time.strftime('%Y-%m-%d %p %I:%M:%S')
        utc_timestamp = utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        self.semantic_memory.append({"korea_timestamp": korea_timestamp, "utc_timestamp": utc_timestamp, "experience": experience, "emotion": emotion, "desire": desire, "age": age, "response":response})
        self.episodic_memory.append({"korea_timestamp": korea_timestamp, "utc_timestamp": utc_timestamp, "experience": experience, "emotion": emotion, "desire": desire, "age": age, "response":response})
        self.save_data()

    def get_intuitive_suggestion(self,prompt):
        # 직관적 제안을 제공합니다.
        return self.intuition.make_suggestion(prompt)

    def run_subconscious_processing(self):
        # 무의식적 분석을 수행합니다.
        self.subconsciousness.analyze_memories()


class Intuition:
    """
    직관적으로 판단하는 부분
    """
    def __init__(self, semantic_memory, episodic_memory):
        self.semantic_memory = semantic_memory
        self.episodic_memory = episodic_memory

    def make_suggestion(self,input_text):
        if self.semantic_memory:
            # 과거의 기억을 기반으로 제안합니다.
            from openai import OpenAI # OpenAI official Python package

            client = OpenAI(api_key="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")
            #input_text = input(':')


            gpt_prompt = [{"role": "assistant","content": f"""

                          입력에 대해 {self.episodic_memory}여기에서 비슷한 케이스의 경험(기억)을 찾아서 참고하고 현재 입력(상황)에 대한 해결책을 제안하라
                          아래예시도 참고해서 출력해라

                          출력예시:
                          입력 이라는 상황에 닥친 지금 과거의 기억에서 유사한 상황인 을 찾았고 현상황에 대한 현실적이고 실천가능한 해결책으로 을 제안합니다

                          유사한상황없으면 너의 생각으로 해결책 제시하여야한다 가장 알맞는 한가지를 위 형식으로 출력하여라

                          

                          """},
                          {"role": "user","content": f"""입력:{input_text}"""}]


            response = client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=gpt_prompt,

            )


            input_prompt = response.choices[0].message.content
            print(input_prompt)

            #random_memory = random.choice(self.semantic_memory)
            suggestion = input_prompt#f"과거 경험 '{random_memory['experience']}'을 바탕으로, 유사한 상황에서는 '{random_memory['emotion']}'을 느낄 수 있고 '{random_memory['desire']}'을 원할 수 있습니다."
            return suggestion
        else:
            #print('기억이 없습니다')

            return "기억이 없습니다."


class Subconsciousness:
    """
    무의식을 처리하고 미리 처리하는 부분
    """
    def __init__(self, semantic_memory, episodic_memory):
        self.semantic_memory = semantic_memory
        self.episodic_memory = episodic_memory

    def analyze_memories(self):
        
        # 예: 감정 빈도를 분석합니다.
        emotion_count = {}
        for memory in self.semantic_memory + self.episodic_memory:
            emotion = memory.get("emotion")
            if emotion:
                if emotion in emotion_count:
                    emotion_count[emotion] += 1

                else:
                    emotion_count[emotion] = 1

        print(f"감정 빈도 분석 결과: {emotion_count}")




class Rightbrain:
    def __init__(self,age,emotion,experience,response,desire):
        self.age = age
        self.emotion = emotion
        self.experience = experience
        self.response = response
        self.desire = desire
        
    def memory_save(self):
        agent = MemoryAgent()


        # 경험을 저장
        agent.encode_experience(self.experience, self.emotion, self.desire, self.age, self.response)

    def memory_use(self,input_text):
        agent = MemoryAgent()


        # 직관적 제안 받기
        suggestion = agent.get_intuitive_suggestion(input_text)
        print(f"직관적 제안: {suggestion}")


        f = open('Intuition.txt','w',encoding='utf-8')
        f.write(f"직관적 결정: {suggestion}")
        f.write('\n')
        



        # 무의식적 처리 실행
        agent.run_subconscious_processing()

        #직관적인 결정에 따라 소뇌를 적극적으로 사용하되 그외에 기관은 완만해선 사용하지않고 우뇌 자체적으로 기억을 바탕으로 행동한다 (단 기억을 활용해도 우뇌로써 어려운일은 하지않는다)(의식으로 이동?)
        #여기에 이제 소뇌를 적극적으로 활용하는 예제가 필요하다
        #내가 오늘 (방금까지 무슨행동을 했더라 나 뭐하고있었지) 라는 자기탐구는 모델작동 동시에 진행되고있어야한다

        #https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/LQR.ipynb#scrollTo=Xqo7pyX-n72M
        #이 코드들이 가상로봇실현에 핵심이다
        if suggestion :
            print()





class SpaceCenter:
    """
    공간에 대한 감각을 담당하는 부분
    """
    

#항상동시에 (멀티스레딩)



'''
ChatGPT
인간이 사칙연산을 수행할 때, 1+1 같은 단순한 계산은 보통 무의식적으로 이루어집니다. 일상 생활에서 이런 간단한 계산은 우리가 수많은 경험과 훈련을 통해 익숙해져서 더 이상 의식하지 않고도 빠르게 처리됩니다. 하지만 복잡한 계산이나 새로운 문제에 직면하면 의식적인 계산이 필요할 수 있습니다. 그러면 머릿속에서 문제를 해결하고 숫자를 조작하면서 답을 찾게 됩니다.


'''


