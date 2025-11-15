import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data= pd.DataFrame({
    'texts_per_day': [1, 10, 3, 0, 5, 7, 2, 8, 4, 6],
    'emoji_usage': [0, 5, 2, 0, 3, 4, 1, 5, 2, 4],
    'left_on_read': [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    'asked_you_out': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'plans_a_date': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'buys_you_flowers': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'buys_you_tea': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'likes_you': [0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
})
x= data.drop('likes_you', axis=1)
y= data['likes_you']
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=42)
model= LogisticRegression()
model.fit(x_train, y_train)
y_pred= model.predict(x_test)
accuracy= accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
new_data= pd.DataFrame({
    'texts_per_day': [3],
    'emoji_usage': [0],
    'left_on_read': [0],
    'asked_you_out': [0],
    'plans_a_date': [1],
    'buys_you_flowers': [0],
    'buys_you_tea': [1],
})
pred= model.predict_proba(new_data)[0][1]
if pred < 0.5 and pred>0.0:
    print(f"AI says: {pred*100:.2f}% chance they like you.")
elif pred >0.5:
    print(f"AI says: {pred*100:.2f}% chance they like you. Go for it!")
else:
    print(f"AI says: only {pred*100:.2f}% chance they like you. Maybe reconsider.")