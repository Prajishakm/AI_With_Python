import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("Auto.csv")
print(df)

X = df.drop(columns=['mpg', 'name', 'origin'])
y = df['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

alphas = [0.1,0.2,0.3,0.4,0.5,1,2,3,4,5,6,7,8]

ridge_scores = []
for a in alphas:
    ridge = Ridge(alpha=a)
    ridge.fit(X_train, y_train)
    ridge_pred = ridge.predict(X_test)
    ridge_scores.append(r2_score(y_test, ridge_pred))

plt.figure(figsize=(8, 5))
plt.plot(alphas, ridge_scores, marker='o', label="Ridge R2", color='blue')
plt.xlabel("Alpha")
plt.ylabel("R2 Score")
plt.title("Ridge Regression Performance")
plt.legend()
plt.show()

best_ridge_alpha = alphas[np.argmax(ridge_scores)]
print("Ridge alpha:", best_ridge_alpha, "with R2 =", max(ridge_scores))
print("Ridge Results (alpha, R2):")
print(list(zip(alphas, ridge_scores)))

lasso_scores = []
for a in alphas:
    lasso = Lasso(alpha=a, max_iter=1000)
    lasso.fit(X_train, y_train)
    lasso_pred = lasso.predict(X_test)
    lasso_scores.append(r2_score(y_test, lasso_pred))

plt.figure(figsize=(8, 5))
plt.plot(alphas, lasso_scores, marker='o', label="Lasso R2", color='red')
plt.xlabel("Alpha")
plt.ylabel("R2 Score")
plt.title("Lasso Regression Performance")
plt.legend()
plt.show()

best_lasso_alpha = alphas[np.argmax(lasso_scores)]
print("Best Lasso alpha:", best_lasso_alpha, "with R2 =", max(lasso_scores))
print("Lasso Results (alpha, R2):")
print(list(zip(alphas, lasso_scores)))

"""
- Ridge regression stabilizes coefficients and prevents overfitting, especially with correlated predictors.
- Lasso regression can shrink some coefficients to zero, performing feature selection.
- Lists of (alpha, R2) are printed for both Ridge and Lasso.
- Separate plots show how R2 changes with alpha for each method.
- Optimal alpha values are identified for both Ridge and Lasso.
"""
