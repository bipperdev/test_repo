import requests
from bs4 import BeautifulSoup
import hashlib
import time

URLS = [
    "",
    ""
]

CHECK_INTERVAL = 180  # 3 minut
BOT_TOKEN = ""
CHAT_ID = ""
# ======================

headers = {
    "User-Agent": "Mozilla/5.0",
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


def get_hash(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.get_text()
        return hashlib.md5(content.encode()).hexdigest()
    except:
        return None


print("Monitoring started...")


last_hashes = {}

for url in URLS:
    last_hashes[url] = get_hash(url)

while True:
    time.sleep(CHECK_INTERVAL)

    for url in URLS:
        new_hash = get_hash(url)
        if new_hash is None:
            continue

        if new_hash != last_hashes[url]:
            print(f" CHANGE DETECTED!!!!!!!: {url}")
            send_telegram(f" Website changed:\n{url}")
            last_hashes[url] = new_hash
        else:
            print(f"No change: {url}")
