import requests_html as req_html
import requests as req

class HTTPRequests():

    def __init__(self):
        self.session = req_html.HTMLSession()

    def get(self, url: str, **kwargs) -> req.Response:

        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response

    def put(self, url: str, **kwargs) -> req.Response:

        try:
            response = self.session.put(url, **kwargs)
            response.raise_for_status()
            return response
        except req.exceptions.HTTPError as errh:
            print(errh)
        except req.exceptions.ConnectionError as errc:
            print(errc)
        except req.exceptions.Timeout as errt:
            print(errt)
        except req.exceptions.RequestException as err:
            print(err)
        except:
            print("Other error")

    @staticmethod
    def post(url: str, **kwargs) -> req.Response:

        try:
            response = req.post(url, **kwargs)
            response.raise_for_status()
            return response
        except req.exceptions.HTTPError as errh:
            print(errh)
        except req.exceptions.ConnectionError as errc:
            print(errc)
        except req.exceptions.Timeout as errt:
            print(errt)
        except req.exceptions.RequestException as err:
            print(err)
        except:
            print("Other error")

    def close_session(self) -> None:

        self.session.close()