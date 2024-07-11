import time
import urllib
from openai import OpenAI
import cv2

def text_image(text):
    
    client = OpenAI(
                api_key="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")


    response = client.images.generate(
    model="dall-e-3",
    prompt=text,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url



    




    # 다운받을 이미지 url
    url = image_url

    # time check
    start = time.time()

    # 이미지 요청 및 다운로드
    urllib.request.urlretrieve(url, "test.jpg")

    # 이미지 다운로드 시간 체크
    print(time.time() - start)

    # 저장 된 이미지 확인


    image = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED)

    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

text_image('white cat') 
#이미지 생성 구현 끝
#https://platform.openai.com/docs/guides/images/language-specific-tips?context=node 이거 이용할수있는 만큼 이용해서 여러 기능 인페이팅같은 편집기술까지 여러 기능 가능한 많이 다 구현하기
