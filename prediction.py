# Importing required libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Reading the data from CSV file
data = pd.read_csv('regen_data.csv')

# Preparing the data for training
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Training the model
regressor = LinearRegression()
regressor.fit(X, y)

# Predicting the Regenerative Energy for new input values
new_data = np.array([[2300, 50, 5]])
new_pred = regressor.predict(new_data)

# Printing the predicted Regenerative Energy for new input values
print("Predicted Regenerative Energy for New Input Values:", new_pred)
