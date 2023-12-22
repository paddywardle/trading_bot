from src.trading.TradingClient import Trader
from src.trading.MarketOrder import MarketOrder
# from src.scheduler.Schedule import Schedule

from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

if __name__ == "__main__":

    trader = Trader()
    # trader.authenticate()

    # market_order = MarketOrder(
    #     stock="SPY",
    #     quantity=0.023,
    #     buy_or_sell=OrderSide.BUY,
    #     time_in_force=TimeInForce.DAY
    # ).create_market_order()

    # trader.submit_order(market_order)


