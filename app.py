import streamlit as st
import pickle
import numpy as np

# Custom CSS for background color
# Custom CSS for background color and heading color
st.markdown(
    """
    <style>
    body {
        background-color:white;
    }
    .stApp {
        background-color: #085187;
        padding: 20px;
        border-radius: 10px;
    }
    .stSidebar { 
        background-color: #085187; 
    }
    h1, h2, h3, h4, h5, h6 {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Parkinsons_model.sav', 'rb'))

# Sidebar for navigation
st.sidebar.title('🩺 Multiple Disease Prediction System')
selected = st.sidebar.selectbox('Select Disease to Predict', (
    'Diabetes Prediction',
    'Heart Disease Prediction',
    'Parkinsons Prediction'
))

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction')
    
    Pregnancies = st.number_input('🦰 Number of Pregnancies', key='pregnancies')
    Glucose = st.number_input('🍬 Glucose Level', key='glucose')
    BloodPressure = st.number_input('💉 Blood Pressure', key='blood_pressure')
    SkinThickness = st.number_input('📏 Skin Thickness', key='skin_thickness')
    Insulin = st.number_input('💉 Insulin Level', key='insulin')
    BMI = st.number_input('⚖️ BMI', format="%f", key='bmi')
    DiabetesPedigreeFunction = st.number_input('📊 Diabetes Pedigree Function', format="%f", key='dpf')
    Age = st.number_input('🎂 Age', key='age')

    if st.button('🔍 Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_prediction[0] == 1:
            st.error('🚨 The person is diabetic')
        else:
            st.success('✅ The person is not diabetic')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction')
    
    age = st.number_input('🎂 Age', key='heart_age')
    sex = st.number_input('⚧️ Sex (1 = Male, 0 = Female)', key='heart_sex')
    cp = st.number_input('💔 Chest Pain Type (0-3)', key='chest_pain')
    trestbps = st.number_input('💉 Resting Blood Pressure', key='rest_bp')
    chol = st.number_input('🩸 Serum Cholesterol (mg/dl)', key='cholesterol')
    fbs = st.number_input('🍬 Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)', key='fbs')
    restecg = st.number_input('📈 Resting Electrocardiographic Results (0-2)', key='rest_ecg')
    thalach = st.number_input('🏃 Maximum Heart Rate Achieved', key='thalach')
    exang = st.number_input('🚴 Exercise Induced Angina (1 = Yes; 0 = No)', key='exang')
    oldpeak = st.number_input('📉 ST Depression Induced by Exercise', format="%f", key='oldpeak')
    slope = st.number_input('📈 Slope of the Peak Exercise ST Segment (0-2)', key='slope')
    ca = st.number_input('🩺 Number of Major Vessels Colored by Fluoroscopy (0-3)', key='ca')
    thal = st.number_input('🧬 Thalassemia (1 = Normal; 2 = Fixed Defect; 3 = Reversible Defect)', key='thal')

    if st.button('🔍 Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_disease_prediction[0] == 1:
            st.error('🚨 The person has heart disease')
        else:
            st.success('✅ The person does not have heart disease')

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("🧠 Parkinson's Disease Prediction")

    fo = st.number_input('🎜 MDVP:Fo(Hz)', format="%f", key='fo')
    fhi = st.number_input('🎵 MDVP:Fhi(Hz)', format="%f", key='fhi')
    flo = st.number_input('🎶 MDVP:Flo(Hz)', format="%f", key='flo')
    jitter_percent = st.number_input('📉 MDVP:Jitter(%)', format="%f", key='jitter')
    jitter_abs = st.number_input('📏 MDVP:Jitter(Abs)', format="%f", key='jitter_abs')
    rap = st.number_input('📊 MDVP:RAP', format="%f", key='rap')
    ppq = st.number_input('📈 MDVP:PPQ', format="%f", key='ppq')
    ddp = st.number_input('🔢 Jitter:DDP', format="%f", key='ddp')
    shimmer = st.number_input('✨ MDVP:Shimmer', format="%f", key='shimmer')
    shimmer_db = st.number_input('🔊 MDVP:Shimmer(dB)', format="%f", key='shimmer_db')
    apq3 = st.number_input('📉 Shimmer:APQ3', format="%f", key='apq3')
    apq5 = st.number_input('📊 Shimmer:APQ5', format="%f", key='apq5')
    apq = st.number_input('📈 MDVP:APQ', format="%f", key='apq')
    dda = st.number_input('🔢 Shimmer:DDA', format="%f", key='dda')
    nhr = st.number_input('📉 NHR', format="%f", key='nhr')
    hnr = st.number_input('🔊 HNR', format="%f", key='hnr')
    rpde = st.number_input('📈 RPDE', format="%f", key='rpde')
    dfa = st.number_input('📊 DFA', format="%f", key='dfa')
    spread1 = st.number_input('📏 Spread1', format="%f", key='spread1')
    spread2 = st.number_input('📏 Spread2', format="%f", key='spread2')
    d2 = st.number_input('🔢 D2', format="%f", key='d2')
    ppe = st.number_input('📈 PPE', format="%f", key='ppe')

    if st.button("🔍 Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        if parkinsons_prediction[0] == 1:
            st.error("🚨 The person has Parkinson's disease")
        else:
            st.success("✅ The person does not have Parkinson's disease")
