import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('50_Startups.csv')
print(df)

numeric_cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']
print("Correlation with Profit:")
print(df[numeric_cols].corr()['Profit'])

X = df[['R&D Spend', 'Marketing Spend']]
y = df['Profit']

plt.scatter(df['R&D Spend'], y)
plt.xlabel('R&D Spend')
plt.ylabel('Profit')
plt.title("Profit vs R&D Spend")
plt.show()

plt.scatter(df['Marketing Spend'], y)
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.title("Profit vs Marketing Spend")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_train_pred)

test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

print("--- Training Performance ---")
print(f"MSE: {train_mse:.2f}")
print(f"RMSE: {train_rmse:.2f}")
print(f"R²: {train_r2:.4f}")

print("--- Testing Performance ---")
print(f"MSE: {train_mse:.2f}")
print(f"RMSE: {train_rmse:.2f}")
print(f"R²: {train_r2:.4f}")

"""
R&D Spend is the strong factor for predicting Profit.
Marketing Spend also helps, but not as much.
The model performs well, with high R² values (~0.91–0.95).
RMSE is small compared to actual profit values, so predictions are close.
Training and testing scores are close, meaning the model is not overfitting.
"""