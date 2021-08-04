import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def app(car_df):
	st.header('visualize data')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.subheader('scatterplot')
	features_list=st.multiselect('select x axis values',('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
	for i in features_list:
		st.subheader('scatterplot between'+i+' and price')
		plt.figure(figsize=(16,6))
		sns.scatterplot(car_df[i],car_df['price'])
		st.pyplot()
	st.subheader('visualization selecter')
	plot_select=st.multiselect('select charts',('histogram','boxplot','heatmap'))
	if 'histogram' in plot_select:
		st.subheader('histogram')
		col=st.selectbox('select columns to create histogram',('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize=(16,6))
		plt.title('histogram for'+col)
		plt.hist(car_df[col],bins='sturges')
		st.pyplot()
	if 'boxplot' in plot_select:
		st.subheader('boxplot')
		cols=st.selectbox('select columns to create boxplot',('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize=(16,6))
		plt.title('boxplot for'+cols)
		sns.boxplot(car_df[cols])
		st.pyplot()
	if 'heatmap' in plot_select:
		st.subheader('heatmap')
		plt.figure(figsize=(16,6))
		sns.heatmap(car_df.corr(),annot=True)
		st.pyplot()