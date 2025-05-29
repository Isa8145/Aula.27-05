import pandas as pd
import streamlit as st

try: 
  tot_registros = df.count() ['total']
except: 
  df = pd.read_csv('circuits.csv')

st.bar_chart(df, x='month', y='total')
