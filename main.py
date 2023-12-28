from trading.AlpacaKeys import AlpacaKeys

from src.opportunities.Opportunities import Opportunities
from src.opportunities.OpportunitiesURL import OpportunitiesURL
from src.indicators.TechnicalIndicators import TechnicalIndicators
from src.trading.TradingJob import TradingJob

if __name__ == "__main__":

    opportunity = OpportunitiesURL(sec_type="stocks", sec_num=200)
    opportunities = Opportunities(opportunity)
    trading_job = TradingJob()
    trading_job.buy_job(opportunities.opportunities)