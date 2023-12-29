from trading.TradingJob import TradingJob
from opportunities.Opportunities import Opportunities
from opportunities.OpportunitiesURL import OpportunitiesURL
from scheduler.Schedule import Schedule
from scheduler.Scheduler import Scheduler

if __name__ == "__main__":
    
    opportunties_url = OpportunitiesURL(sec_type="stocks", sec_num=200)
    opportunties = Opportunities(opportunties_url)
    
    trading_job = TradingJob()
    
    trading_job.buy_job(opportunties)

    trading_job.sell_job()