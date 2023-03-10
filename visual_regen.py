# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the data from CSV file
data = pd.read_csv('regen_data.csv')

# Creating the subplots
fig, axs = plt.subplots(2, 2, figsize=(10,10))

# Plotting the Load vs Regen Energy graph
axs[0, 0].scatter(data['Load'], data['Regen Energy'], color='blue')
axs[0, 0].set_title('Load vs Regen Energy')
axs[0, 0].set_xlabel('Load (kg)')
axs[0, 0].set_ylabel('Regen Energy (kJ)')

# Plotting the Speed vs Regen Energy graph
axs[0, 1].scatter(data['Speed'], data['Regen Energy'], color='green')
axs[0, 1].set_title('Speed vs Regen Energy')
axs[0, 1].set_xlabel('Speed (km/h)')
axs[0, 1].set_ylabel('Regen Energy (kJ)')

# Plotting the Brake Pressure vs Regen Energy graph
axs[1, 0].scatter(data['Brake Pressure'], data['Regen Energy'], color='red')
axs[1, 0].set_title('Brake Pressure vs Regen Energy')
axs[1, 0].set_xlabel('Brake Pressure (bar)')
axs[1, 0].set_ylabel('Regen Energy (kJ)')

# Plotting the Correlation Matrix
corrMatrix = data.corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()
