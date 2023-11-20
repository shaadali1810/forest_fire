import pickle
from flask import  Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

rideg_model=pickle.load(open('model/ridge.pkl','rb'))
standard_scaler=pickle.load(open('model/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        new_data_scaled=standard_scaler.tranform([Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region])
        result = rideg_model.predict(new_data_scaled)
        
        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')
    




if __name__=="__main__":
        app.run(host="0.0.0.0")
