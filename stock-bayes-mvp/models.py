import numpy as np
import pandas as pd


# 技术模型：均线交叉
def technical_model(df):
    df["ma_short"] = df["Close"].rolling(5).mean()
    df["ma_long"] = df["Close"].rolling(20).mean()

    if df["ma_short"].iloc[-1] > df["ma_long"].iloc[-1]:
        prob = 0.6
    else:
        prob = 0.4

    return {"prob_up": prob, "confidence": 0.6}


# RSI模型
def rsi_model(df, period=14):
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    last_rsi = rsi.iloc[-1]

    if last_rsi < 30:
        prob = 0.65
    elif last_rsi > 70:
        prob = 0.35
    else:
        prob = 0.5

    return {"prob_up": prob, "confidence": 0.7}


# 情绪模型（模拟）
def sentiment_model(df):
    prob = np.random.normal(0.5, 0.05)
    prob = max(min(prob, 0.7), 0.3)

    return {"prob_up": prob, "confidence": 0.5}
