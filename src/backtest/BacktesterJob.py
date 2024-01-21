from src.strategies.Strategy import Strategy

from src.indicators.TechnicalIndicators import TechnicalIndicators

import pandas as pd

class BacktesterJob:

    def __init__(self, buy_job:callable=None, sell_job:callable=None, buy_signal:callable=None, sell_signal:callable=None) -> None:
        
        self.buy_job = buy_job or self.default_buy_job
        self.sell_job = sell_job or self.default_sell_job

        self.strategy = Strategy(buy_signal=buy_signal, sell_signal=sell_signal)

    def default_buy_it(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:

        indicators = TechnicalIndicators(windows=windows)

        op_stats = indicators.get_stats(opportunity)

        sma = op_stats["sma14"].iloc[-2]
        close = op_stats["Close"].iloc[-2]

        return self.strategy.buy_signal(sma=sma, prev_close=close)
    
    def default_buy_job(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:

        self.default_buy_it(windows, opportunity)

    def default_sell_it(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:
         
        indicators = TechnicalIndicators(windows=windows)

        op_stats = indicators.get_stats(opportunity)

        sma = op_stats["sma14"].iloc[-2]
        close = op_stats["Close"].iloc[-2]

        return self.strategy.sell_signal(sma=sma, prev_close=close)
    
    def default_sell_job(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:

        self.default_sell_it(windows, opportunity)