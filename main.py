from trading.TradingJob import TradingJob
from opportunities.Opportunities import Opportunities
from opportunities.OpportunitiesURL import OpportunitiesURL
from indicators.TechnicalIndicators import TechnicalIndicators

import time

if __name__ == "__main__":

    opportunties_url = OpportunitiesURL(sec_type="stocks", sec_num=200)
    opportunties = Opportunities(opportunties_url)

    trading_job = TradingJob()

    while True:

        trading_job.buy_job(opportunities=opportunties)
        trading_job.sell_job()

        time.sleep(60)