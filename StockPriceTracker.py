import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data for a given ticker using yfinance."""
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data[['Open', 'Close', 'High', 'Low', 'Volume']]

def calculate_moving_average(data, window=7):
    """Calculate the 7-day moving average of closing prices."""
    data['Moving_Average'] = data['Close'].rolling(window=window).mean()
    return data

def save_to_csv(data, ticker):
    """Save stock data to a CSV file."""
    filename = f"{ticker}_stock_data.csv"
    data.to_csv(filename)
    return filename
