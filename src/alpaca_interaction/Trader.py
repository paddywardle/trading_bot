from src.alpaca_interaction.AlpacaKeys import AlpacaKeys
from src.alpaca_interaction.MarketOrder import MarketOrder

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.models import TradeAccount
from alpaca.trading.requests import CancelOrderResponse
from alpaca.trading.models import Position

class Trader:

    def __init__(self, paper=True) -> None:
        self.paper = paper
        self.alpaca_keys = AlpacaKeys()
        self.trading_client = None

    def authenticate(self) -> None:

        self.trading_client = TradingClient(api_key=self.alpaca_keys.api_key, secret_key=self.alpaca_keys.secret_key, paper=self.paper)

    def get_account(self) -> TradeAccount:
        return self.trading_client.get_account()
    
    def get_all_assets(self, asset_type:AssetClass=None) -> list[AssetClass]:

        if asset_type:
            search_params = GetAssetsRequest(asset_class=asset_type)
            return self.trading_client.get_all_assets(search_params)
        return self.trading_client.get_all_assets()
    
    def get_all_positions(self) -> list[Position]:

        return self.trading_client.get_all_positions()
    
    def submit_order(self, market_order:MarketOrder=None) -> None:

        self.trading_client.submit_order(order_data=market_order)

    def cancel_order(self) -> list[CancelOrderResponse]:

        return self.trading_client.cancel_orders()