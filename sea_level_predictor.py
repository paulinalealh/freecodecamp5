import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy.stats import stats

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
 
    # Create first line of best fit
    years = np.arange(df["Year"].min(),2051)
    fl_prediction = predict_y(df["Year"], df["CSIRO Adjusted Sea Level"], years)
    plt.plot(years, 
             fl_prediction, 
             color= "turquoise")

    # Create second line of best fit
    recent_years= np.arange(2000,2051)
    mask = df["Year"] >= 2000
    x_train = df.loc[mask, "Year"]
    y_train = df.loc[mask, "CSIRO Adjusted Sea Level"]
    sl_prediction = predict_y(x_train,y_train,recent_years)
    plt.plot(recent_years, 
             sl_prediction, 
             color= "aquamarine")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


def predict_y(x_train,y_train, x_pred):
    slope, intercept, *_ = stats.linregress(x_train,y_train)  
    return slope * x_pred + intercept

draw_plot()