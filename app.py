# # 1. Library imports
# import uvicorn
# from fastapi import FastAPI
# from banknote import BankNotes
# import pandas as pd
# import numpy as np
# import pickle


# # 2. Create the app object
# app=FastAPI()
# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

# # 3. Index route, opens automatically on http://127.0.0.1:8000
# @app.get('/')
# def index():
#     return "Wecome to BankNote Prediction Model"

# @app.post('/predict')
# def predict_banknote(data:BankNotes):
#     data=data.dict()
#     variance=data['variance']
#     skewness=data['skewness']
#     curtosis=data['curtosis']
#     entropy=data['entropy']
#     prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
#     # return {"Prediction": prediction , "datas": data}
#     if(prediction[0]>0.5):
#         prediction="Fake note"
#     else:
#         prediction="Its a Bank note"
#     return {
#         'prediction': prediction
#     }

# # 5. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8000
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)

# 1. Import Libraries
import streamlit as st
import pickle
from banknote import BankNotes
import pandas as pd
import numpy as np
import pickle


# 2. Load the trained model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Create Streamlit Web App
st.title("🏦 BankNote Authentication App")
st.write("Upload the required values to check whether a banknote is **real** or **fake**.")

# 4. Take user input
variance = st.number_input("Variance", value=0.0, step=0.1)
skewness = st.number_input("Skewness", value=0.0, step=0.1)
curtosis = st.number_input("Curtosis", value=0.0, step=0.1)
entropy = st.number_input("Entropy", value=0.0, step=0.1)

# 5. Predict on button click
if st.button("Predict"):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    
    if prediction[0] > 0.5:
        st.error("🚨 Fake Note Detected!")
    else:
        st.success("✅ It's a Real Bank Note!")

# 6. Run with: `streamlit run app.py`