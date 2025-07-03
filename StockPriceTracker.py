import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data for a given ticker using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}")
        return data[['Open', 'Close', 'High', 'Low', 'Volume']]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_moving_average(data, window=7):
    """Calculate the 7-day moving average of closing prices."""
    data['Moving_Average'] = data['Close'].rolling(window=window).mean()
    return data

def save_to_csv(data, ticker):
    """Save stock data to a CSV file."""
    filename = f"{ticker}_stock_data.csv"
    data.to_csv(filename)
    return filename

def main():
    """Main function to run the stock price tracker."""
    ticker = input("Enter stock ticker (e.g., AAPL, MSFT, TSLA): ").upper()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    if stock_data is None:
        return
    stock_data = calculate_moving_average(stock_data)
    csv_file = save_to_csv(stock_data, ticker)
    print(f"Data saved to {csv_file}")
    