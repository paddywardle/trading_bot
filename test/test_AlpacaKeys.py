from trading.AlpacaKeys import AlpacaKeys

def test_check_key_types():
    keys = AlpacaKeys()
    assert keys.api_key != None
    assert keys.secret_key != None