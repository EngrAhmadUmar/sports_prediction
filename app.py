import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


# loading the trained model
model = pickle.load(open('PickleModel.pkl','rb'))


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:#002E6D;padding:20px;font-weight:15px"> 
    <h1 style ="color:white;text-align:center;"> Sport Prediction</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    default_value_goes_here = ""
    ball_control = st.number_input("Please enter the players Ball Control Attribute", 0, 100000000, 0)
    short_passing = st.number_input("Please enter the players Short Passing Attribute", 0, 100000000, 0)
    dribbling = st.number_input("Please enter the players Dribbling Attribute", 0, 100000000, 0)
    crossing = st.number_input("Please enter the players Crossing Attribute", 0, 100000000, 0)
    curve = st.number_input("Please enter the players Curve Attribute", 0, 100000000, 0)

    attributes = [ball_control, short_passing, dribbling, crossing, curve]

    result = ""

    #Display Results
    if st.button("Predict"):
      scaler = StandardScaler()
      scaler.fit([attributes])
      featureshost = scaler.transform([attributes])
      prediction = model.predict(featureshost)

      result = prediction
      st.write(result)


if _name_ == '_main_':
    main()
