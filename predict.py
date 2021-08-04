import streamlit as st 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error
@st.cache
def prediction(car_df,car_width,engine_size,horse_power, drive_wheel_fwd, car_comp_buick):
	x=car_df.iloc[:,:-1]
	y=car_df['price']
	x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)
	lr=LinearRegression()
	lr.fit(x_train,y_train)
	score=lr.score(x_train,y_train)
	price=lr.predict([[car_width,engine_size,horse_power, drive_wheel_fwd, car_comp_buick]])
	price=price[0]
	y_test_pred=lr.predict(x_test)
	r2_score1=r2_score(y_test,y_test_pred)
	mae=mean_absolute_error(y_test,y_test_pred)
	mse=mean_squared_error(y_test,y_test_pred)
	msle=mean_squared_log_error(y_test,y_test_pred)
	return price,score,r2_score1,mae,mse,msle 
def app(car_df):
	st.markdown("<p style='color:red;font-size:40px'> This App Uses <b> Linear Regression </b> </p>")
	st.subheader('Select the values')
	car_wid=st.slider('car width',float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
	eng_size=st.slider('engine size',int(car_df['enginesize'].min()),int(car_df['enginesize'].max()))
	hor_pow=st.slider('horse power',int(car_df['horsepower'].min()),int(car_df['horsepower'].max()))
	driver_fwd=st.radio('Is is a forward wheel car',('yes','no'))
	if driver_fwd=='no':
		driver_fwd=0 
	else:
		driver_fwd=1 
	car_comp=st.radio('is the car manufactured by buick',('yes','no'))
	if car_comp=='no':
		car_comp=0
	else:
		car_comp=1 
	if st.button('predict'):
		st.subheader('Prediction Results')
		price,score,r2_score1,mae,mse,msle=prediction(car_df,car_wid,eng_size,hor_pow,driver_fwd,car_comp)
		st.write('predicted price of car is',price)
		st.write('score of this model is',score)
		st.write('r2_score is',r2_score1)
		st.write('mse is',mse)
		st.write('mae is',mae)
		st.write('msle is',msle)



