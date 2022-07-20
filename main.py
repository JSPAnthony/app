
import streamlit as st
import requests


st.title('HD_model')




def get_predictions(age, sex, chestpaintype, restingbp, cholesterol, fastingbs, restingecg, maxhr, exerciseangina, oldpeak,
            st_slope):
    # url = 'https://github.com/JSPAnthony/ads-final-project.git' \
        format(age=age, sex=sex, chestpaintype=chestpaintype, restingbp= restingbp, cholesterol=cholesterol, fastingbs=fastingbs, restingecg=restingecg, maxhr=maxhr, exerciseangina=exerciseangina, oldpeak=oldpeak, st_slope=st_slope)
response = requests.post(url)
json_response = response.json()
heartdisease=json_response['prediction']
'return' [heartdisease]





age = st.number_input('Enter patient age')
sex = st.selectbox('Enter patient sex', ('M', 'F'))
chestpaintype= st.selectbox('Enter Chest pain type', ('ATA', 'NAP', 'ASY', 'TA'))
restingbp = st.number_input('enter the resting BP')
cholesterol = st.number_input('enter patient cholesterol')
fastingbs = st.number_input('enter fastingbs')
restingecg= st.selectbox('resting ECG', ('Normal', 'ST', 'LVH'))
maxrh = st.number_input('maxhr')
exerciseangina = st.selectbox('exercise angina', ('N', 'Y'))
oldpeak = st.number_input('oldpeak')
st_slope = st.selectbox('st_slope', ('Up', 'Flat', 'Down'))





result = ""

# when 'Predict' is clicked, make the prediction and store it
if st.button("Predict"):
    result= get_predictions(age=age, sex=sex, chestpaintype=chestpaintype, restingbp= restingbp, cholesterol=cholesterol,
                fastingbs=fastingbs, restingecg=restingecg, maxhr=maxhr, exerciseangina=exerciseangina, oldpeak=oldpeak, st_slope=st_slope)
    st.success(f'HeartDisease  {result}')