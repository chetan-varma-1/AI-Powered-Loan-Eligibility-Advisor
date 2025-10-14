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