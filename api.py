
import json
import time
import random
import flask
from flask import request, jsonify
from datalayer import DataLayer


app = flask.Flask(__name__)
app.config["DEBUG"] = True


DL=DataLayer()



@app.route('/', methods=['GET'])
def home():
    return '''<h1>API for calculating fitness</h1>'''


# Post pour calculer fitness de l'individu (somme des uns)
@app.route('/api/evaluate', methods =['POST'])
def api_evaluate():

    req_data = request.get_json()
    id = req_data['id']
    bits = req_data['bits']
    


    DL.addMolecule(id,bits,'RUNNING','',{})



    # initialiser la variable contenant le score
    sum = 0 
    print ('calculating score ...')
    
    # Simuler le calcule de l'evaluation de l'individu avec une probabilité d'erreur de 20%
    time.sleep(10)
    if (random.random()<0.8):
        for x in (tuple (bits)):
            sum = sum + int(x)

        DL.updateMolecule(id,'FINISHED','SUCCESS',{'score' : sum})
      
    else:
        DL.updateMolecule(id,'FINISHED','ERROR',{})
       

    print ('FINISHED')
 
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
    return jsonify((data["execution"]["output"]))

# execution: RUNNING / TERMINATED 
# output status: ERROR / SUCCESS and results  


# api avec 
# changer aux gets
# documentation de l'api 
# Modulaire (decoupler l'acces aux données) (DAO DTO)


app.run()