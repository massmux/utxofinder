
import requests
import json
import sys

address_file = f"{sys.path[0]}/addresses.txt"


class UtxoFinder:



    def find(self,btc_address):
        url = "https://blockchain.info/unspent"
        response = requests.get(f"{url}?active={btc_address}")
        if response.status_code == 200:
            utxo_res = json.loads(response.text)['unspent_outputs']
            return utxo_res
        else:
            return []

    def utxo_count(self,btc_address):
        a = self.find(btc_address)
        return len(a)


