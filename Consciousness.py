
from openai import OpenAI # OpenAI official Python package
from listToString import listToString
def consciousness():
    f = open('recognize_con.txt','r',encoding='utf-8')
    f2 = listToString(f.readlines())
    a,b,c,d = f2.split('\n')
    client = OpenAI(
            api_key="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")
    '''a = 'put the trash'
    b = 'situation that is put the trash'
    c = 'ended'''
    #input_text = input()
    gpt_prompt = [{"role": "system", "content": f'''You are conscious. You are aware of the actions you are doing and are responsible for recognizing your words and emotions. You judge and recognize what you are doing, where you are, what emotions you are feeling, and what situation you are in. must play a role
                You're acting, you're talking, you're in a situation
                What you will print

                I am now in a "situation", and I am "acting" according to the situation. also I am saying "speak" and I am feeling 'emotion'
                    It must be in exactly the format of the output example. 어법이나 문법상으로 문제없는 한문장이 되게하여야만한다 
                "action" : {a}
                "situation" : {b}
                "speak" : {c}
                "emotion" : {d} 
                
                '''}
                
                    ]#,{"role": "system", "content": f'''{input_text}'''}


    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=gpt_prompt,

    )

    input_prompt = response.choices[0].message.content
    print(input_prompt)#자기가 무슨일을 하는지 인식하는것 그것이야말로 의식이라 정의하기로하였다

def conscious_opinion(content):
    #현재인식된값들을 바탕으로 의식적으로 의견을 낸다 
    f = open('recognize_con.txt','r',encoding='utf-8')
    f2 = listToString(f.readlines())
    a,b,c,d = f2.split('\n')
    client = OpenAI(
            api_key="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")
    '''a = 'put the trash'
    b = 'situation that is put the trash'
    c = 'ended'''
    #input_text = input()
    gpt_prompt = [{"role": "system", "content": f'''You are conscious. You are aware of the actions you are doing and are responsible for recognizing your words and emotions. You judge and recognize what you are doing, where you are, what emotions you are feeling, and what situation you are in. must play a role
                You're acting, you're talking, you're in a situation
                What you will print

                I am now in a "situation", and I am "acting" according to the situation. also I am saying "speak" and I am feeling 'emotion'
                    It must be in exactly the format of the output example. 어법이나 문법상으로 문제없는 한문장이 되게하여야만한다 또한 {content}에 대한 의견을 내줘
                "action" : {a}
                "situation" : {b}
                "speak" : {c}
                "emotion" : {d} 
                
                출력예시 : 
                위 판단들을 바탕으로 {content}에 대한 의견을 내줘(답변을 해줘)
                
                '''}
                
                    ]#,{"role": "system", "content": f'''{input_text}'''}


    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=gpt_prompt,

    )

    input_prompt = response.choices[0].message.content
    print(input_prompt)#자기가 무슨일을 하는지 인식하는것 그것이야말로 의식이라 정의하기로하였다

    return input_prompt

'''
a,b,c,d = input().split(',')
consciousness(a,b,c,d)
'''