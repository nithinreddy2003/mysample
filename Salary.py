import streamlit as st
import pickle
pickle_in=open('Salary_Prediction.pkl','rb')
model=pickle.load(pickle_in)

Experience=st.number_input('Enter Years Of Experience')
if st.button("PREDICT"):
  salary=model.predict([[Experience]]).squeeze()
  salary=int(salary)
  st.success(f'SALARY PREDICTED IS {salary}')
