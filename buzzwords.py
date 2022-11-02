import requests
from bs4 import BeautifulSoup

GOOGLE_API_KEY = "https://docs.googleapis.com/v1/documents/1OevE4HFiAgUPlOym3RAPjtvpk1zIurOKdTdrUFoyS28"

class BuzzWordGetter:
    def collect(self,url):
        dat = requests.get(GOOGLE_API_KEY).text
        __import__("ipdb").set_trace()
        soup = BeautifulSoup(dat,"html.parser")
        soup.find_all("DOCS_modelChunk")
        return "random str"
