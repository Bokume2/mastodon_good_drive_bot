from mastodon import Mastodon
from mastodon.return_types import Status
import uuid
from bs4 import BeautifulSoup
import html
import re

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
