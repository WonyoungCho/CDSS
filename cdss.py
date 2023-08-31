import pandas as pd
import streamlit as st

import os

#st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 500px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

footerText = """
<style>
#MainMenu {
visibility:hidden ;
}

footer {
visibility : hidden ;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>

<div class='footer'>
<p> Copyright @ 2023 by Wonyoung Cho, Contact <a href="mailto:wycho@oncosoft.io"> wycho@oncosoft.io </a></p>
</div>
"""

st.markdown(footerText, unsafe_allow_html=True)

def set_bmi(bmi):
    x = 4
    if   bmi <  18.5           : x = 1
    elif bmi >= 18.5 and bmi < 23: x = 2
    elif bmi >= 23   and bmi < 25: x = 3
    elif bmi >= 25             : x = 4

    return x

def right():
    cols = st.columns([1,2])
    with cols[0]:
        st.info('Age')
    with cols[1]:
        age = st.radio('Age', ['10s','20s','30s','40s','50s','60s','70s','80s','90s'], horizontal=True, label_visibility='collapsed')
    cols = st.columns([1,2])
    with cols[0]:
        st.success('Sex')
    with cols[1]:
        sex = st.radio('Sex', ['Male', 'Female'], horizontal=True, label_visibility='collapsed')

    cols = st.columns(3)
    with cols[1]:
        st.write('Weight (kg)')
    with cols[2]:
        st.write('Height (cm)')

        
    cols = st.columns(3)
    with cols[1]:
        weight = st.number_input('Weight (kg)',value=70, label_visibility='collapsed')
    with cols[2]:
        height = st.number_input('Height (cm)',value=170, label_visibility='collapsed')
    with cols[0]:
        bmi = weight/((height/100)**2)
        bmiGroup = set_bmi(bmi)
        bmiDict = {1:'Underweight',2:'Normal',3:'Overweight',4:'Obesity'}
        st.info('BMI'+os.linesep+f'({bmiDict[bmiGroup]})')

    cols = st.columns([1,2])
    with cols[0]:
        st.success('Region of regidence')
    with cols[1]:
        region  = st.radio('Region of regidence', ('Urban','Rural'), horizontal=True, label_visibility='collapsed')
    regionDict = {'Urban':1,'Rural':2}

    cols = st.columns([1,2])
    with cols[0]:
        st.info('Household income')
    with cols[1]:
        income   = st.radio('Household income',('1Q (Lowest)','2Q','3Q','4Q (Highest)'), horizontal=True, label_visibility='collapsed')
    incomeDict = {'1Q (Lowest)':1,'2Q':2,'3Q':3,'4Q (Highest)':4}

    cols = st.columns([1,2])
    with cols[0]:
        st.success('Smoking status')
    with cols[1]:
        smoke   = st.radio('Smoking status within 1-year', ('No','Yes'), horizontal=True, label_visibility='collapsed')

    cols = st.columns([1,2])
    with cols[0]:
        st.info('Acohol / week')
    with cols[1]:
        alcohol = st.radio('Acohol consumption per week', ('0','1','2-3','4-5','6-7'), horizontal=True, label_visibility='collapsed')

    cols = st.columns([1,2])
    with cols[0]:
        st.success('Eating meat / week')
    with cols[1]:
        eatMeat = st.radio('Eating meat per week', ('0','1','2-3','4-5','6-7'), horizontal=True, label_visibility='collapsed')

    cols = st.columns(3)
    with cols[1]:
        st.write('Days per week')#' (e.g. shopping, walking, housework)')
    with cols[2]:
        st.write('Hours per day')
        
    cols = st.columns(3)
    with cols[0]:
        st.info('Light physical activity')#' (e.g. shopping, walking, housework)')
    with cols[1]:
        lightDay = st.number_input('Days per week', min_value=0, max_value=7, value=1, label_visibility='collapsed')
    with cols[2]:
        lightMin = st.number_input('Hours per day', min_value=0, max_value=7, value=1, label_visibility='collapsed')

    cols = st.columns(3)
    with cols[0]:
        st.success('Moderate physical activity')#' (e.g. sweeping the floor, walking briskly, slow dancing, vacuuming)')
    with cols[1]:
        moderateDay = st.number_input('Days per week ', min_value=0, max_value=7, value=1, label_visibility='collapsed')
    with cols[2]:
        moderateMin = st.number_input('Hours per day ', min_value=0, max_value=7, value=1, label_visibility='collapsed')


    cols = st.columns(3)
    with cols[0]:
        st.info('Vigorous physical activity')#' (e.g. swimming, shoveling, soccer, jumping rope, carrying heavy loads)')
    with cols[1]:
        vigorousDay = st.number_input('Days per week  ', min_value=0, max_value=7, value=1, label_visibility='collapsed')
    with cols[2]:
        vigorousMin = st.number_input('Hours per day  ', min_value=0, max_value=7, value=1, label_visibility='collapsed')

    return

def main():
    right()

    result1 = 0.6423
    result2 = 0.3476
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: red;'>CDSS</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: red;'>(Clinical Decision Support System)</h1>", unsafe_allow_html=True)
        st.markdown(f'# Probability of adverse event after treatments')
        st.markdown(f'# - Dermatitis: {result1*100:.2f} %')
        st.markdown(f'# - Metastasis: {result2*100:.2f} %')


if __name__=='__main__':
    main()
