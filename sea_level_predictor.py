import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_predictor():
    # Load Data
    data = pd.read_csv("./epa-sea-level.csv")

    # Extract the year from the 'Year' column
    data['Year'] = data['Year'].str.extract('(\d+)', expand=False)

    # Convert 'Year' to numeric and handle non-numeric values
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
    data = data.dropna(subset=['Year', 'CSIRO Adjusted Sea Level'])

    # Create Scatter Plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Linear Regression - Full Dataset
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Predict Sea Level in 2050 - Full Dataset
    plt.plot(data['Year'], slope * data['Year'] + intercept, color='red', label='Full Dataset')
    plt.plot([i for i in range(1880, 2051)], [slope * i + intercept for i in range(1880, 2051)], color='red', linestyle='dashed')

    # Linear Regression - Since 2000
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Predict Sea Level in 2050 - Since 2000
    plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='blue', label='Since 2000')
    plt.plot([i for i in range(2000, 2051)], [slope_recent * i + intercept_recent for i in range(2000, 2051)], color='blue', linestyle='dashed')

    # Finalize Plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()

    return plt

# Call the function to run the code
sea_level_predictor()

