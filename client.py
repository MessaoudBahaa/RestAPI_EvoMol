import requests
import json


payload = {'id':2,'bits':'0100101110101'}

r = requests.post('http://127.0.0.1:5000/api/evaluate', json=payload)

print (r.text)