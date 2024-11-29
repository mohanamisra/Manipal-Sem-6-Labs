from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

from sklearn.linear_model import LogisticRegression

x, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state=42)

# Logistic Regression
lr = LogisticRegression(random_state=1)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(accuracy)
print(mse)
