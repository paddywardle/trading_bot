from src.trading.AlpacaKeys import AlpacaKeys

def test_check_key_types():
    keys = AlpacaKeys()
    print(AlpacaKeys)
    assert keys["ALPACA_API_KEY"] != None
    assert keys["ALPACA_SECRET"] != None