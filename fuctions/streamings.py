from mastodon import Mastodon, StreamListener
from mastodon.return_types import Notification, Status
from utils.load_env import INSTANCE_URL, ACCESS_TOKEN, DEV
from .functions import yell

class Bot(StreamListener):
    effective_notification_types = (
        "mention",
        "follow"
    )

    def __init__(self, client: Mastodon):
        super().__init__()
        self.client = client

    def on_notification(self, notification: Notification):
        if notification.account.bot or notification.type not in self.effective_notification_types:
            return
        
        if notification.type == "follow":
            self.client.account_follow(notification.account)
        elif notification.type == "mention":
            status: Status = notification.status
            
            if status.reblog is not None:
                return
            
            yell(self.client, status)
        
def login() -> Mastodon:
    client = Mastodon(
        access_token = ACCESS_TOKEN,
        api_base_url = INSTANCE_URL
    )
    if DEV == "true":
        client.session.verify = False
    return client

def listen(client: Mastodon):
    client.stream_user(Bot(client))
