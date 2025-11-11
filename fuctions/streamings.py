from mastodon import Mastodon, StreamListener
from mastodon.return_types import Status
from ..utils.load_env import INSTANCE_URL, ACCESS_TOKEN, DEV

class Bot(StreamListener):
    def __init__(self, client: Mastodon):
        super().__init__()
        self.client = client

    def on_update(self, status: Status):
        if status.account.bot or status.reblog is not None:
            return
        
def login() -> Mastodon:
    client = Mastodon(
        client_secret = ACCESS_TOKEN,
        api_base_url = INSTANCE_URL
    )
    if DEV == "true":
        client.session.verify = False
    return client

def listen(client: Mastodon):
    client.stream_user(Bot(client))
