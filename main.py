from trading.TradingJob import TradingJob
from opportunities.Opportunities import Opportunities
from opportunities.OpportunitiesURL import OpportunitiesURL
from scheduler.Schedule import IntervalSchedule
from scheduler.Scheduler import Scheduler

import time

if __name__ == "__main__":

    schedule = IntervalSchedule()

    scheduler1 = Scheduler()
    scheduler2 = Scheduler()

    opportunties_url = OpportunitiesURL(sec_type="stocks", sec_num=200)
    opportunties = Opportunities(opportunties_url)
    
    trading_job = TradingJob()

    scheduler1.add_interval_job(trading_job=trading_job.buy_job, schedule=schedule, args=[opportunties])

    scheduler2.add_interval_job(trading_job=trading_job.sell_job, schedule=schedule)

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler1.shutdown()
        scheduler2.shutdown()