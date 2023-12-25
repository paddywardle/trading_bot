from trading.AlpacaKeys import AlpacaKeys

from src.Opportunities.Opportunities import Opportunities
from src.Opportunities.OpportunitiesURL import OpportunitiesURL
from src.Opportunities.Opportunity import Opportunity


from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

if __name__ == "__main__":

    # trader = Trader()
    # trader.authenticate()

    # market_order = MarketOrder(
    #     stock="SPY",
    #     quantity=0.023,
    #     buy_or_sell=OrderSide.BUY,
    #     time_in_force=TimeInForce.DAY
    # ).create_market_order()

    # trader.submit_order(market_order)

    opportunity = OpportunitiesURL(sec_type="stocks", sec_num=200)
    # print(opportunity.build_url())
    opportunities = Opportunities(opportunity)
    # print(opportunities.opportunities["Symbol"][0])
    op_stat = Opportunity(symbol=opportunities.opportunities["Symbol"][0])
    print(op_stat.ticker_history)