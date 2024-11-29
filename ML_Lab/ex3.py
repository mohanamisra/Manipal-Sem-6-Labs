from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import accuracy_score, mean_squared_error

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25,  random_state = 42)

# STANDARDISE THE TRAINING AND TESTING FEATURES. IMPORTANT FOR MODELS SENSITIVE TO OUTPUT LIKE SVM
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# SVM
svm = SVC(kernel='linear', C=1.0)
svm.fit(x_train, y_train)
y_pred = svm.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("SVM accuracy = ", accuracy)

# Kernel Ridge Regression
krr = KernelRidge(kernel='rbf', alpha=0.5, gamma=0.1)
krr.fit(x_train, y_train)
krr_pred = krr.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print("MSE of KRR = ", mse)
