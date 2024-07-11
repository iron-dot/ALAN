import requests
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
#os.environ['CURL_CA_BUNDLE'] = ''

def calculation(prompt):
    tokenizer = AutoTokenizer.from_pretrained("internlm/internlm2-math-7b",cache_dir='C:/Users/', trust_remote_code=True)
    # Set `torch_dtype=torch.float16` to load model in float16, otherwise it will be loaded as float32 and might cause OOM Error.
    model = AutoModelForCausalLM.from_pretrained("internlm/internlm2-math-7b", cache_dir='C:/Users/',trust_remote_code=True, torch_dtype=torch.float16).cuda()
    model = model.eval()
    prompt_math = prompt
    response, history = model.chat(tokenizer, prompt_math, history=[], meta_instruction="")
    print(response)
#calculation('a+b=10 a=2, b=?')