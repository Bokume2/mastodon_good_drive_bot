from mastodon import Mastodon
from mastodon.return_types import Status
import uuid
from bs4 import BeautifulSoup
import html
import re
import random

def remove_html_tag(text: str, doRet: bool = True):
    if doRet:
        text = text.replace("</p><p>", "\n\n")
        text = text.replace("<br */>", "\n")
    else:
        text = text.replace("</p><p>", " ")
        text = text.replace("<br */>", " ")
    
    return html.unescape(BeautifulSoup(text, "html.parser").get_text())

def yell(client: Mastodon, status: Status):
    content = remove_html_tag(status.content)
    uuid_value = uuid.uuid4()
    yell_voices = ["いってらっしゃい！", "ご安全に！", "Have a good drive!"]
    actual_yell_voices = []
    if re.search(r"(行|い)って(き|来)ます", content):
        actual_yell_voices.append(yell_voices[0])
    if "ご安全に" in content:
        actual_yell_voices.append(yell_voices[1])
    if len(actual_yell_voices) == 0:
        actual_yell_voices = yell_voices
    yell_voice = random.choice(actual_yell_voices)
    reply_content = f"\n\n{uuid_value}\n\n{yell_voice}"
    client.status_reply(status, reply_content)
