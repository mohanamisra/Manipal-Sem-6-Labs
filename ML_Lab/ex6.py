import numpy as np
from sklearn.linear_model import LinearRegression
# Generate some random data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
# Create a LinearRegression object
lin_reg = LinearRegression()
# Train the model on the data
lin_reg.fit(X, y)
# Print the intercept and coefficients
print("Intercept: ", lin_reg.intercept_)
print("Coefficients: ", lin_reg.coef_)
# Make a prediction
X_new = np.array([[0], [2]])
y_pred = lin_reg.predict(X_new)
# Print the predicted values
print("Predicted values: ", y_pred)