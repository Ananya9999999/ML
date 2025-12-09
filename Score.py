import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("Student_Marks.csv")

print("First 5 records:")
print(df.head())

x = df[['time_study']]
y = df[['Marks']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Predictions:", y_pred)

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

new_data = pd.DataFrame({'time_study': [10]})
pred = model.predict(new_data)
print(f"Predicted Marks for studying 10 hours: {pred[0][0]:.2f}")
