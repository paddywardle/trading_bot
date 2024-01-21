from src.backtest.BacktesterJob import BacktesterJob

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pandas as pd
import yfinance as yf

class Backtester:

    def __init__(self, symbol:str, 
                 buy_signal:callable=None, 
                 sell_signal: callable=None, 
                 buy_job: callable=None,
                 sell_job: callable=None,
                 period:str="1y", 
                 interval:str="1d") -> None:
        
        self.symbol = symbol # in the future could make this so it get the top losers on each day
        self.period = period
        self.interval = interval

        self.trading_job = BacktesterJob(buy_job=buy_job,
                                        sell_job=sell_job,
                                        buy_signal=buy_signal,
                                        sell_signal=sell_signal)

        self.positions:dict[str, dict] = {}
        self.sales: dict[str, dict] = {}
    
    def sell_order(self, current_date:datetime, op:pd.Series):

        # assume we sell at the average of the day
        sell_price = (op["Low"]+op["High"])/2
        # sell all current positions of the stocks

        for key, val in self.positions.items():
                
            self.sales[self.symbol + " " + current_date.strftime('%Y-%m-%d')] = {
                "buy_date": val["buy_date"],
                "sell_date": current_date,
                "qty": key["qty"],
                "buy_price": val["buy_price"],
                "sell_price": sell_price,
                "price_difference_per_share": (sell_price - val["buy_price"]),
                "position_profit_loss": (sell_price - val["buy_price"]) * key["qty"]
            }

            self.positions.pop(key, None)
    
    def buy_order(self, current_date:datetime, op:pd.Series):
        
        # assume we buy at the average price of the day
        self.positions[self.symbol + " " + current_date.strftime('%Y-%m-%d')] = {
            "buy_date": current_date,
            "buy_price": (op["Low"].iloc[-1]+op["High"].iloc[-1])/2,
            "qty": 1
        }

    def run(self, start_date:datetime=None, end_date:datetime=None):

            current_date = start_date
            ticker = yf.Ticker(ticker=self.symbol)

            while (current_date <= end_date):

                # get adjusted start date
                current_start_date = current_date - relativedelta(years=1)

                op = ticker.history(start=current_start_date, end=current_date+timedelta(days=1), interval=self.interval)

                buy_bool = self.trading_job.buy_job(opportunity=op)

                if buy_bool:
                    self.buy_order(current_date=current_date, op=op.iloc[-1,:])

                sell_bool = self.trading_job.sell_job(opportunity=op)

                if sell_bool:
                    self.sell_order(current_date=current_date, op=op.iloc[-1,:])

                current_date += timedelta(days=1)

            # then have an object that take the current positions and the sell orders at the end of the sim and calculates the metrics

            # needs to calculate metrics
        
            # run buy job, add metadata of buy a dictionary, if buy skip the sell
            # then run sell job, add metadata of sell to a dictionary, calculate return, add to overall return
        
        # calculate backtesting stats