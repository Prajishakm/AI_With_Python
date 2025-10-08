import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv('bank.csv', delimiter=';')

print(df.head())
print("\nColumn names:\n", df.columns)
print("\nData types:\n", df.dtypes)

df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
print(df2.head())

df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])
print(df3.head())

df3['y'] = df3['y'].apply(lambda x: 1 if x == 'yes' else 0)

plt.figure(figsize=(12, 8))
sns.heatmap(df3.corr(), cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap for Bank Dataset")
plt.show()

"""
Explanation:
From the heatmap, we can see that most of the variables are only weakly correlated.
This means there’s no strong linear relationship between most features.
Dummy variables from the same category (e.g., marital status or job type)
show slight negative correlations since they represent mutually exclusive groups.
"""

X = df3.drop('y', axis=1)
y = df3['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

cm_log = metrics.confusion_matrix(y_test, y_pred_log)
sns.heatmap(cm_log, annot=True, fmt='d', cmap='Greens')
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("Accuracy (Logistic Regression):", metrics.accuracy_score(y_test, y_pred_log))

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

cm_knn = metrics.confusion_matrix(y_test, y_pred_knn)
sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - KNN (k=3)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("Accuracy (KNN, k=3):", metrics.accuracy_score(y_test, y_pred_knn))

"""
Model Comparison:

- Logistic Regression:
  Works well when the relationship between variables and target is approximately linear.
  Usually performs better for large datasets and is more interpretable.

- K-Nearest Neighbors (K=3):
  Works well for non-linear relationships, but can be slower and less accurate
  for large datasets with many features.

Typically, in the Bank Marketing dataset, Logistic Regression gives slightly
better accuracy and clearer insights than KNN.
"""