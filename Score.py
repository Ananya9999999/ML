import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data= {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Score': [12,25,32,40,50,55,65,72,80,90]
}
df= pd.DataFrame(data)

x= df[['Hours_Studied']]
y= df[['Score']]

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2, random_state=42)

model= LinearRegression()
model.fit(x_train,y_train)

y_pred= model.predict(x_test)
print("Predictions:", y_pred)
mse= mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

new_data= pd.DataFrame({'Hours_Studied': [10]})
predicted_score= model.predict(new_data)
print(f'Predicted Score for 10 hours studied: {predicted_score[0][0]:.2f}')