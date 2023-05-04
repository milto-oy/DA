import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

df = pd.read_csv('housing.csv')
st.title('The Boston Housing Dataset')
st.text('')
st.text('')

size = st.slider('Пропорция тестовой и обучающей выборок:', 0.01, 1.0, 0.01)
st.write(f'Доля тестовой выборки {size*100}% ')

if st.button('Отобразить первые десять строк'):
    st.write(df.head(10))

if st.button('Обучить модель. Рассчитать показатель MAE'):
    X_train, X_test, y_train, y_test = train_test_split(df.drop('MEDV', axis=1),
                                                        df['MEDV'],
                                                        test_size=size,
                                                        random_state=2100)
    st.write('Разделили данные и передали в обучение')
    regr_model = XGBRegressor()
    regr_model.fit(X_train, y_train)
    pred = regr_model.predict(X_test)
    st.write('Обучили модель, MAE = ' + str(mean_absolute_error(y_test, pred)))
