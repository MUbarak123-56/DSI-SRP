import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

fpl_ult = pd.read_csv("FPL_ULTIMATE.csv", encoding = "latin1")
fpl_ult = fpl_ult.drop("Unnamed: 0", axis = 1)
fpl_ultx = fpl_ult[['goals_scored', 'assists', 'minutes', 'clean_sheets', 'position_index']]
fpl_ulty = fpl_ult['total_points']

fpl_xtrain, fpl_xtest, fpl_ytrain, fpl_ytest = train_test_split(fpl_ultx, fpl_ulty, train_size = 0.75, random_state = 69)
model_fpl = make_pipeline(PolynomialFeatures(3), LinearRegression())
model_fpl.fit(fpl_xtrain, fpl_ytrain)

def run():
    from PIL import Image
    image = Image.open('Premier-League-balls.jpg')
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
    minutes = st.number_input('Minutes Played', min_value = 0, value = 0)
    matches = st.number_input('Games Played', min_value = 0, value = 0)
    clean_sheets = st.number_input('Clean Sheets', min_value = 0, value = 0)
    st.write("Refer to the guide above for position index")
    position_index = st.selectbox('Position Index', [1,2,3,4,5])
    st.write("Use this link to find your players' FPL point: https://fantasy.premierleague.com/statistics")
    actual_points = st.number_input('FPL Points', min_value = 0, value = 0)

    output = 0
    fpl_input = np.array([[goals_scored, assists, minutes,clean_sheets, position_index]])

    if st.button("Calculate FPL points per game"):
        output = model_fpl.predict(fpl_input)
        output = (output/minutes)*90
        st.write("After playing", str(matches), "games,", name, "has a predicted FPL points to game ratio of:")
        st.success('%.2f'%(float(output))) 
        fpg = (actual_points/minutes)*90
        st.write('His actual FPL points to game ratio is: %.2f'%(float(fpg)))

if __name__ == '__main__':
    run()