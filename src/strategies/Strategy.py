class Strategy:

    def __init__(self, buy_signal:callable=None, sell_signal:callable=None) -> None:

        self.buy_signal = buy_signal or self.default_buy_signal
        self.sell_signal = sell_signal or self.default_sell_signal

    def default_buy_signal(self,open,close,previous_open,previous_close) -> bool:

        # return True if buy, False if not
        if (open<close and previous_open>previous_close and close>previous_open and open<=previous_close):
            return True
        return False

    def default_sell_signal(self,open,close,previous_open,previous_close) -> bool:
        
        # return True if buy, False if not
        if (open>close and previous_open<previous_close and close<previous_open and open>=previous_close):
            return True
        return False

    