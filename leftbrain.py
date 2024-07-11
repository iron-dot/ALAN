from calculation import calculation
from language import language
from Consciousness import consciousness
from time_manage import check_schedules,process_command
from openai import OpenAI # OpenAI official Python package
import threading
class LeftBrain:
    """
    좌뇌:
    - 수리(수학) 기능 담당
    - 시간에 대한 감각 제어
    - 의식적 행동을 감지하고 처리
    - 언어 처리 기능
    """
    
    def MathCenter(prompt):
        """
        수리(수학) 기능을 담당하는 부분
        """
        calculation(prompt)


    def Consciousness(a,b,c,d):
        """
        의식적 행동을 감지하고 처리하는 부분
        """
        consciousness(a,b,c,d)

    def LanguageCenter(prompt):
        """
        언어 처리 기능을 담당하는 부분
        """
        language(prompt)


    def TimeCenter(prompt):
        """
        시간에 대한 감각을 담당하는 부분
        """
        schedules = {}

        # 스케줄 확인 스레드 시작
        schedule_thread = threading.Thread(target=check_schedules, args=(schedules,))
        schedule_thread.daemon = True
        schedule_thread.start()

        command = prompt#recognize_voice_command()
        if command:
            process_command(command)









    def main(self,prompt):
        
        




        client = OpenAI(
            api_key="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")
        prompt = input(':')
        gpt_prompt = [{"role": "system", "content": f'''{prompt}에 알맞는 능력을 능력 목록에서 선택하고 아래예시처럼 출력하고 또한 능력개수도 함께 아래예시처럼출력한다
                        능력 목록 : 언어, 수학, 시간, 의식

                        입력예시(prompt):
                        Left-brain language skills, you need to say things to calm down angry people,
                        Left-brain consciousness, we need to find the cause of what problem has led to this current situation and suggest an alternative.
                        

                        출력예시:
                        언어, you need to say things to calm down angry people,
                        의식, we need to find the cause of what problem has led to this current situation and suggest an alternative,
                        능력개수,2


                    '''}
                        ]

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=gpt_prompt,

        )

        input_prompt = response.choices[0].message.content
        print(input_prompt)

        input_prompt = input_prompt.split(',')
        input_prompt = [l.strip('\n') for l in input_prompt]
        print(input_prompt)

        for i in range(int(input_prompt[-1])):
            if '언어' in input_prompt:
                l_index = input_prompt.index('언어')
                action = input_prompt[l_index+1]
                print(action)

                input_prompt.remove('언어')
                input_prompt.remove(action)


                self.LanguageCenter(action)


            if '수학' in input_prompt:
                l_index = input_prompt.index('수학')
                action = input_prompt[l_index+1]
                print(action)

                input_prompt.remove('수학')
                input_prompt.remove(action)
                self.MathCenter(action)

                

            if '의식' in input_prompt:
                l_index = input_prompt.index('의식')
                action = input_prompt[l_index+1]
                print(action)

                input_prompt.remove('의식')
                input_prompt.remove(action)
                
                self.Consciousness(action)
            if '시간' in input_prompt:

                l_index = input_prompt.index('시간')
                action = input_prompt[l_index+1]
                print(action)

                input_prompt.remove('시간')
                input_prompt.remove(action)
                self.TimeCenter(action)




            input_prompt.remove('능력개수')
            input_prompt.remove(input_prompt[-1])
            print(input_prompt)

                    
                #prompt를 대뇌에서 가져온 판단결과로 하자 그걸 이제 여기서 풀어서 해석하고 각각맞는 역할에 가는식으로하도록한다 

