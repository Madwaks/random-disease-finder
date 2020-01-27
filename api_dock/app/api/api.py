from flask import Flask, request
from flask_restplus import Api, Resource
import json
import sys
sys.path.append('./app')

from back import finddisease

app = Flask(__name__)
api = Api(app=app, title='Diagnosis API', validate=True)

fd = finddisease.FindDisease()

@api.route("/find_disease/<string:list_symptoms>")
@api.doc(params={'list_symptoms': 'the list of symptoms as a string : "1234"'})
class DiseaseApi(Resource):
    def get(self, list_symptoms):
        l_s = [int(i)+1 for i in list_symptoms]
        diseases = fd.get_ids_names(l_s).to_json(orient='records')
        
        return {'disease' : json.loads(diseases)}

@api.route("/find_symptoms/")
class SymptomsApi(Resource):
    def get(self):
        

        return {"symptoms": fd.sympt_dict}

if __name__ == '__main__':
    app.run(port= 8887, host='0.0.0.0')