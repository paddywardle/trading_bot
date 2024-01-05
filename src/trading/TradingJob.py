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

from src.notification.SlackClient import SlackClient

import pandas as pd
from alpaca.trading.models import Position
import alpaca
import requests

class TradingJob:

    def __init__(self, buy_job:callable=None, sell_job:callable=None, buy_signal:callable=None, sell_signal:callable=None) -> None:
        self.strategy = Strategy(buy_signal=buy_signal, sell_signal=sell_signal)
        self.buy_job = buy_job or self.default_buy_job
        self.sell_job = sell_job or self.default_sell_job
        self.slack_client = SlackClient()
        self.trader = Trader()
        self.trader.authenticate()

    def default_buy_job(self, opportunities:Opportunities=None) -> None:

        market = Market()

        if market.is_market_open():
            for i, row in opportunities:
                self.default_buy_it(row)
        else:
            self.slack_client.send_message(f"{market.market_location} is not open")

    def default_buy_it(self, opportunity:pd.Series=None) -> None:

        op_stats = TechnicalIndicators(symbol=opportunity["Symbol"], period="1y")
        
        sma = op_stats.ticker_history["sma14"].iloc[-1]
        close = op_stats.ticker_history["Close"].iloc[-1]

        buy_bool = self.strategy.buy_signal(sma=sma, prev_close=close)
        
        if buy_bool:
            try:
                qty = 1
                mo = MarketOrder(stock=opportunity["Symbol"], quantity=qty, buy_or_sell="buy").create_market_order()
                submit = self.trader.submit_order(market_order=mo)
                self.slack_client.send_message(f"Bought: {opportunity['Symbol']}, Quantity: {qty}")
            except (requests.exceptions.HTTPError,alpaca.common.exceptions.APIError):
                self.slack_client.send_message(f"{opportunity['Symbol']} not active")

    def default_sell_job(self):

        market = Market()
        
        if market.is_market_open():
            positions = Positions()
        
            for i, pos in enumerate(positions):
                self.default_sell_it(pos)
        else:
            self.slack_client.send_message(f"{market.market_location} is not open")

    def default_sell_it(self, position:Position=None) -> None:

        op_stats = TechnicalIndicators(symbol=position.symbol, period="1y")

        sma = op_stats.ticker_history["sma14"].iloc[-1]
        close = op_stats.ticker_history["Close"].iloc[-1]

        sell_bool = self.strategy.sell_signal(sma=sma, prev_close=close)

        if sell_bool:
            mo = MarketOrder(stock=position.symbol, quantity=position.qty, buy_or_sell="sell").create_market_order()
            submit = self.trader.submit_order(market_order=mo)
            self.slack_client.send_message(f"Sold: {position.symbol}, Quantity: {position.qty}")