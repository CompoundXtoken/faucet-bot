import requests
from bs4 import BeautifulSoup
import time
import random

FAUCET_URLS = [
    "https://autofaucet.dutchycorp.space/faucet.php",
    "https://claimfreecoins.io/dogecoin",
    "https://freeshibainu.com",
    "https://faucet.bitcoinhub.org",
    "https://pipeflare.io",
    "https://autofaucet.org",
    "https://claimbtc.cc",
    "https://coinpayu.com",
    "https://cryptofaucet.com",
    "https://faucetcrypto.com"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

def claim_faucet(url):
    try:
        res = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")
        print(f"[OK] {url} - {res.status_code}")
        return True
    except Exception as e:
        print(f"[ERR] {url} - {e}")
        return False

def run():
    print("Starting faucet bot...")
    for url in FAUCET_URLS:
        success = claim_faucet(url)
        time.sleep(random.randint(5, 15))  # mimic human delay
    print("Cycle complete.")

if __name__ == "__main__":
    run()
