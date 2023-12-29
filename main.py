from src.alpaca_interaction.Market import Market
from src.alpaca_interaction.Trader import Trader

from src.opportunities.Opportunities import Opportunities
from src.opportunities.OpportunitiesURL import OpportunitiesURL
from src.indicators.TechnicalIndicators import TechnicalIndicators
from src.trading.TradingJob import TradingJob
from src.positions.Positions import Positions

if __name__ == "__main__":
    
    # opportunity = OpportunitiesURL(sec_type="stocks", sec_num=200)
    # opportunities = Opportunities(opportunity)
    trading_job = TradingJob()
    trading_job.sell_job()