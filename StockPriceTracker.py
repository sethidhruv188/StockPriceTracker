import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def main():
    """Main function to run the stock price tracker."""
    print("Starting stock price tracker...")
    ticker = input("Enter stock ticker (e.g., AAPL, MSFT, TSLA): ").upper()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    if stock_data is None:
        print("Failed to fetch stock data. Exiting.")
        return

    stock_data = calculate_moving_average(stock_data)
    csv_file = save_to_csv(stock_data, ticker)
    plot_file = plot_stock_data(stock_data, ticker)

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data for a given ticker using yfinance."""
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if data.empty:
            print(f"No data found for {ticker}")
            return None
        return data[['Open', 'Close', 'High', 'Low', 'Volume']]
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def calculate_moving_average(data, window=7):
    """Calculate the 7-day moving average of closing prices."""
    try:
        data['Moving_Average'] = data['Close'].rolling(window=window).mean()
        return data
    except Exception as e:
        print(f"Error calculating moving average: {e}")
        return data

def save_to_csv(data, ticker):
    """Save stock data to a CSV file."""
    filename = f"{ticker}_stock_data.csv"
    try:
        data.to_csv(filename)
        print(f"Data saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error saving CSV: {e}")
        return None

def plot_stock_data(data, ticker):
    """Generate and save a plot of closing prices and moving average."""
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
        plt.plot(data.index, data['Moving_Average'], label='7-Day Moving Average', color='orange')
        plt.title(f"{ticker} Stock Price and 7-Day Moving Average")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{ticker}_stock_plot.png")
        plt.close()
        print(f"Plot saved as {ticker}_stock_plot.png")
        return f"{ticker}_stock_plot.png"
    except Exception as e:
        print(f"Error plotting data: {e}")
        return None


main()



