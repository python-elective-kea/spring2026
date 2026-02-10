from math import pi
import pandas as pd
import requests as rq
from dotenv import load_dotenv
import os
from pathlib import Path
import subprocess

load_dotenv()
x = os.getenv('API_KEY_') # classic token from Dev Settings in Settings in github
# print(x)

if not x:
    raise ValueError("API_KEY not found in environment variables")

head = {
    'Authorization' : f'token {x}' 
}

res = rq.get('https://api.github.com/repos/Socu22/ExamDay?', headers=head)
res.raise_for_status()  # Raise exception for bad status codes

output_path = Path(__file__).parent / 'pyresult.json'
with open(output_path, 'w') as f:
    f.write(res.text)


print(res.json)

