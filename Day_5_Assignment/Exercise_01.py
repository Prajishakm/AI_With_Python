
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import r2_score
import pandas as pd

data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
X = df[['bmi','s5']]
y = df['target']

model = LinearRegression()
y_pred1 = cross_val_predict(model, X, y)
print("R2 with bmi+s5:", r2_score(y, y_pred1))

X2 = df[['bmi','s5','bp']]
y_pred2 = cross_val_predict(model, X2, y)
print("R2 with bmi+s5+bp:", r2_score(y, y_pred2))

X3 = df[['bmi','s5','bp','s4']]
y_pred3 = cross_val_predict(model, X3, y)
print("R2 with bmi+s5+bp+s4:", r2_score(y, y_pred3))

"""
a) Next variable is 'bp', because after bmi and s5 it has one of the strongest correlations with the target. 
b) Adding 'bp' improves the R² score compared to using only bmi and s5. 
d) Adding even more variables like 's4' gives a small further improvement, but not very big. 
"""