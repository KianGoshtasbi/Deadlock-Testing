import argparse
import pandas as pd
import numpy as np
import requests
import json
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
import warnings
import json
from collections import defaultdict
BASE_URL = {
    'game': 'https://api.deadlock-api.com',
    'assets': 'https://assets.deadlock-api.com'
}

def get_data(url,params=None):
    trys = 5
    print(f"[INFO] Fetching data from {url}")
    for i in range(trys):
        try:
            response = requests.get(url,params=params)
            response.raise_for_status()
            data = response.json()
            print(f"[SUCCESS] Data recieved from {url}!")
            return data
        except requests.exceptions.RequestException as z:
            if (i == trys - 1):
                print(f"[ERROR] All {trys} requests have failed, aborting")
                return None
            print(f"[WARNING] Request failed {z}, trying again")
    return None

def main():
    item_data = get_data(f"{BASE_URL['game']}/v1/analytics/item-stats")
    
    with open('item_data.json', 'w') as f:
        json.dump(item_data, f, indent=2)
    
    with open('item_data.json','r') as f:
        id_data = json.load(f)
    
    item_ids = [entry['item_id'] for entry in id_data]
    item_wins = [entry['wins'] for entry in id_data]
    item_losses = [entry['losses'] for entry in id_data]
    item_matches = [entry['matches'] for entry in id_data]
    item_players = [entry['players'] for entry in id_data]
  

    item_dict = defaultdict(list)
    # Getting specific info I want for an item and adding it to dictionary
    
    for i in range(len(item_ids)):
        x = item_ids[i]
        item_data = get_data(f"{BASE_URL['assets']}/v2/items/{x}")
        item_name = item_data['name']
        item_cost = item_data['cost']
        item_tier = item_data['item_tier']
        item_dict[x].append(item_name)
        item_dict[x].append(item_cost)
        item_dict[x].append(item_tier)
        item_dict[x].append(item_wins[i])
        item_dict[x].append(item_losses[i])
        item_dict[x].append(item_matches[i])
        item_dict[x].append(item_players[i])
    
    with open('item_attributes.json', 'w') as f:
        json.dump(dict(item_dict), f, indent=2)
    #ID: NAME | COST | TIER | WINS | LOSSES | MATCHES | PLAYERS
        
    

    




if __name__ == "__main__":
    main()



