import requests
import json


payload = {'id':2,'bits':'0100101110101'}

r = requests.post('http://127.0.0.1:5000/api/evaluate', json=payload)
print (r.text)
r = requests.get('http://127.0.0.1:5000/api/evaluate/status',{'id':2})
print (r.text)

#r = requests.post('http://127.0.0.1:5000/api/evaluate/status', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/esttermine', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/estsucces', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/output', json=payload)



