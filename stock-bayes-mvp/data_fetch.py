import yfinance as yf
import pandas as pd


def get_price_data(symbol: str, period="3mo", interval="1d"):
    data = yf.download(symbol, period=period, interval=interval)
    data = data.dropna()
    return data
