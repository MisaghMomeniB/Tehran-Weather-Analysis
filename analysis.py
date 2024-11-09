import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV File
file_path = 'weather-csv.csv'
data = pd.read_csv(file_path)

# Initial data overview
print("Initial Data Information : ")
print(data.info())
print("\nStatistical Summary of Data : ")
print(data.describe())

# Convert the Data column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Set plot dimensions
plt.figure(figsize=(12, 8))