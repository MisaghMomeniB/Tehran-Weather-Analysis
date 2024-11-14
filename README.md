![Screenshot from 2024-11-09 18-38-59](https://github.com/user-attachments/assets/4af2c9fa-85ee-4241-848f-84ab35e1b608)
![Screenshot from 2024-11-09 18-38-53](https://github.com/user-attachments/assets/ad2518f4-dc97-4cc8-a021-9ea01bd8ed3b)
![Screenshot from 2024-11-09 18-38-45](https://github.com/user-attachments/assets/7df2b3f8-b551-4d84-bdd6-9574beb72996)

<br>

### Importing Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
- `pandas`: Used to load and manage data in a DataFrame.
- `matplotlib.pyplot` and `seaborn`: Visualization libraries, where `seaborn` provides enhanced and easier-to-style plots.

### Loading Data
```python
file_path = 'weather-csv.csv'  # Path to the CSV file
data = pd.read_csv(file_path)
```
- Sets the path to the CSV file (`weather-csv.csv`) and loads it into a `pandas` DataFrame named `data`.

### Initial Data Overview
```python
print("Initial Data Information:")
print(data.info())
print("\nStatistical Summary of Data:")
print(data.describe())
```
- `data.info()` displays basic information such as column types, number of non-null values, and memory usage.
- `data.describe()` provides a statistical summary, including the mean, standard deviation, and quartiles for each numeric column.

### Converting Date Column to Datetime Format
```python
data['Date'] = pd.to_datetime(data['Date'])
```
- Converts the `Date` column to a datetime format, enabling time-based plotting.

### Setting Plot Dimensions
```python
plt.figure(figsize=(12, 8))
```
- Sets the overall size of the figure to 12x8 inches, allowing sufficient space for subplots.

### Plotting Temperature Trends Over Time
```python
plt.subplot(2, 2, 1)
sns.lineplot(x=data['Date'], y=data['Temperature (°C)'], color='orange')
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
```
- Sets up a 2x2 grid of subplots and creates the first subplot in the upper-left corner.
- Uses `sns.lineplot` to plot temperature over time, setting `Date` as the x-axis and `Temperature (°C)` as the y-axis.
- Adds labels and a title for clarity.

### Plotting Humidity Trends Over Time
```python
plt.subplot(2, 2, 2)
sns.lineplot(x=data['Date'], y=data['Humidity (%)'], color='blue')
plt.title("Humidity Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
```
- Creates the second subplot in the upper-right corner, plotting humidity over time with `Date` on the x-axis and `Humidity (%)` on the y-axis.

### Plotting Pressure Trends Over Time
```python
plt.subplot(2, 2, 3)
sns.lineplot(x=data['Date'], y=data['Pressure (hPa)'], color='purple')
plt.title("Pressure Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Pressure (hPa)")
```
- Creates the third subplot in the lower-left corner, plotting pressure over time with `Date` on the x-axis and `Pressure (hPa)` on the y-axis.

### Plotting Wind Speed Trends Over Time
```python
plt.subplot(2, 2, 4)
sns.lineplot(x=data['Date'], y=data['Wind Speed (km/h)'], color='green')
plt.title("Wind Speed Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
```
- Creates the fourth subplot in the lower-right corner, plotting wind speed over time.

### Adjusting Layout
```python
plt.tight_layout()
plt.show()
```
- `plt.tight_layout()` adjusts the spacing between subplots to avoid overlap.
- `plt.show()` displays the figure with all four subplots.

### Frequency Plot for Weather Conditions
```python
plt.figure(figsize=(10, 6))
sns.countplot(y=data['Weather Condition'], palette='viridis', orient="h", order=data['Weather Condition'].value_counts().index)
plt.title("Frequency of Weather Conditions")
plt.xlabel("Number of Days")
plt.ylabel("Weather Condition")
plt.xticks(rotation=45)
plt.show()
```
- Creates a new figure of size 10x6 inches.
- Uses `sns.countplot` to create a horizontal bar plot showing the frequency of each weather condition.
- `data['Weather Condition'].value_counts().index` sorts the conditions in descending frequency order.
- Sets labels for axes and rotates x-axis ticks for better readability.
- Displays the figure.

### Calculating and Plotting the Correlation Matrix
```python
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
```
- Selects only numeric columns (`float64` and `int64` types) from `data` to calculate correlations.
- `numeric_data.corr()` computes the correlation matrix for the selected columns.

```python
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Factors")
plt.show()
```
- Creates a new figure of size 10x8 inches.
- Uses `sns.heatmap` to plot the correlation matrix, with color mapping (`coolwarm`) and annotations to display correlation values.
- Adds a title and displays the correlation matrix plot.
