import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

df = pd.read_csv("weight-height.csv")
print(df.head())

X = df["Height"].values.reshape(-1, 1)
y = df["Weight"].values

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.scatter(X, y, alpha=0.5, label="Data")
plt.plot(X, y_pred, color="red", label="Regression Line")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.show()

rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("Root Mean Squared Error (RMSE):", rmse)
print("R² score:", r2)