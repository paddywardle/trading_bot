from src.alpaca_interaction.AlpacaKeys import AlpacaKeys
from src.alpaca_interaction.MarketOrder import MarketOrder
from src.alpaca_interaction.Trader import Trader
from src.alpaca_interaction.Market import Market

from src.strategies.Strategy import Strategy

from src.opportunities.Opportunities import Opportunities
from src.opportunities.OpportunitiesStats import OpportunitiesStats
from src.opportunities.OpportunitiesURL import OpportunitiesURL

from src.indicators.TechnicalIndicators import TechnicalIndicators

from src.positions.Positions import Positions

import pandas as pd
from alpaca.trading.models import Position

class TradingJob:

    def __init__(self, buy_job:callable=None, sell_job:callable=None, buy_signal:callable=None, sell_signal:callable=None) -> None:

        self.strategy = Strategy(buy_signal=buy_signal, sell_signal=sell_signal)
        self.buy_job = buy_job or self.default_buy_job
        self.sell_job = sell_job or self.default_sell_job

    def default_buy_job(self, opportunities:Opportunities=None) -> None:

        market = Market()
        
        if market.is_market_open():
            for i, row in opportunities:
                self.default_buy_it(row)
        else:
            print(f"{market.market_location} is not open")

    def default_buy_it(self, opportunity:pd.Series=None) -> None:

        op_stats = TechnicalIndicators(symbol=opportunity["Symbol"], period="2d", calc_stats=False)

        open_cur = op_stats.ticker_history["Open"].iloc[1]
        close_cur = op_stats.ticker_history["Close"].iloc[1]
        open_prev = op_stats.ticker_history["Open"].iloc[0]
        close_prev = op_stats.ticker_history["Close"].iloc[0]

        buy_bool = self.strategy.buy_signal(open=open_cur, close=close_cur, previous_open=open_prev, previous_close=close_prev)

        if buy_bool:
            mo = MarketOrder(stock=opportunity["Symbol"], quantity=1, buy_or_sell="buy").create_market_order()
            submit = Trader().submit_order(market_order=mo)

    def default_sell_job(self):

        market = Market()
        
        if market.is_market_open():
            positions = Positions()
        
            for i, pos in enumerate(positions):
                self.default_sell_it(pos)
        else:
            print(f"{market.market_location} is not open")


    def default_sell_it(self, position:Position=None) -> None:

        op_stats = TechnicalIndicators(symbol=position.symbol, period="2d", calc_stats=False)

        open_cur = op_stats.ticker_history["Open"].iloc[1]
        close_cur = op_stats.ticker_history["Close"].iloc[1]
        open_prev = op_stats.ticker_history["Open"].iloc[0]
        close_prev = op_stats.ticker_history["Close"].iloc[0]

        sell_bool = self.strategy.sell_signal(open=open_cur, close=close_cur, previous_open=open_prev, previous_close=close_prev)

        print(sell_bool)

        # if sell_bool:
        #     mo = MarketOrder(stock=position.symbol, quantity=position.qty, buy_or_sell="sell").create_market_order()
        #     submit = Trader().submit_order(market_order=mo)


            

