import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")

st.header("house prediction")
sqrt=st.number_input("Enter squrefit")
Bed=st.number_input("Enter Bedrooms")
Ag=st.number_input("Enter Age")
distance=st.number_input("Distance to city")
btn=st.button("price!")
if btn:
    model=pickle.load(open("hpp.pkl","rb"))
    res=model.predict([[sqrt,Bed,Ag,distance]])[0]
    st.markdown(f"Expected price :{res}")