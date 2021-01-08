
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
    return '''<h1>API for molecules evaluation</h1>'''


# Post pour calculer fitness de l'individu (somme des uns)
@app.route('/evaluation', methods =['POST'])
def molecule_evaluation():

    req_data = request.get_json()
    id = req_data['id']
    bits = req_data['bits']
    
    DL.addMolecule(id,bits,'RUNNING','',{})

    # initialiser la variable contenant le score
    sum = 0 
    print ('calculating score ...')
    
    # Simuler le calcule de l'evaluation de l'individu avec une probabilité d'erreur de 20%
    time.sleep(15)
    if (random.random()<0.8):
        for x in (tuple (bits)):
            sum = sum + int(x)

        DL.updateMolecule(id,'FINISHED','SUCCESS',{'score' : sum})
    else:
        DL.updateMolecule(id,'FINISHED','ERROR',{})


    return jsonify(sum)

# retourner l'etat d'execution d'individu
@app.route('/evaluation/<id>/<field>', methods =['GET'])
def molecule_fields(id,field):
    molecule = DL.getMolecule(int(id))
    
    if (molecule is None) : 
        return "molecule not found"
    elif (field in ("status","output","result")) : 
        return molecule[field]
    else :
        return "not valid field"

# retourner si une evaluation d'un individu est terminé
@app.route('/evaluation/<id>', methods =['GET'])
def molecule_status(id):
    molecule = DL.getMolecule(int(id))

    if ('status' in request.args ) :
        status = request.args['status']
    else:
        if (molecule is None) : 
            return "molecule not found"
        else :
            return molecule

    
    if (molecule is None) : 
        return "molecule not found"
    else :
        return jsonify(molecule["status"]==status)






app.run()