import streamlit as st
import joblib 
import sklearn 

mymodel = joblib.load('model.pkl')
st.title("Rain Fall Prediction")

a1=st.number_input("Enter Pressure")
a2=st.number_input("Dewpoint")
a3=st.number_input("Humidity")
a4=st.number_input("Cloud")
a5=st.number_input("Sunshine")
a6=st.number_input("Winddirection")
a7=st.number_input("Windspeed")

if st.button("predict"):
    op = mymodel.predict([[a1,a2,a3,a4,a5,a6,a7]])
    st.write("Rainfall is: ",op)
    