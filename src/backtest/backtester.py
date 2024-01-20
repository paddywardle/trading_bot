from src.strategies.Strategy import Strategy

from src.opportunities.OpportunityTickers import OpportunityTickers

from src.indicators.TechnicalIndicators import TechnicalIndicators

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pandas as pd
import yfinance as yf

class Backtester:

    def __init__(self, symbol:str, 
                 buy_signal:callable=None, 
                 sell_signal: callable=None, 
                 buy_strategy: callable=None,
                 sell_strategy: callable=None,
                 period:str="1y", 
                 interval:str="1d") -> None:
        
        self.symbol = symbol # in the future could make this so it get the top losers on each day

        self.strategy = Strategy(buy_signal=buy_signal, sell_signal=sell_signal)
        self.buy_strategy = self.default_buy or buy_strategy
        self.sell_strategy = self.default_sell or sell_strategy

        self.period = period
        self.interval = interval

        self.positions:dict[datetime, dict] = {}

    def default_buy(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:

        indicators = TechnicalIndicators(windows=windows)

        op_stats = indicators.get_stats(opportunity)

        sma = op_stats["sma14"].iloc[-2]
        close = op_stats["Close"].iloc[-2]

        return self.strategy.buy_signal(sma=sma, prev_close=close)

    def default_sell(self, windows:list[str]=None, opportunity:pd.Series=None) -> bool:
         
        indicators = TechnicalIndicators(windows=windows)

        op_stats = indicators.get_stats(opportunity)

        sma = op_stats["sma14"].iloc[-2]
        close = op_stats["Close"].iloc[-2]

        return self.strategy.sell_signal(sma=sma, prev_close=close)

    def run(self, start_date:datetime=None, end_date:datetime=None):

            current_date = start_date
            ticker = yf.Ticker(ticker=self.symbol)

            while (current_date <= end_date):

                # get adjusted start date
                current_start_date = current_date - relativedelta(years=1)

                op = ticker.history(start=current_start_date, end=current_date+timedelta(days=1), interval=self.interval)

                buy_bool = self.buy_strategy(opportunity=op)
            
                if buy_bool:
                    self.positions[current_date] = {
                        "buy_price": (op["Low"][-1]+op["High"][-1])/2,
                        "qty": 1
                    }

                sell_bool = self.sell_strategy(opportunity=op)

                if sell_bool:
                    pass
                    # sell all in positions and add to returns object

                # assume you buy at the average of high and low
                # add a day to the current date

                current_date += timedelta(days=1)
                break

            # needs to calculate metrics
        
            # run buy job, add metadata of buy a dictionary, if buy skip the sell
            # then run sell job, add metadata of sell to a dictionary, calculate return, add to overall return
        
        # calculate backtesting stats