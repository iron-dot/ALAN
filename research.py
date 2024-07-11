#research : 탐구 주제를 무작위로 계속 생성하고 탐구활동을 실제로 수행하는 모델
from openai import OpenAI # OpenAI official Python package
#자유 활동 및 성장 모델 (모듈, 기관)

client = OpenAI(api_key="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")

GP_dict = dict()
GP_dict["role"] = "assistant"
GP_dict["content"] = """
Learn based on these questions and create new questions related to those inquiry questions. They should not be duplicated, but should be related and similar, but create new questions that are slightly different.

{
"question": "How did the planets in our solar system form?",
"topic": "Space and celestial bodies",
"description": "Explores the theory of planet formation in the solar system.",
"related_research": ["Solar System Formation Theory", "Astrophysics"]
},

You must add , (comma) and do not add a comma only to the last data.

Based on the examples above, create and output the research questions in the form of a data set, just by changing the content in the same format."""

gpt_prompt = [GP_dict]

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=gpt_prompt
)

random_question = response.choices[0].message.content
print(random_question)


f = open('dataset/research.json','a',encoding='utf-8')
f.write('\n')
f.write(random_question)

f = open('dataset/research.json','r',encoding='utf-8')
fC = f.readlines()
f2 = ''.join(fC).strip()


client = OpenAI(
    api_key="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"
)
while True:
    gpt_prompt = [{"role": "assistant","content": f"""Select one by one from {f2} and print (exploration questions)"""}]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=gpt_prompt,
    )

    input_prompt = response.choices[0].message.content
    print(input_prompt)
    f = open('dataset/research.txt','r',encoding='utf-8')
    fC = f.readlines()
    fS = ''.join(fC).strip()


    if not input_prompt in fS:
        f = open('dataset/research.txt','a', encoding='utf-8')
        f.write(input_prompt)
        continue
       



    with open("dataset/research.txt", "r",encoding='utf-8') as file:
        n_lines = 0  # 줄 수를 저장할 변수
        # 파일 끝(EOF)에 도달할 때까지 문자열을 하나씩 읽기
        for line in file:
            n_lines += 1  # 줄 수 증가
        print(n_lines)# 줄 수 출력


    
    for x in range(n_lines):
        f = open('dataset/research.txt','r',encoding='utf-8')
        fC = f.readline()
        print(fC)#탐구 질문 1번부터 ~
        #탐구 질문 fC 를 기반으로 탐구활동을 개시한다
        #그후 다음 질문 탐구활동을 위해 위 for문으로 돌아간다
        



