# -*- coding: utf-8 -*-
"""ML Lab Exp4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R9zu3JqrfraQaComRjZgDUiJCXQotAYB

# **EXPERIMENT-4 (Logistic Regression)**

# BOSTAN HOUSE PRICE PREDICTION
"""

from sklearn.datasets import load_iris

data=load_iris()

data.DESCR

data.keys()

data.target_names

X=data.data
y=data.target

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(X_train,y_train)

((X_train.shape,y_train.shape),(X_test.shape,y_test.shape))

predictions=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,predictions)

data.feature_names

!pip install -q pyngrok
!pip install -q streamlit

import pickle
pickle_out=open('Flower_data.pkl','wb')
pickle.dump(model,pickle_out)
pickle_out.close()

import streamlit as st
import pickle
pickle_in=open('Flower_data.pkl','rb')
model=pickle.load(pickle_in)

sepal_length=st.number_input('sepal length (cm)')
sepal_width=st.number_input('sepal width (cm)')
petal_length=st.number_input('petal length (cm)')
petal_width=st.number_input('petal width (cm)')
r=""
if st.button("PREDICT"):
  result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
  if result==0:
    print("Predicted Flower is SETOSA")
  elif result==1:
    print("Predicted Flower is VERSICOLOR")
  else:
    print("Predicted Flower is VERGINICA")





