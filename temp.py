# -*- coding: utf-8 -*-
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open(r"C:\Users\ASUS\Desktop\chs main project\diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open(r"C:\Users\ASUS\Desktop\chs main project\heart_disease_model.sav", "rb"))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (Range: 0 - 17)')

    with col2:
        Glucose = st.text_input('Glucose Level (Range: 50-199)')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value (Range: 60-122)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value (Range: 50-99)')

    with col2:
        Insulin = st.text_input('Insulin Level (Range: 100-848)')

    with col3:
        BMI = st.text_input('BMI value (Range: 16-67.1)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (Range: 0.078-2.42)')

    with col2:
        Age = st.text_input('Age of the Person (Range: 21-81)')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (Range: 29-77)')

    with col2:
        sex = st.text_input('Sex (Range: 0-1)')

    with col3:
        cp = st.text_input('Chest Pain types (Range: 0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Range: 94-200)')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl (Range: 130-560)')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (Range: 0-1)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (Range: 0-2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (Range: 71-202)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (Range: 0-1)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (Range: 0-6.2)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (Range: 0-2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (Range: 0-4)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (Range: 0-3)')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
