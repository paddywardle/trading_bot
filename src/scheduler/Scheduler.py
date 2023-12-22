from src.scheduler.Schedule import Schedule

from apscheduler.schedulers.blocking import BlockingScheduler

class Scheduler:

    def __init__(self, schedule:Schedule=None) -> None:

        self.scheduler = BlockingScheduler()
        self.schedule = schedule

    def add_job(self, trading_job:callable=None) -> None:

        self.scheduler.add_job(trading_job, 
                               trigger=self.schedule.trigger, 
                               day_of_week=self.schedule.day_of_week, 
                               hour=self.schedule.hour, 
                               minute=self.schedule.minute, 
                               start_date=self.schedule.start_date, 
                               timezone=self.schedule.timezone
                            )
        
    def start_job(self) -> None:

        self.scheduler.start()