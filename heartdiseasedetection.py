# -*- coding: utf-8 -*-
"""HeartDiseaseDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ukS0okch2qGBb2yRfzOvD8d5jaxBvgxC
"""



import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('/content/data.csv')

heart_data.head()



# print last 5 rows of the dataset
heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.isnull().sum()

heart_data.describe()

heart_data['target'].value_counts()

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Test data : ', test_data_accuracy)

#@title Form
Age = 62 #@param {type:"integer"}
Sex = 0 #@param {type:"integer"}
CP = 0 #@param {type:"integer"}
trestbps = 0 #@param {type:"integer"}
chol = 0 #@param {type:"integer"}
fbs = 0 #@param {type:"integer"}
restecg = 0 #@param {type:"integer"}
thalach = 0 #@param {type:"integer"}
exang = 0 #@param {type:"integer"}
oldpeak = 0 #@param {type:"integer"}
slope = 0 #@param {type:"integer"}
ca = 0 #@param {type:"integer"}
thal = 0 #@param {type:"integer"}
target = 0 #@param {type:"integer"}

input_data = (Age,Sex,CP,140,268,0,0,160,0,3.6,0,2,2)
#input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

#@title Form
Age = 52 #@param {type:"integer"}
Sex = 0 #@param {type:"integer"}
CP = 0 #@param {type:"integer"}
trestbps =  140#@param {type:"integer"}
chol =  268#@param {type:"integer"}
fbs =  0#@param {type:"integer"}
restecg = 0 #@param {type:"integer"}
thalach =  160#@param {type:"integer"}
exang = 0 #@param {type:"integer"}
oldpeak =  3.6#@param {type:"number"}
slope = -2 #@param {type:"integer"}
ca =  2#@param {type:"integer"}
thal =  2#@param {type:"integer"}
target = 0 #@param {type:"integer"}

input_data = (Age,Sex,CP,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
#input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

