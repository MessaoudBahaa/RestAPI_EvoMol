import requests
import json


payload = {'id':2,'data':'0100101110101'}

r = requests.post('http://127.0.0.1:5000/api/post/efaluate', json=payload)

print (r.text)