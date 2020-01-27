from flask import Flask, jsonify, render_template, request
import os

import requests
import json

API_HOST = os.environ.get('API_HOST', '0.0.0.0')

API_PATH = 'http://{}:8887/'.format(API_HOST)

app = Flask(__name__)

@app.route('/')
def main():
    try:
        resp = requests.get(API_PATH+'find_symptoms')
        dict_sympt = json.loads(resp.content)
    except Exception as e:
        raise(e)

    return render_template("index.html", data_sympt=dict_sympt['symptoms'], titre='DISEASE')

@app.route('/find-diseases', methods=['POST'])
def get_data():
    if request.method == 'POST':
        selected_ = request.form.getlist("symptoms")

        #Generates code to request API
        code_symp = ''
        for i in selected_:
            code_symp = code_symp + str(int(i)-1)
            
        try:
            resp = requests.get(API_PATH+'find_disease/'+code_symp)
            return json.loads(resp.content)
        except Exception as e:
            raise(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')