from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(y_test)
print(y_pred)
print(accuracy_score(y_test, y_pred))