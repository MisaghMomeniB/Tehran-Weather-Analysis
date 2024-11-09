__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# Tehran-Weather-Analysis 🐍

In This Project, I Tried to Create a __Data Analysis__ With Chart Visualization Using Python and Its Related Libraries.
# Does It Require Any Installation Steps or Prerequisites?

`` python -m venv venv `` <br>
`` pip install pandas seaborn matplotlib `` <br>
# Line-by-line Code Analysis

### Importing Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
- **`pandas`**: Used for data manipulation and analysis. It helps with handling the CSV file, data cleaning, and data operations.
- **`matplotlib.pyplot`**: A plotting library used to create static, animated, and interactive visualizations.
- **`seaborn`**: Built on top of matplotlib, seaborn provides a high-level interface for drawing attractive and informative statistical graphics.

### Reading the CSV File
```python
file_path = 'weather-csv.csv'  # Path to the CSV file
data = pd.read_csv(file_path)
```
- The CSV file located at `file_path` is read into a DataFrame called `data`. The `read_csv()` function reads the file and converts it into a tabular format that pandas can work with.

### Initial Data Overview
```python
print("Initial Data Information:")
print(data.info())
print("\nStatistical Summary of Data:")
print(data.describe())
```
- **`data.info()`**: Displays a concise summary of the DataFrame, including the number of non-null entries in each column, data types, and memory usage.
- **`data.describe()`**: Provides statistical details of the numeric columns such as mean, standard deviation, min, max, and quartiles.

### Converting Date Column to Datetime
```python
data['Date'] = pd.to_datetime(data['Date'])
```
- This line converts the `Date` column to a `datetime` format. This is essential for time-based operations like plotting time series data.

### Plotting Temperature Trends
```python
plt.figure(figsize=(12, 8))

# Plot temperature trends over time
plt.subplot(2, 2, 1)
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], color='orange')
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
```
- **`plt.figure(figsize=(12, 8))`**: Sets the figure size for the plots to be 12x8 inches.
- **`plt.subplot(2, 2, 1)`**: Creates a 2x2 grid of subplots, and the current plot will occupy the first position (top-left).
- **`sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], color='orange')`**: Plots the temperature over time. The x-axis represents the date and the y-axis represents temperature in degrees Celsius.
- **`plt.title()`, `plt.xlabel()`, `plt.ylabel()`**: These functions add titles and labels to the plot for clarity.

### Plotting Humidity Trends
```python
# Plot humidity trends over time
plt.subplot(2, 2, 2)
sns.lineplot(x=data['Date'], y=data['Humidity (%)'], color='blue')
plt.title("Humidity Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
```
- **`plt.subplot(2, 2, 2)`**: This places the current plot in the second position (top-right) of the 2x2 grid.
- **`sns.lineplot(x=data['Date'], y=data['Humidity (%)'], color='blue')`**: Plots the humidity trend over time using a blue line.

### Plotting Pressure Trends
```python
# Plot pressure trends over time
plt.subplot(2, 2, 3)
sns.lineplot(x=data['Date'], y=data['Pressure (hPa)'], color='purple')
plt.title("Pressure Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
```
- **`plt.subplot(2, 2, 3)`**: Places this plot in the third position (bottom-left) of the 2x2 grid.
- **`sns.lineplot(x=data['Date'], y=data['Pressure (hPa)'], color='purple')`**: Plots the pressure trend over time using a purple line.

### Plotting Wind Speed Trends
```python
# Plot wind speed trends over time
plt.subplot(2, 2, 4)
sns.lineplot(x=data['Date'], y=data['Wind Speed (km/h)'], color='green')
plt.title("Wind Speed Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
```
- **`plt.subplot(2, 2, 4)`**: This places the plot in the fourth position (bottom-right) of the 2x2 grid.
- **`sns.lineplot(x=data['Date'], y=data['Wind Speed (km/h)'], color='green')`**: Plots the wind speed trend over time using a green line.

### Adjusting Layout and Showing the Plot
```python
plt.tight_layout()
plt.show()
```
- **`plt.tight_layout()`**: Automatically adjusts the subplots to fit within the figure area without overlapping.
- **`plt.show()`**: Displays the plots.

### Plotting the Weather Conditions
```python
# Updated countplot for weather conditions
plt.figure(figsize=(10, 6))
sns.countplot(y=data['Weather Condition'], palette='viridis', orient="h", order=data['Weather Condition'].value_counts().index)
plt.title("Frequency of Weather Conditions")
plt.xlabel("Number of Days")
plt.ylabel("Weather Condition")
plt.xticks(rotation=45)
plt.show()
```
- **`plt.figure(figsize=(10, 6))`**: Creates a new figure with size 10x6 inches for the weather condition plot.
- **`sns.countplot(y=data['Weather Condition'], ...)`**: Creates a countplot (a bar plot that shows the frequency of weather conditions). The `y` parameter sets weather conditions on the y-axis. The `order` argument orders the bars based on the frequency of weather conditions.
- **`plt.xticks(rotation=45)`**: Rotates the x-axis labels by 45 degrees to make them readable.

### Correlation Matrix of Numeric Data
```python
# Selecting only numeric columns for correlation calculation
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
```
- **`data.select_dtypes(include=['float64', 'int64'])`**: Selects only the numeric columns (those of type float64 or int64) from the DataFrame for correlation analysis.
- **`numeric_data.corr()`**: Calculates the correlation matrix for the numeric columns. The result shows how strongly the different variables (like temperature, humidity, etc.) are correlated with each other.

### Plotting the Correlation Matrix
```python
# Plot the updated correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Factors")
plt.show()
```
- **`plt.figure(figsize=(10, 8))`**: Creates a new figure with size 10x8 inches for the heatmap.
- **`sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)`**: Plots the correlation matrix as a heatmap. The `annot=True` adds numerical annotations in each cell of the matrix, and `cmap="coolwarm"` specifies the color scheme.
- **`plt.title("Correlation Matrix of Factors")`**: Adds a title to the heatmap.
- **`plt.show()`**: Displays the heatmap.

---

### Summary of Actions
1. **Data Inspection**: Prints basic information and statistical summary of the dataset.
2. **Date Conversion**: Converts the "Date" column into a proper datetime format for time series analysis.
3. **Plots Over Time**: Creates four subplots showing trends in temperature, humidity, pressure, and wind speed over time.
4. **Weather Condition Frequency**: Shows a countplot to visualize the distribution of weather conditions.
5. **Correlation Analysis**: Computes and visualizes the correlation matrix of the numeric variables.

These steps are used to analyze and visualize the dataset, identifying trends, distributions, and relationships between weather-related variables.
