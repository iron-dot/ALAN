from openai import OpenAI # OpenAI official Python package
from listToString import listToString
client = OpenAI(api_key="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")

def language(prompt):#(tasks)
        

        
        #대화 기능
        #content = tasks[0]["Language organ command delivery"]["command content"]
        gpt_prompt = [{"role": "assistant","content": f"""{prompt}"""}]

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=gpt_prompt,
    
        )
        print(response.choices[0].message.content)
        input_prompt = response.choices[0].message.content
        print(input_prompt)
        f = open('language.txt','a',encoding='utf-8')
        f.write(str(input_prompt))
        
        




#연결기관을 통해 의식과 인격생각체에게 언어적으로 할말을 명령받고 그대로 전하는역할만 한다

