import requests
from core.scripts.config import api_url
class Http():
    def __init__(self) -> None:
        self.session = requests.session()
        self.base_url = api_url

    def add_game(self, nick):
        self.session.post(self.base_url + 2)

    def get_started_game(self):
        pass