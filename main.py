import requests
import time
import random

USERNAME = "Mrlove348"
DOGE_ADDRESS = "DU3vqZw4iXoh9eTqAtP48rYB6TRcb8jzvr"  # Replace this with your FaucetPay DOGE address

FAUCETS = [
    f"https://autofaucet.dutchycorp.space/?user={USERNAME}",
    f"https://autofaucet.org/?user={USERNAME}",
    f"https://claimfreecoins.io/dogecoin?address={DOGE_ADDRESS}",
    f"https://freeshibainu.com/?address={DOGE_ADDRESS}",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html",
}

def claim_faucet(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            print(f"SUCCESS: {url}")
        else:
            print(f"FAIL: {url} — Status: {r.status_code}")
    except Exception as e:
        print(f"ERROR on {url}: {str(e)}")

def run_cycle():
    random.shuffle(FAUCETS)
    for url in FAUCETS:
        claim_faucet(url)
        time.sleep(random.randint(10, 30))

if __name__ == "__main__":
    run_cycle()
