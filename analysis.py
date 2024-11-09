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

# Plot temperature trends over time
plt.subplot(2, 2, 1)
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], color='orange')
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

# Plot humidity trends over time
plt.subplot(2, 2, 2)
sns.lineplot(x=data['Date'], y=data['Humidity (%)'], color='blue')
plt.title("Humidity Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")