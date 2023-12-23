from dataclasses import dataclass

@dataclass
class OpportunitiesURL:

    sec_type:str
    sec_num:str
    url:str=f"https://finance.yahoo.com/"

    def build_url(self) -> str:

        if self.sec_type.lower() == "stocks":
            self.url += "losers?"
        if self.sec_type.lower() == "crypto":
            self.url += "crypto?"

        if self.sec_num < 100:
            self.url += "count={self.sec_num}"
        else:
            self.url += "offset={}&count=100"

        return self.url