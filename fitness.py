import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('mental_health_data.csv')

data.dropna(inplace=True)

X = data[['year', 'country', 'sex', 'age', 'suicides_no']]
y = data['suicides_no']

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

def predict_mental_health_score(year, country, sex, age):
    user_inputs = pd.DataFrame({
        'year': [year],
        'country': [country],
        'sex': [sex],
        'age': [age],
        'suicides_no': [0]  
    })
    user_inputs = pd.get_dummies(user_inputs)
    predicted_score = model.predict(user_inputs)
    return predicted_score[0]

predicted_score = predict_mental_health_score(2020, 'United States', 'male', '35-54 years')
print(f"Predicted Mental Health Score: {predicted_score}")

