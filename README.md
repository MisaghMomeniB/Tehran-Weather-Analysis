![Screenshot from 2024-11-09 18-38-59](https://github.com/user-attachments/assets/4af2c9fa-85ee-4241-848f-84ab35e1b608)
![Screenshot from 2024-11-09 18-38-53](https://github.com/user-attachments/assets/ad2518f4-dc97-4cc8-a021-9ea01bd8ed3b)
![Screenshot from 2024-11-09 18-38-45](https://github.com/user-attachments/assets/7df2b3f8-b551-4d84-bdd6-9574beb72996)

<br>

# 🌤️ Weather Data Analysis 🌧️

This project involves the analysis of weather data collected over a period of time, including various factors such as temperature 🌡️, humidity 💧, pressure ⏱️, wind speed 🌬️, and weather conditions ☀️. The goal is to explore trends over time, analyze relationships between different variables, and visualize these insights using various plots 📊.

## 📑 Project Overview

This repository contains the code and data for weather data analysis. The dataset includes the following columns:

- **Date** 📅: The date of the weather observation.
- **Temperature (°C)** 🌡️: The temperature recorded in degrees Celsius.
- **Humidity (%)** 💧: The humidity level in percentage.
- **Pressure (hPa)** ⏱️: The atmospheric pressure in hectopascals.
- **Wind Speed (km/h)** 🌬️: The wind speed in kilometers per hour.
- **Weather Condition** ☁️: The observed weather condition (e.g., sunny, rainy, cloudy, etc.).

## 🔧 Requirements

Before running the code, ensure that you have the following Python libraries installed:

- `pandas` 📊
- `matplotlib` 🖼️
- `seaborn` 🎨

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib seaborn
```

## 📂 Dataset

The dataset used for this analysis is stored in a CSV file named `weather-csv.csv`. You should place this file in the same directory as the script or provide the appropriate file path.

## 💻 Code Description

### 1. Initial Data Overview 🧐

The script starts by reading the weather data CSV file into a Pandas DataFrame. It then prints out an overview of the data, including:

- The data types of each column 📝.
- A statistical summary of the numeric columns (e.g., mean, standard deviation, min, max) 📊.

### 2. Data Preprocessing 🛠️

The `Date` column is converted to a datetime type to allow proper plotting over time 📅.

### 3. Visualizations 📈

The code generates a set of visualizations using `matplotlib` and `seaborn`:

- **Temperature Trends** 🌡️: A line plot showing how the temperature changes over time.
- **Humidity Trends** 💧: A line plot showing the humidity trends.
- **Pressure Trends** ⏱️: A line plot showing the pressure changes.
- **Wind Speed Trends** 🌬️: A line plot showing the wind speed variations.

These plots are displayed in a 2x2 grid for easy comparison.

### 4. Weather Conditions Distribution 🌥️

A count plot is created to show the distribution of different weather conditions, providing insight into how often each weather type occurred in the dataset 🌈.

### 5. Correlation Analysis 🔍

The script calculates and visualizes the correlation matrix between numeric variables (temperature, humidity, pressure, and wind speed). The correlation matrix is plotted as a heatmap 🌡️🔲 to understand the relationships between these factors.

## ▶️ How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/weather-data-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-data-analysis
   ```

3. Place your `weather-csv.csv` file in the same directory as the script.

4. Run the Python script to generate the plots and analysis:

   ```bash
   python analysis.py
   ```

## 📊 Output

After running the script, you will get the following outputs:

- A set of line plots for temperature, humidity, pressure, and wind speed trends over time 🌡️💧⏱️🌬️.
- A horizontal count plot for the distribution of weather conditions ☀️☁️🌧️.
- A heatmap showing the correlation matrix between the numeric factors 🔲.

## 📄 License

This project is open-source and available under the MIT License 📝.

---

### 1. **Importing Libraries**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
- **`pandas`**: A powerful data manipulation library. It is used for data reading, cleaning, and analysis.
- **`matplotlib.pyplot`**: A plotting library used to create visualizations like graphs and charts.
- **`seaborn`**: Built on top of `matplotlib`, it provides high-level, aesthetically pleasing visualization functions.

### 2. **Reading the CSV File**

```python
file_path = 'weather-csv.csv'  # Path to the CSV file
data = pd.read_csv(file_path)
```
- **`file_path`**: This is the path to the CSV file containing weather data.
- **`pd.read_csv()`**: This function reads the CSV file and loads it into a pandas DataFrame (`data`). The DataFrame is a 2-dimensional table with rows and columns, making it easy to manipulate and analyze data.

### 3. **Initial Data Overview**

```python
print("Initial Data Information:")
print(data.info())
print("\nStatistical Summary of Data:")
print(data.describe())
```
- **`data.info()`**: Displays basic information about the dataset, including the number of rows, column names, data types, and number of non-null values in each column.
- **`data.describe()`**: Provides a statistical summary of numeric columns (e.g., mean, standard deviation, min, max, etc.), which is useful for understanding the distribution of values in the dataset.

### 4. **Convert the Date Column to Datetime Type**

```python
data['Date'] = pd.to_datetime(data['Date'])
```
- **`pd.to_datetime()`**: This function converts the `Date` column, which is likely in string format, into a pandas `datetime` object. This allows you to perform time-based operations (e.g., plotting time series) and ensures that the dates are in a proper format.

### 5. **Setting Plot Dimensions**

```python
plt.figure(figsize=(12, 8))
```
- **`plt.figure(figsize=(12, 8))`**: This sets the size of the entire figure (the grid of plots). It makes the plots large enough for easy viewing, with a width of 12 inches and a height of 8 inches.

### 6. **Plotting Temperature Trends Over Time**

```python
plt.subplot(2, 2, 1)
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], color='orange')
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
```
- **`plt.subplot(2, 2, 1)`**: This specifies the position of the plot in a 2x2 grid. The first plot will appear in the top-left corner (row 1, column 1).
- **`sns.lineplot()`**: A seaborn function used to create a line plot. The `x`-axis represents the `Date`, and the `y`-axis represents the `Temperature (°C)`.
  - **`color='orange'`**: Specifies the color of the line to be orange.
- **`plt.title()`, `plt.xlabel()`, `plt.ylabel()`**: These functions add the title and axis labels to the plot.

### 7. **Plotting Humidity Trends Over Time**

```python
plt.subplot(2, 2, 2)
sns.lineplot(x=data['Date'], y=data['Humidity (%)'], color='blue')
plt.title("Humidity Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
```
- This block is similar to the previous one but plots the humidity trends over time instead. 
- The plot will be placed in the second position in the 2x2 grid (row 1, column 2), and the color is set to blue.

### 8. **Plotting Pressure Trends Over Time**

```python
plt.subplot(2, 2, 3)
sns.lineplot(x=data['Date'], y=data['Pressure (hPa)'], color='purple')
plt.title("Pressure Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
```
- This block plots the pressure trends, with a purple color, in the third position of the 2x2 grid (row 2, column 1).

### 9. **Plotting Wind Speed Trends Over Time**

```python
plt.subplot(2, 2, 4)
sns.lineplot(x=data['Date'], y=data['Wind Speed (km/h)'], color='green')
plt.title("Wind Speed Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
```
- The fourth subplot in the grid (row 2, column 2) shows the wind speed trends over time, with a green line.

### 10. **Adjust Layout and Show Plots**

```python
plt.tight_layout()
plt.show()
```
- **`plt.tight_layout()`**: This automatically adjusts the spacing between plots to ensure that titles and labels don’t overlap.
- **`plt.show()`**: This displays the plots on the screen.

### 11. **Updated Countplot for Weather Conditions**

```python
plt.figure(figsize=(10, 6))
sns.countplot(y=data['Weather Condition'], palette='viridis', orient="h", order=data['Weather Condition'].value_counts().index)
plt.title("Frequency of Weather Conditions")
plt.xlabel("Number of Days")
plt.ylabel("Weather Condition")
plt.xticks(rotation=45)
plt.show()
```
- **`plt.figure(figsize=(10, 6))`**: Sets the size of the count plot figure.
- **`sns.countplot()`**: Creates a count plot (bar plot) to show how often each weather condition occurred.
  - **`y=data['Weather Condition']`**: The `y`-axis represents the weather conditions.
  - **`palette='viridis'`**: Specifies the color palette for the plot.
  - **`orient="h"`**: This makes the bars horizontal.
  - **`order=data['Weather Condition'].value_counts().index`**: Orders the bars based on the frequency of each weather condition, from most frequent to least frequent.
- **`plt.xticks(rotation=45)`**: Rotates the x-axis labels by 45 degrees for better readability.

### 12. **Selecting Only Numeric Columns for Correlation Calculation**

```python
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
```
- **`data.select_dtypes(include=['float64', 'int64'])`**: Selects only the numeric columns (those with data types `float64` and `int64`) from the DataFrame.
- **`numeric_data.corr()`**: Computes the correlation matrix for the selected numeric columns. This matrix shows how strongly the numeric variables are related to each other.

### 13. **Plotting the Correlation Matrix**

```python
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Factors")
plt.show()
```
- **`plt.figure(figsize=(10, 8))`**: Sets the size of the correlation matrix plot.
- **`sns.heatmap()`**: Plots a heatmap of the correlation matrix.
  - **`annot=True`**: Annotates the heatmap with the correlation values.
  - **`cmap="coolwarm"`**: Uses the "coolwarm" color map to represent the correlation values, with colors ranging from blue (negative correlation) to red (positive correlation).
  - **`linewidths=0.5`**: Adds a slight border between cells in the heatmap.
- **`plt.title()`**: Adds a title to the heatmap.

---

### Summary
This script reads weather data from a CSV file, performs some initial data analysis, and generates several plots:

1. Trends of temperature, humidity, pressure, and wind speed over time.
2. A count plot showing the distribution of weather conditions.
3. A heatmap showing the correlations between the numeric factors (temperature, humidity, pressure, wind speed).

Each plot is displayed in a clear and structured manner, providing insights into the weather data.
