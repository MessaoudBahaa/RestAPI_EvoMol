
import json
import time
import random
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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

# retourner si une evaluation d'un individu etait un succés
@app.route('/api/evaluate/estsucces', methods =['POST'])
def api_est_succes():
    req_data = request.get_json()
    filename = str(req_data['id'])+'.tmp'
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    read_file.close()
    return jsonify((data["execution"]["output"]["result"]=="SUCCESS"))

# retourner les resultats d'un evaluation d'un individu
@app.route('/api/evaluate/output', methods =['POST'])
def api_get_evaluation_data():
    req_data = request.get_json()
    filename = str(req_data['id'])+'.tmp'
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    read_file.close()
    return jsonify((data["execution"]["output"])

# execution: RUNNING / TERMINATED 
# output status: ERROR / SUCCESS and results  

