from src.opportunities.OpportunityTickers import OpportunityTickers

from src.indicators.TechnicalIndicators import TechnicalIndicators

import pandas as pd

class backtester:

    def __init__(self, symbol:str, buy_strategy:callable=None, sell_strategy: callable=None, period:str="1y", interval:str="1d") -> None:
        
        self.symbol = symbol # in the future could make this so it get the top losers on each day
        self.buy_strategy = buy_strategy
        self.sell_strategy = sell_strategy

        self.opportunity = OpportunityTickers(symbol=self.symbol, period=self.period, interval=self.interval)
        self.ticker_history:pd.DataFrame = self.opportunity.get_ticker_history()

    def run(self):

        for op in self.ticker_history.iterrows():
            pass
            # needs to calculate metrics
        
            # run buy job, add metadata of buy a dictionary, if buy skip the sell
            # then run sell job, add metadata of sell to a dictionary, calculate return, add to overall return
        
        # calculate backtesting stats