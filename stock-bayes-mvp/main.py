from fastapi import FastAPI
from data_fetch import get_price_data
from models import technical_model, rsi_model, sentiment_model
from bayes import bayesian_fusion

app = FastAPI()


@app.get("/predict/{symbol}")
def predict(symbol: str):
    df = get_price_data(symbol)

    tech = technical_model(df)
    rsi = rsi_model(df)
    senti = sentiment_model(df)

    result = bayesian_fusion([tech, rsi, senti])

    return {
        "symbol": symbol,
        "technical": tech,
        "rsi": rsi,
        "sentiment": senti,
        "posterior_prob_up": round(result, 4),
    }
