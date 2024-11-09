import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
file_path = '/mnt/data/weather_data.csv'  # Path to the CSV file
data = pd.read_csv(file_path)

# Initial data overview
print("Initial Data Information:")
print(data.info())
print("\nStatistical Summary of Data:")
print(data.describe())

# Convert the Date column to datetime type
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

# Plot pressure trends over time
plt.subplot(2, 2, 3)
sns.lineplot(x=data['Date'], y=data['Pressure (hPa)'], color='purple')
plt.title("Pressure Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")

# Plot wind speed trends over time
plt.subplot(2, 2, 4)
sns.lineplot(x=data['Date'], y=data['Wind Speed (km/h)'], color='green')
plt.title("Wind Speed Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")

plt.tight_layout()
plt.show()

# Plot frequency of weather conditions
plt.figure(figsize=(10, 6))
sns.countplot(data['Weather Condition'], palette='viridis')
plt.title("Frequency of Weather Conditions")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Days")
plt.xticks(rotation=45)
plt.show()

# Plot correlation matrix between factors
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Factors")
plt.show()
