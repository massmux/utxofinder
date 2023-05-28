#!/usr/bin/env python3

"""
This example parse an addresses list and prints only addresses where at least 1 utxo is found
"""

import sys
from utxofinder import UtxoFinder


address_file = f"{sys.path[0]}/addresses.txt"

class LoadAddresses:
    def load(self,addresses_file):
        try:
            f = open(addresses_file)
            addresses = f.read().strip().split('\n')
            f.close()
            return addresses
        except:
            return False


if __name__ == '__main__':
    # retrieve addresses list
    addr = LoadAddresses()
    addresses = addr.load(address_file)

    # parse all addresses to find if some has unspent outputs
    for i in addresses:
        finder = UtxoFinder()
        n = finder.utxo_count(i)
        if n>0:
            # print how many utxo on this address
            print (f"{i} utxo: {n}")
