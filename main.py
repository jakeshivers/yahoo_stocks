# Importing yfinance library to fetch stock data from Yahoo Finance
import yfinance as yf
import pandas as pd


def fetch_stock_data(symbol):

    stock = yf.Ticker(symbol)
    df = stock.history(period="1mo", interval="5m")
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df = df.reset_index()
    df.rename(columns={"Datetime": "Date"}, inplace=True)
    
    print(df.head(5))
    df.insert(0, "stock_symbol", symbol) 
    print(df.head(5))
    
    
    
    
    
fetch_stock_data(symbol="GOOG")
