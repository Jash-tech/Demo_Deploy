# 1. Library imports
import uvicorn
from fastapi import FastAPI
from banknote import BankNotes
import pandas as pd
import numpy as np
import pickle


# 2. Create the app object
app=FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return "Wecome to BankNote Prediction Model"

@app.post('/predict')
def predict_banknote(data:BankNotes):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    # return {"Prediction": prediction , "datas": data}
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
