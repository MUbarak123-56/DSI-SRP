# FPL-Predictor

This is a repository for the Fantasy Premier League Predictor project.

### Prerequisite
To conduct this project, the following tools & technologies were leveraged:
- pandas
- NumPy
- tidyverse
- scikit-learn
- matplotlib
- Tableau
- R
- Python
- R studio
- Jupyter Notebook

### Description
The Premier League is the most entertaining soccer league globally.Therefore, I have decided 
to build a web application that is going to estimate players’ performance so teams can deploy it in
signing players within the premier league. The metric used to gauge
performance is called FPL points. FPL stands for Fantasy Premier League, which is an
online platform where players are given points based on performance after gameplay.
The goal of this project is to calculate the expected FPL points per game for players in
the premier league based on certain stats.

#### Data Collection & Wrangling
Data was collected from multiple sources, transformed,
cleaned, wrangled and combined to build new datasets that were going to be used for
data visualization and modeling. The final dataset that proved to be very useful is one
that contained a cumulative weekly data that summed up players’ performance
variables from August 2016 till May 2019.

#### Exploratory Data Analysis
After using different sources to collect data sets, newly
formed datasets on 2016/17, 2017/18 and 2018/19 seasons were created. Then, bar
charts, scatter plots, box plots and interactive dashboards were built to show how
different variables interrelate with each other as well as how the players’ FPL points
differed based on positions. A dashboard that shows players' progression over time from 2016 to 2021 can
be seen on Tableau [here](https://public.tableau.com/app/profile/mubarak.ganiyu/viz/FPLanalysis2016-2021/FPLPoints201617).

#### Modeling
Using a dataset that added up players’ stats over the course of three
seasons for modeling was optimal. This made it possible for the model to study what
happened after 200 minutes of gameplay as well as what happened after 4000 minutes
of gameplay and make predictions. Moreover, it was utilizing a huge dataset of over
45,000 records in which each player had about 38 to 114 recorded rows of gameplay in
the dataset. This made it easy for the model to learn how different players would be
expected to perform based on position and use this knowledge combined with the other
systematically chosen stats to predict FPL points.

#### Web Application
The final activity was to build a web application that let people input
players’ names as well as their stats and use the predictive model to output a prediction
of the FPL points per game. Here is the [link](https://fpl-predictor.herokuapp.com/) to the created website. The values of
variables from this [dataset](https://docs.google.com/spreadsheets/d/129W2qsK1sHmTfqVh4PLSX14ZrVKFg1t_xVz6LlsuIRQ/edit#gid=405641194) can be tested with the web app.

### Contact Info

Mubarak Ganiyu - mubarak.a.ganiyu@vanderbilt.edu

