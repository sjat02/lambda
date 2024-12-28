import pandas as pd
import numpy as np
import streamlit as st

st.title('Title of the app')

st.write('This is a simple text')

df = pd.DataFrame({'First Col':[1,2,3,4,5],
                   'second col':[10,20,30,40,50]})

st.write('here is the dataframe')

st.write(df)


chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(chart_data)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")


upload_file=st.file_uploader("Choose a file uploader")

if upload_file is not None:
     df= pd.read_csv(upload_file)
     st.write(df)

