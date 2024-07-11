import main
import leftbrain  
from listToString import listToString
from bigbrain import bigbrain
from rightbrain import Rightbrain
from Consciousness import conscious_opinion

'''
class NeuralTransmissionSubstance:
    def __init__(self) :
        
        """
        신경 전달 물질: 다른 기관들로 정보를 전달하는 역할, 연결기관이랑 연관이 깊음
        """
        f = open('nts.txt','r',encoding='utf-8')
        f2 = listToString(f.readlines())
        self.nts = f2
        f.truncate()
    def run(self):
        print(self.nts)
        return self.nts
'''




class PersonalityEntity(leftbrain,bigbrain):
    #나이 설정 : 사용자 및 유저들에 평가를 받아 나이를 결정한다 평가가 상위권이면 나이를 올리고 (1살) 중위권이면 유지하나 점수 조금 반영해놓고 다음평가에 추가점수로 반영한다 또한 하위권점수도 반영할땐 반영한다 평가는 정기평가로 2달에 한번씩 평가한다
    """
    인격 생각체: 모든 판단과 결정을 처리하고 최종 결정을 내리는 역할
    """

    def __init__(self, name, prompt):
        self.alan = main.Alan
        self.name = name
        self.leftbrain = leftbrain.LeftBrain
        #self.nts = NeuralTransmissionSubstance.run()
        self.prompt = prompt
        self.bigbrain = bigbrain()
        self.rightbrain = Rightbrain()
        self.con = conscious_opinion


    def run(self):
        

        

        #여러 사물인식및 다른 동물같은것도 인식해서 여러가지 많은 요소를 갖고 상황판단하는 인간이랑 최대한 똑같이 만든다
        
        try:
            input_action = self.bigbrain.emotion()#1차판단결과를 좌뇌 의식속으로 전송한다 
        except:
            f = open('bigbrainemotion.txt','r',encoding='utf-8')
            input_action = listToString(f.readlines())



        f = open('situation.txt','r',encoding='utf-8')
        situation = listToString(f.readlines())

        con = self.bigbrain.judge_con(situation)
        if 'consciousness' in con:
            content = self.con(input_prompt)# 2차판단 진행 여기수정
            prompt = self.alan.personity(content)#2차판단결과를 바탕으로 최종결정을 내린다
            self.bigbrain.judge(prompt)#대뇌로 최종결과를 전송한다 , 우뇌사용시 인격생각체에게 이미 행동 처리했으니 적합한지 판단해달라요청해서 판단 받기

        else:

            

            input_text = situation#상황

            # 직관적 제안 받기(직관적 처리)
            self.rightbrain.memory_use(input_text)


            f = open('Intuition.txt','r',encoding='utf-8')
            Intuition = listToString(f.readlines())


            self.alan.personity(Intuition+'이것은 적합한 조치였는지 판단해줘(평가해줘)')#2차판단결과를 바탕으로 최종결정을 내린다
            #self.bigbrain.judge(prompt)#대뇌로 최종결과를 전송한다 , 우뇌사용시 인격생각체에게 이미 행동 처리했으니 적합한지 판단해달라요청해서 판단 받기
            
            
#무의식 의식 동시에 처리가능하게 그리고 더 빠른 속도로 작업 처리하게 모델전반적으로 더 좋은 리소스가 필요하다

            
            
            


        
        
        # 두 개의 스레드를 생성
        


        #얘가 위 작업들 다 수행후 자기가 한 작업들 쉽게 말해 경험을 저장한다
        
        f = open('age.txt', 'r', encoding='utf-8')#성능평가 점수에 따라 나이를 늘린다 나이 지정 코드 만들기
        age = listToString(f.readlines())
        
        f = open('recognize_con.txt','r',encoding='utf-8')
        input_prompt = listToString(f.readlines())
        input_prompt = input_prompt.split(':')
        emotion = input_prompt[-1]#마지막 부분
        experience = prompt
        emotion = emotion#감정
        desire = 'None'
        response = input_action#취한 행동
        # 경험을 저장
        self.rightbrain.memory_save(experience, emotion, desire, age,response)






class IndependentModule:
    """
    독립적으로 작동하는 기능 모듈
    """

class SpeechModule(IndependentModule):
    """
    음성 인식 및 처리 기능 모듈
    """

class SearchModule(IndependentModule):
    """
    검색 기능을 담당하는 모듈
    """

class AutomationModule(IndependentModule):
    """
    자동화 기능을 담당하는 모듈
    """

class MimicryModule(IndependentModule):
    """
    모방 기능을 담당하는 모듈
    """

class ConnectionModule(IndependentModule):
    """
    연결 기능을 담당하는 모듈
    """

class TranslationModule(IndependentModule):
    """
    번역 기능을 담당하는 모듈
    """

class HackingModule(IndependentModule):
    """
    해킹 기능을 담당하는 모듈
    """
PersonalityEntity.run()