#Importing libraries
import streamlit as st
import pandas as pd
import pickle

st.title('Car Price Prediction')

with open("car_price.sav", 'rb') as f:
   model = pickle.load(f)

col1, col2 = st.columns(2)


with col1:
   a = st.number_input("Present Price:")

with col2:
   b = st.number_input("KMs driven")

with col1:
   c = st.selectbox("Fuel Type",
                   ("Petrol", "Diesel", "CNG"),
                   index=None,
                   placeholder="Select fuel type...",
                  )
   if(c=="Petrol"):
      c=2
   elif(c=="Diesel"):
      c=1
   elif(c=="CNG"):
      c=0

with col2:
   d = st.selectbox("Seller Type",
                   ("Dealer", "Individual"),
                   index=None,
                   placeholder="Select seller type...",
                  )
   if(d=="Dealer"):
      d=0
   elif(d=="Individual"):
      d=1

with col1:
   e = st.selectbox("Transmission Type",
                   ("Manual", "Automatic"),
                   index=None,
                   placeholder="Select transmission type...",
                  )
   if(e=="Manual"):
      e=1
   elif(e=="Automatic"):
      e=0

with col2:
   f = st.slider('Number of Previous Owners', 0, 3, 0)

with col1:
   g = st.slider('Number of years', 5, 20, 5)
   
st.write('---')

pred=0

if st.button('Car Price Prediction'):
   user_input = [a,b,c,d,e,f,g]
   pred = model.predict([user_input])[0]

st.success(round(pred,2))
