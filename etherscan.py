import requests
import pandas as pd
from tqdm import tqdm

API_KEY = "YourEtherscanAPIKey"

def get_transactions(address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    if data["status"] != "1":
        return None
    df = pd.DataFrame(data["result"])
    df["timeStamp"] = pd.to_datetime(df["timeStamp"].astype(int), unit="s")
    return df
