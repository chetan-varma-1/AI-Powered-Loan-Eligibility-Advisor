import streamlit as st
import pickle
from chatbot import show_chatbot

#load the pre-trained model
model =pickle.load(open('model.pkl','rb'))

#streamlit layout for home page

def home_page():
    st.title("🚀Loan Prediction System")
    st.markdown("### **Welcome to the Loan Prediction System")
    st.markdown("""This tools helps you predict whether your loan application will be approved or rejected based on a variety of personal and financial factors. Fill in your details and let the system predict your loan status with an accurate machine learning model.""")

    #add an image to the loan page
    st.image("loan.png",caption="Loan Prediction System")
    st.markdown("###🕵️‍♀️ Project Overview")
    st.markdown("""
                This project was developed as part of my **AI Intership** at **Infosys Springboard**. The object was to build a **AI powered loan advisor system** that uses machine learning to predict whether a loan application  will be approved or rejected based on various parameters like personal and financial details of the applicant.
                This system takes the user's input and processes it through a pre-trained model to deliver a prediction about the loan status. We used alogrithms like ** Logistic regresstion** and **Random Forest** and **Decision Tress** for accurate predictions.
                """)
#streamlit Layout for about us page

def about_us_page():
    st.title("📋About Us")
    st.markdown("""**Our Mission**: We aim to provide **Innovative, effective, and easy_to_use** financial tools that 
                assist individuals in making better financial decisions. Our mission is to simplify 
                complex loan application process using advanced technoloy like **Machine learning** and **AI** """)
    st.markdown("""
                The **Loan perdiction System** architecture is designed to  seamlessly collect user inputs, process them through a machine learning model, and deliver accurate predictions for loan approval. Here's a breakdown of the system componets:
                
                1. **User Interface (UI): The front-end interfaces built using **Streamlit** allows users to input thei personal and financial information.
                2. **Data Preprocessing**: Data entered by users is cleaned and transformed into numerical values,ensuring compatibilit with the machine learning model.
                3. **Machine Learning Model**: The core of the system is a trained model(e.g., Random Forest, Logistic Regression), which predicts the likelihood of loan approval based on historical data.
                4. ** Prediction Engine**: The system runs the model on the preprocessed data and returns the loan approval decision..
                5. ** Visualization & Output**: The result is displayed to the user in a clear format with feedback on whether the loan is likely to be approved or rejected.
                
                Below is a diagram of the system architecture for better understanding:
                """)
    #Image of System Architecture
    st.image("system_architecture.png",caption="System Architecture Diagram")

    #Activity log section
    st.markdown("###📊Project Acivity Log")
    st.markdown(""""
                Throughout my intership, I engaged in various key activities to contribute to the ** Loan Prediction System ** project:
                
                
                1. ** Data Collection** : Gathered relavant data from past loan applicants, including financial history, loan amounts, and approval outcomes.
                2. ** Data Cleaning** :  Handled missing values, outliers, and transformed categorical data to ensure compatibility with machine learning alogrithms.
                3. ** Model Selection **: Experimennted with various machine learning algorithms such as ** Logistic Regression**, ** Random Forest**, and ** Decision Tree** to find the best-preforming model.
                4. ** Model Training & Optimization** : Trained the model on historical data, fine-tuned hyperparameters, and evaluted performance metrics like ** accuracy **, ** precision ** and ** recall **.
                5. ** Deployement & Testing**: Deployed the trained model into the Streamlit application, tested the prediction system with real user inputs,  and optimized its performance.
                
                This project has provided me with hands-on experience in ** data preprocessing **  , **model training** , and ** AI deployment** , which are essential skills for my AI professional.
                """ )
    #prokect acitivity image
    st.image("Project Acitivity.png",caption= "Project Activity Diagram")

#streamlit layout for Prediction page

def prediction_page():
    st.title("🚀Loan Adivisor System")
    st.markdown("### 📋Enter Loan Application Details to Predict Your Loan Status")\
    
    #user input fields for prediction
    gender = st.selectbox("👤Gender",["Male","Female"])
    married= st.selectbox("💍Marital Status",["Yes","No"])
    dependents= st.selectbox("👥 Dependents",["0","1","2","3+"])
    





    
