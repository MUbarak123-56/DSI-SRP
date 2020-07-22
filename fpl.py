from pycaret.regression import load_model, predict_model
import pandas as pd
import numpy as np
import streamlit as st

fpl_model = load_model("Fantasy_predictive_model")

def predict(model, input_df):
    fpl_pred = predict_model(estimator = model,data = input_df)
    fpl_prediction = fpl_pred['Label'][0]
    return fpl_prediction

def run():
    from PIL import Image
    image = Image.open('logo-premier-league.jpg')
    st.image(image, use_column_width = True)

    st.title('Fantasy Premier League Predictor app')
    st.header('Welcome to FPL Player Points per Game Predictor!')
    st.write('Insert players features to find out their predicted FPL scores')
    st.write('')
    st.header('Guide for the position index:')
    st.write('1 is for Goalkeeper')
    st.write('2 is for Centre-Back, Left-Back or Right-Back')
    st.write('3 is for Defensive Midfield, Central Midfield, Left Midfield, Right Midfield or Midfielder')
    st.write('4 is for Left Winger, Right Winger or Attacking Midfielder')
    st.write('5 is for Forward, Second Striker or Centre-Forward')
    
    name = st.text_input('Name')
    goals_scored = st.number_input('Goals', min_value = 0, value = 0)
    assists = st.number_input('Assists', min_value = 0, value = 0)
    minutes = st.number_input('Minutes', min_value = 0, value = 0)
    clean_sheets = st.number_input('Clean Sheets', min_value = 0, value = 0)
    position_index = st.selectbox('Position Index', [1,2,3,4,5])
    matches = st.number_input('Games Played', min_value = 0, value = 0)

    output = 0
    fpl_dict = {'goals_scored':goals_scored, 'minutes':minutes, 'assists':assists, 'clean_sheets':clean_sheets,'position_index':position_index}
    fpl_input = pd.DataFrame([fpl_dict])

    if st.button("Calculate FPL points per game"):
        output = predict(model = fpl_model, input_df = fpl_input)
        output = float(output)
        output = (output/minutes)*90
    st.success('The predicted FPL points per game is %.2f'%(float(output)))

if __name__ == '__main__':
    run()