import streamlit as st
import pickle
import numpy as np



model=pickle.load(open('model.pkl','rb'))



st.title("Heart Diseasis Prediction")
st.markdown("CareFully Fill  Your Medical Data ")


col1,col2=st.columns(2)


with col1:
   age=st.number_input("Enter Your Age",0,100,40)
   sex=st.selectbox("Gender",[0,1])
   cp=st.selectbox("Chest Pain Type",[0,1,2,3])
   trestbps=st.number_input("Blood presser",75,200,120)
   chol=st.number_input("Cholesterol(mg/dl)",100,650,200)
   fbs=st.selectbox("Blood Suger",[0,1])

with col2:
  restecg=st.selectbox("ECG",[0,1,2])
  thalach=st.number_input("MAX Heart Rate",65,220,140)
  exang=st.selectbox("Angina",[0,1])
  oldpeak=st.number_input("ST Depression",0.0,10.0,1.0,step=0.1)
  slope=st.selectbox("Slope",[0,1,2])
  ca=st.selectbox("Major Vessels",[0,1,2,3])
  thal=st.selectbox("Thal ",[1,2,3])


if st.button("Click"):
   data=np.array([[age,sex,cp,trestbps,chol,fbs,
                restecg,thalach,exang,oldpeak,slope,ca,thal]])
   
   prediction=model.predict(data)[0]

   if prediction==1:
      st.warning("You Have Heart Disease")
   else:
      st.success("You are Fine")