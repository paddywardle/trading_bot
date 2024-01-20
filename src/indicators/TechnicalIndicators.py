import yfinance as yf
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import sma_indicator

class TechnicalIndicators:

    def __init__(self, symbol:str=None, period:str="1y", interval:str="1d", windows:list[int]=None, calc_stats:bool=True) -> None:

        self.symbol = symbol
        self.period = period
        self.interval = interval
        self.ticker = yf.Ticker(ticker=self.symbol)
        self.ticker_history = self.get_ticker_history()
        
        if calc_stats:
            self.get_stats(windows=windows or [14,30,50,200])

    def get_ticker_history(self) -> pd.DataFrame:

        return self.ticker.history(period=self.period, interval=self.interval)
    
    def get_sma(self, window:int=None) -> None:

        self.ticker_history["sma" + str(window)] = sma_indicator(close=self.ticker_history["Close"], window=window, fillna=False)

    def get_rsi(self, window:int=None) -> None:

        self.ticker_history["rsi" + str(window)] = RSIIndicator(close=self.ticker_history["Close"], window=window).rsi()

    def get_bb(self, window:int=None, window_dev:int=None) -> None:

        bollinger = BollingerBands(close=self.ticker_history["Close"], window=window, window_dev=window_dev)

        self.ticker_history["bbhi" + str(window)] = bollinger.bollinger_hband_indicator()
        self.ticker_history["bblo" + str(window)] = bollinger.bollinger_lband_indicator()

    def get_stats(self, windows:list[int]) -> None:

        try:
            for window in windows:

                self.get_sma(window=window)
                self.get_rsi(window=window)
                self.get_bb(window=window, window_dev=2)

            self.ticker_history.reset_index(drop=True, inplace=True)
        except KeyError:
            pass

    # def returns(self, days:int=None) -> None:
        
    #     self.ticker_history[str(days) + "_returns"] = 


