import streamlit as st
import numpy as np
import pandas as pd
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('View Data')
  with st.beta_expander('view dataset'):
    st.table(car_df)
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())    
    
    # ADD NEW CODE FROM HERE
    beta_col1,beta_col2,beta_col3=st.beta_columns(3)
    with beta_col1:
      if st.checkbox('show all column names'):
        st.table(list(car_df.columns))
    with beta_col2:
      if st.checkbox('view column data type'):
        st.table(car_df.dtypes)
    with beta_col3:
      if st.checkbox('view column data'):
        col_data=st.selectbox('select column',tuple(car_df.columns))
        st.write(car_df[col_data])