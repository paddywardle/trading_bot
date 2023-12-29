import pandas_market_calendars as pd_mcal
import pytz
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

class Market:

    def __init__(self) -> None:
        load_dotenv("config/.env")
        self.market_location = os.getenv("MARKET_LOCATION")
        self.market_calendar = os.getenv("MARKET_CALENDAR")

    def is_market_open(self) -> bool:
        
        timezone = pytz.timezone(zone=self.market_location)
        time_now = datetime.now(tz=timezone)
        loc_calendar = pd_mcal.get_calendar(name=self.market_calendar)
        market_sched = loc_calendar.schedule(start_date=time_now.date(), end_date=time_now.date())

        if not market_sched.empty:

            market_open = market_sched.iloc[0]["market_open"].to_pydatetime().replace(tzinfo=None)
            market_close = market_sched.iloc[0]["market_close"].to_pydatetime().replace(tzinfo=None)
            time_now_no_tz = time_now.replace(tzinfo=None)

            if (market_open <= time_now_no_tz) and (time_now_no_tz < market_close):
                return True
            
        return False