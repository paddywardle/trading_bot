import yfinance as yf
import pandas as pd
from dataclasses import dataclass, field

@dataclass
class OpportunityTickers:

    symbol:str
    period:str=field(default="1y")
    interval:str=field(default="1d")
    ticker:yf.Ticker=field(default=None)

    def __post_init__(self):
        self.ticker:yf.Ticker=yf.Ticker(ticker=self.symbol)

    def get_ticker_history(self) -> pd.DataFrame:

        return self.ticker.history(period=self.period, interval=self.interval)