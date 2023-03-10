# Importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Reading the data from CSV file
data = pd.read_csv('regenerative_braking_data.csv')

# Preparing the data for training
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set results
y_pred = regressor.predict(X_test)

# Printing the predicted and actual values
print("Predicted Values:", y_pred)
print("Actual Values:", y_test)
