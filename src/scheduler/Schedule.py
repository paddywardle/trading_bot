from dataclasses import dataclass
from apscheduler.schedulers.blocking import BlockingScheduler

@dataclass
class Schedule:

    trigger:str
    day_of_week:str
    hour:str
    minute:str
    start_date:str
    timezone:str