import streamlit as st
import math
import pickle


with open("titanic_model.pkl",'rb') as f:
    titanic_model = pickle.load(f)

st.header("Titanic Survival Prediction !!!")
 
pclass_mapping = {
    "Premiere": 1,
    "Executive": 2,
    "Economy": 3
}

Sex_mapping = {
    "Male":0,"Female":1
}
Embarked_mapping = {
    "Cherbourg":1,
    "Queenstown":2,
    "Southampton":3
}

col1, col2, col3 = st.columns(3)

with col1:   
    Pclass = st.selectbox("Class(Premiere/Executive/Economy)", ["1", "2", "3"])
with col2:
    Sex = st.selectbox("Gender(Male/Female)",("0","1"))
with col3:
    Age = st.number_input("Age of Passenger")

col4, col5 = st.columns(2)

with col4:
    SibSp = st.number_input("Siblings/Spouses")
with col5:
    Parch = st.number_input("Parent/Children")
 
col6, col7 = st.columns(2)
with col6 :
    Fare = st.number_input("Fare of Journey")
with col7 :
    Embarked = st.selectbox("Picking Point(Cherbourg/Queenstown/Southampton)",("1","2","3"))

if st.button("Predict"):
    features = [[
        int(Pclass),      # user already picked 1 / 2 / 3
        int(Sex),         # 0 / 1
        math.ceil(Age),
        math.ceil(SibSp),
        math.ceil(Parch),
        Fare,             # keep as float
        int(Embarked)     # 1 / 2 / 3
    ]]

    result = titanic_model.predict(features)[0]
    output_labels = {
        1: "The passenger will Survive",
        0: "The passenger will NOT Survive"
    }
    st.markdown(f"## {output_labels[result]}")

