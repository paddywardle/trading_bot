from src.backtest.Backtester import Backtester
import yfinance as yf

from datetime import datetime

if __name__ == "__main__":

    back = Backtester(symbols=["AAPL"])
    
    start_date = datetime(2023,11,1)
    end_date = datetime(2023, 12, 1)

    back.run(start_date=start_date, end_date=end_date)