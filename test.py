from datetime import datetime, timedelta
from src.backtest.backtester import backtester

if __name__ == "__main__":

    back = backtester("AAPL")

    start_date = datetime(2023, 11, 1)
    end_date = datetime(2024, 1, 20)

    back.run(start_date=start_date, end_date=end_date)