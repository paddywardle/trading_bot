from src.requests.HTTPRequests import HTTPRequests
from src.opportunities.OpportunitiesURL import OpportunitiesURL

import yfinance as yf
import pandas as pd

class Opportunities:

    def __init__(self, opportunity:OpportunitiesURL=None) -> None:

        self.http_request = HTTPRequests()
        self.opportunities = self.get_opportunities(opportunity=opportunity)

    def __iter__(self):

        return self.opportunities.iterrows()
    
    def __len__(self):

        return len(self.opportunities)

    def get_raw_info(self, url:str=None):

        response = self.http_request.get(url)

        tables = pd.read_html(response.html.raw_html)

        df_raw = tables[0].copy()

        df_raw.columns = tables[0].columns

        return df_raw
    
    def get_opportunities(self, opportunity:OpportunitiesURL=None) -> pd.DataFrame:

        df_historical = []
        offset=0
        url = opportunity.build_url()

        # change this to aysnchronous
        while True:
            df_raw = self.get_raw_info(url.format(offset))

            if offset >= opportunity.sec_num or df_raw.empty:
                break

            df_historical.append(df_raw)
            offset += 100

        self.http_request.close_session()
        
        df_historical = pd.concat(df_historical)
        df_historical["asset_type"] = opportunity.sec_type

        return df_historical






