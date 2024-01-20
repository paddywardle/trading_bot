from src.opportunities.OpportunityTickers import OpportunityTickers

import yfinance as yf
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import sma_indicator

class TechnicalIndicators:

    def __init__(self, windows:list[int]=None) -> None:

        self.windows = windows or [14,30,50,200]
    
    def get_sma(self, opportunity_tickers:pd.DataFrame=None, window:int=None) -> pd.DataFrame:

        opportunity_tickers["sma" + str(window)] = sma_indicator(close=opportunity_tickers["Close"], window=window, fillna=False)

        return opportunity_tickers

    def get_rsi(self, opportunity_tickers:pd.DataFrame=None, window:int=None) -> pd.DataFrame:

        opportunity_tickers["rsi" + str(window)] = RSIIndicator(close=opportunity_tickers["Close"], window=window).rsi()
        
        return opportunity_tickers

    def get_bb(self, opportunity_tickers:pd.DataFrame=None, window:int=None, window_dev:int=None) -> pd.DataFrame:

        bollinger = BollingerBands(close=opportunity_tickers["Close"], window=window, window_dev=window_dev)

        opportunity_tickers["bbhi" + str(window)] = bollinger.bollinger_hband_indicator()
        opportunity_tickers["bblo" + str(window)] = bollinger.bollinger_lband_indicator()
        
        return opportunity_tickers

    def get_stats(self, opportunity_tickers:pd.DataFrame=None) -> pd.DataFrame:

        try:
            for window in self.windows:

                self.get_sma(opportunity_tickers=opportunity_tickers, window=window)
                self.get_rsi(opportunity_tickers=opportunity_tickers, window=window)
                self.get_bb(opportunity_tickers=opportunity_tickers, window=window, window_dev=2)

            opportunity_tickers.reset_index(drop=True, inplace=True)

            return opportunity_tickers
        
        except KeyError:
            pass