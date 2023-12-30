from src.scheduler.Schedule import CronSchedule, IntervalSchedule

from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler:

    def __init__(self) -> None:

        self.scheduler = BackgroundScheduler()

    def add_cron_job(self, trading_job:callable=None, schedule:CronSchedule=None, args:list=None) -> None:

        if args is not None:
            self.scheduler.add_job(trading_job, 
                                trigger=schedule.trigger, 
                                day_of_week=schedule.day_of_week, 
                                hour=schedule.hour, 
                                minute=schedule.minute, 
                                start_date=schedule.start_date,
                                timezone=schedule.timezone,
                                args=args
                                )
        else:
            self.scheduler.add_job(trading_job, 
                                trigger=schedule.trigger, 
                                day_of_week=schedule.day_of_week, 
                                hour=schedule.hour, 
                                minute=schedule.minute, 
                                start_date=schedule.start_date,
                                timezone=schedule.timezone
                                )
            
    def add_interval_job(self, trading_job:callable=None, schedule:IntervalSchedule=None, args:list=None) -> None:

        if args is not None:
            self.scheduler.add_job(trading_job, 
                                trigger=schedule.trigger, 
                                minutes=schedule.minutes, 
                                start_date=schedule.start_date,
                                timezone=schedule.timezone,
                                args=args
                                )
        else:
            self.scheduler.add_job(trading_job, 
                                trigger=schedule.trigger, 
                                minutes=schedule.minutes, 
                                start_date=schedule.start_date,
                                timezone=schedule.timezone
                                )
        
    def start_job(self) -> None:

        self.scheduler.start()

    def end_job(self) -> None:

        self.scheduler.shutdown()