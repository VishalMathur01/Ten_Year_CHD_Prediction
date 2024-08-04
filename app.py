import streamlit as st
import pandas as pd
import joblib

model = joblib.load('rfc.joblib')

st.title("Test whether you are at risk of getting heart disease in the next 10 years 😮")
st.divider()

age = st.slider("Enter your Age🧓👶", 0, 100, value=64)
education = st.select_slider("Enter your education (1: School, 2: Under Graduate, 3: Post Graduate, 4: PhD) 📚", [1.0, 2.0, 3.0, 4.0], value=2.0)
cigsPerDay = st.slider("Cigarettes smoked per day 🚬", 0, 70, value=3)
BPMeds = st.select_slider("Was Taking Medication for Blood Pressure 💊", [0.0, 1.0], value=0.0)
prevalentStroke = st.select_slider("Whether or not You had previously had a stroke 🫀", [0, 1], value=0)
prevalentHyp = st.select_slider("Whether or not You were hypertensive", [0, 1], value=0)
diabetes = st.select_slider("Whether or not You had diabetes 🍬", [0, 1], value=0)
totChol = st.slider("Cholesterol levels", 107.0, 696.0, value=221.0)
sysBP = st.slider("Systolic blood pressure", 0.0, 300.0, value=148.0)
diaBP = st.slider("Diastolic blood pressure", 0.0, 300.0, value=85.0)
BmI = st.slider("BMI [Weight/ Height]", 0.0, 100.0, value=29.77)
heartRate = st.slider("Heartrate ", 0.0, 200.0, value=90.0)
glucose = st.slider("Glucose", 40.0, 500.0, value=80.0)
sex = st.selectbox("Sex [Yes there are only two Genders]🚹🚺", ["M", "F"], index=1)
is_smoking = st.selectbox("Have you smoked 🚬", ['YES', 'NO'], index=0)

def predict():
    sample_data = pd.DataFrame([{
        'age': int(age), 
        'education': float(education),
        'sex': str(sex),
        'is_smoking': str(is_smoking),
        'cigsPerDay': float(cigsPerDay), 
        'BPMeds': float(BPMeds),
        'prevalentStroke': int(prevalentStroke),
        'prevalentHyp': int(prevalentHyp),
        'diabetes': int(diabetes), 
        'totChol': float(totChol),
        'sysBP': float(sysBP),
        'diaBP': float(diaBP),
        'BMI': float(BmI),
        'heartRate': float(heartRate),
        'glucose': float(glucose)
    }])
    
   
    sample_data = sample_data[['age', 'education', 'sex', 'is_smoking', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']]
    
    
    predictions = model.predict(sample_data)
    if predictions[0] == 0:
        st.balloons()
        st.success("Congratulation!!! You are free from risks of having CHD in Ten Years 🎉🎊🥳")
    else:
        st.error("Be Careful!!! You are at risk of having CHD in Ten Years ⚠️😔😔")

trigger = st.button("Predict 🪄", on_click=predict)
