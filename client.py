import requests
import json


payload = {'id':2,'name':'bahaa'}

r = requests.post('http://127.0.0.1:5000/api/post/test', json=payload)

print (r.text)