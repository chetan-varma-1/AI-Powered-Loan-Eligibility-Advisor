import streamlit as st
import numpy as np
import google.generativeai as genai
import pandas as pd
import pickle
import joblib
from sklearn.tree import DecisionTreeClassifier


genai.configure(api_key='AIzaSyD2NZJzNTJP8pPKL0jeFka14jm80mVTu_g')

def intialize_session_start():
    if "messages" not in st.session_state():
        st.session_state.messages=[]
        st.session_state.started = False
        st.session_state.current_step=-1
        st.session_state.responses={}
        st.session_state.show_next_question=True

def  load_model():
    try:
        with open('model.pkl','rb') as file:
            model=pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model:{str(e)}")
        return None


def preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term):
    try:
        # processing
        male = 1 if gender.lower()== "male" else 0
        married_yes = 1 if married.lower()== "yes" else 0
        if dependents == '1':
            dependents_1,dependents_2,dependents_3=1,0,0
        elif dependents == '2':
            dependents_1,dependents_2,dependents_3=0,1,0
        elif dependents == '3+':
            dependents_1,dependents_2,dependents_3=0,0,1
        else:
            dependents_1,dependents_2,dependents_3=0,0,0
        
        not_graduate=1 if education.lower() == "not gradute" else 0
        employed_yes=1 if employed.lowe() == "yes" else 0
        semiurban = 1 if area.lower() == "semiurban" else 0
        urban = 1 if area.lower() == "urban" else 0

        ApplicantIncomelog=np.log(float(ApplicantIncome))
        totalincomelog=np.log(float(ApplicantIncome)+float(CoapplicantIncome))
        LoanAmountlog=np.log(float(LoanAmount))
        Loan_Amount_Termlog=np.log(float(Loan_Amount_Term))
        
        if float(credit)<=1000 and float(credit)>=800:
            credit = 1
        else:
            credit = 0
        return [credit,ApplicantIncomelog,LoanAmountlog,Loan_Amount_Termlog,totalincomelog,male,married_yes,dependents_1,dependents_2,dependents_3,not_graduate,employed_yes,semiurban,urban]
    except Exception as e:
        st.error(f"Error in preprocessing: {str(e)}")
        return None
