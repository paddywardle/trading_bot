from dataclasses import dataclass
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

@dataclass
class Schedule:

    trigger:str='cron'
    day_of_week:str='mon-fri'
    hour:str='00-23'
    minute:str='1,16,31,46'
    start_date:str=str(datetime.now())
    timezone:str='Europe/London'