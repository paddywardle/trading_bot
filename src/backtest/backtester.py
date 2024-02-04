from src.backtest.BacktesterJob import BacktesterJob

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pandas as pd
import yfinance as yf

class Backtester:

    def __init__(self, symbols:list[str], 
                 buy_signal:callable=None, 
                 sell_signal: callable=None, 
                 buy_job: callable=None,
                 sell_job: callable=None,
                 period:str="1y", 
                 interval:str="1d",
                 current_positions:dict[str,dict]=None) -> None:
        
        self.symbols:list[str] = symbols # in the future could make this so it get the top losers on each day
        self.period:str = period
        self.interval:str = interval

        self.trading_job:BacktesterJob = BacktesterJob(buy_job=buy_job,
                                        sell_job=sell_job,
                                        buy_signal=buy_signal,
                                        sell_signal=sell_signal)

        self.positions:dict[str, dict] = current_positions or {} # if we have current positions at the start
        self.sales: dict[str, dict] = {}
        self.ticker_data = None
    
    def sell_order(self, current_date:datetime, op:pd.Series) -> None:

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
    
    def buy_order(self, current_date:datetime, op:pd.Series) -> None:
        
        # assume we buy at the average price of the day
        self.positions[self.symbol + " " + current_date.strftime('%Y-%m-%d')] = {
            "buy_date": current_date,
            "buy_price": (op["Low"].iloc[-1]+op["High"].iloc[-1])/2,
            "qty": 1
        }

    def get_ticker_data(self, start_date:datetime=None, end_date:datetime=None) -> None:

        if len(self.symbols) > 1:
            ticker_dfs = []

            for symbol in self.symbols:
                # - timedelta(years=1) would need to reflect the self.period
                ticker_history = yf.Ticker(ticker=symbol).history(start=start_date-relativedelta(years=1), end=end_date+timedelta(days=1), interval=self.interval).reset_index()

                ticker_history["symbol"] = symbol

                ticker_dfs.append(ticker_dfs)
            
            self.ticker_data = pd.concat(ticker_dfs)
        else:
            ticker_history = yf.Ticker(ticker=self.symbols[0]).history(start=start_date-relativedelta(years=1), end=end_date+timedelta(days=1), interval=self.interval).reset_index()

            ticker_history["symbol"] = self.symbols[0]

            self.ticker_data = ticker_history

    def run(self, start_date:datetime=None, end_date:datetime=None) -> None:
            
            self.get_ticker_data(start_date=start_date, end_date=end_date)

            current_date = start_date

            while (current_date <= end_date):

                self.run_it(current_date)

                current_date += timedelta(days=1)

    def run_it(self, current_date:datetime=None) -> None:

        prev_year = current_date - relativedelta(years=1)

        # so theres an issue here between timezone date formats
        current_period_tickers = self.ticker_data[(self.ticker_data["Date"] >= prev_year) and (self.ticker_data["Date"] <= current_date+timedelta(days=1))]

        for symbol in self.symbols:
            
            op = current_period_tickers[current_period_tickers["symbol"] == symbol]

            buy_bool = self.trading_job.buy_job(opportunity=op)

            if buy_bool:
                self.buy_order(current_date=current_date, op=op.iloc[-1,:])

            sell_bool = self.trading_job.sell_job(opportunity=op)

            if sell_bool:
                self.sell_order(current_date=current_date, op=op.iloc[-1,:])

            # then have an object that take the current positions and the sell orders at the end of the sim and calculates the metrics

            # needs to calculate metrics
        
            # run buy job, add metadata of buy a dictionary, if buy skip the sell
            # then run sell job, add metadata of sell to a dictionary, calculate return, add to overall return
        
        # calculate backtesting stats
        #with ThreadPoolExecutor() as executor:
        #executor.map(get_stats, ticker_list) https://stackoverflow.com/questions/71161902/get-info-on-multiple-stock-tickers-quickly-using-yfinance