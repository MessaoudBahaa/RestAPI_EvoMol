from pymongo import MongoClient

MongoDbUri = 'mongodb://127.0.0.1:27017'

class DataLayer:
     
    def __init__(self):
        self.client = MongoClient (MongoDbUri)
        self.db = self.client.evomoldb
        

    def addMolecule(self, id, bits,status,result,output):
        #ajouter
        molecule = {
            'id' : id ,
            'bits' : bits,
            'status' : status,
            'result' : result,
            'output' : output
        }

        self.db.molecules.insert_one(molecule)
        

    def getMolecule(self):
        #retourner execution
        return 0

    def updateMolecule(self,id,status,result,output):
        
    
        self.db.molecules.update_one({'id': id}, { '$set' : {'status':status, 'result' : result, 'output' : output} })
        #mettre a jour l'exuction
        return 0