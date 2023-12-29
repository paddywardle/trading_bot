from src.alpaca_interaction.Trader import Trader
from src.indicators.TechnicalIndicators import TechnicalIndicators

from alpaca.trading.models import Position
from dataclasses import dataclass, field

@dataclass
class Positions:

    positions:list[Position]=field(default_factory=list)
    symbols:list[str]=field(default_factory=list)

    def __post_init__(self):
        trader = Trader()
        trader.authenticate()
        self.positions = trader.get_all_positions()
        self.symbols = [pos.symbol for pos in self.positions]

    def __iter__(self):
        return iter(self.positions)