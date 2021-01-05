import requests
import json
import asyncio
import aiohttp




def background(f):
    from functools import wraps
    @wraps(f)
    def wrapped(*args, **kwargs):
        loop = asyncio.get_event_loop()
        if callable(f):
            return loop.run_in_executor(None, f, *args, **kwargs)
        else:
            raise TypeError('Task must be a callable')    
    return wrapped


@background
def evaluate(individu): 
    r = requests.post('http://127.0.0.1:5000/evaluation', json=individu)



payload = {'id':8,'bits':'1100011100101101'}
evaluate(payload)

print ('I dont wait !')
"""








r = requests.get('http://127.0.0.1:5000/evaluation/3',{'status':'FINISHED'})
print (r.text)
"""
#r = requests.post('http://127.0.0.1:5000/api/evaluate/status', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/esttermine', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/estsucces', json=payload)
#r = requests.post('http://127.0.0.1:5000/api/evaluate/output', json=payload)



