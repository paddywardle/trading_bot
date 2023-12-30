from dataclasses import dataclass
from datetime import datetime

@dataclass
class CronSchedule:

    trigger:str='cron'
    day_of_week:str='mon-fri'
    hour:str='00-23'
    minute:str='1,16,31,46'
    start_date:str=str(datetime.now())
    timezone:str='Europe/London'

@dataclass
class IntervalSchedule:

    trigger: str = 'interval'
    minutes: int = 1  # Set your desired interval in minutes
    start_date: str = str(datetime.now())
    timezone: str = 'Europe/London'