from diffusers import TextToVideoZeroPipeline
import imageio
import torch

import requests
import os
os.environ['CURL_CA_BUNDLE'] = ''

def text_video(prompt):

    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
    result = pipe(prompt=prompt).images
    result = [(r * 255).astype("uint8") for r in result]
    imageio.mimsave("video.mp4", result, fps=1)

    mp4 = 'video.mp4'
    return mp4

#text_video('a human is working the road')
#성능 앞으로 늘리거나 더좋은거 다운받아서 사용하기 또는 스스로 개선능력에 추가하기