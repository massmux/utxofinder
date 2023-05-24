#!/usr/bin/env python3

import requests
import json

class UtxoFinder:

    def find(self, btc_address):
        response = requests.get('https://blockchain.info/unspent?active=' + btc_address)
        if response.status_code == 200:
            utxo_res = json.loads(response.text)['unspent_outputs']
            return utxo_res
        else:
            return None


if __name__ == '__main__':
    btc_address = 'bc1q3crq5xy53n6zhdwa70uqv8hu70aww7hmh3wgxh'
    finder = UtxoFinder()
    utxo_res = finder.find(btc_address)
    
    for utxo in utxo_res:
        print(utxo)