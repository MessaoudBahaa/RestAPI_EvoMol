
import json
import time
import random
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# Post pour calculer fitness de l'individu (somme des uns)
@app.route('/api/evaluate', methods =['POST'])
def api_evaluate():

    req_data = request.get_json()

    # initialiser le dictionnaire contenant l'état d'execution
    data = {
    "execution": {
        "status": "RUNNING",
        "output": { "result":"ERROR",
                    "data":{}
        }
    }
    }

    # initialiser la variable contenant le score
    sum = 0 
    print ('calculating score ...')


    # preparer le nom du fichier temporaire
    filename = str(req_data['id'])+'.tmp'
    # initialiser le fichier
    with open(filename, "w") as write_file:
        json.dump(data, write_file)
    write_file.close()

    # Simuler le calcule de l'evaluation de l'individu avec une probabilité d'erreur de 20%
    time.sleep(10)
    if (random.random()<0.8):
        for x in (tuple (req_data['bits'])):
            sum = sum + int(x)
        output = {  "result": "SUCCESS",
                "data": { "id": req_data['id'], 
                            "bits": req_data['bits'], 
                            "score": sum}}
        data["execution"]["output"]=output
    else:
        output = { "result":"ERROR",
                    "data":{}
        }

    # mettre a jour l'etat d'execution et les resultats
    data["execution"]["status"]="TERMINATED"
    data["execution"]["output"]=output

    # ecrire les resultats dans le fichier
    with open(filename, "w") as write_file:
        json.dump(data, write_file)

    print ('TERMINATED')
    write_file.close()
    return jsonify(sum)

# retourner l'etat d'execution d'individu
@app.route('/api/evaluate/status', methods =['POST'])
def api_status():
    req_data = request.get_json()
    filename = str(req_data['id'])+'.tmp'
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    read_file.close()
    return jsonify(data)

# retourner si une evaluation d'un individu est terminé
@app.route('/api/evaluate/esttermine', methods =['POST'])
def api_est_termine():
    req_data = request.get_json()
    filename = str(req_data['id'])+'.tmp'
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    read_file.close()

    return jsonify((data["execution"]["status"]=="TERMINATED"))


# execution: RUNNING / TERMINATED 
# output status: ERROR / SUCCESS and results  

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()