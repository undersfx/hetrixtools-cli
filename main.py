#!/usr/bin/env python3

from argparse import ArgumentParser
from selenium import webdriver
from pprint import pprint
import blacklist
import monitors
import delist
import json

# Parser config
parser = ArgumentParser(
    prog='rbl',
    description='Tools to maintain my sanity',)

parser.add_argument('-u', action='store_true',
                    help='update cache file')

parser.add_argument('-c', action='store_true',
                    help='count blacklisted ips')

parser.add_argument('-l', action='store_true',
                    help='list all ips blacklisted and its blacklist') # TODO

parser.add_argument('--dnsrbl', action='store_true',
                    help='run the delist process for dnsrbl.org')

def main():
    args = parser.parse_args()

    def load_cache():
        '''Load the cache file from disk'''

        with open('cached_data.json', 'r') as f:
            ips = json.load(f)
            print('Cached data found, using the file.')
            return ips

    def update_cache(ips):
        '''Write a new cache file in disk'''

        with open('cached_data.json', 'w') as f:
            json.dump(ips, f)
            print('New cache saved')

    if args.u:
        # Force cache file to be updated
        ips = monitors.get_data()
        update_cache(ips)
    else:
        # Try to load a existing cache file
        try:
            ips = load_cache()
        except FileNotFoundError:
            ips = monitors.get_data()
            update_cache(ips)

    # Print the blacklist count
    if args.c:
        bl_count = blacklist.count(ips)
        pprint(sorted(bl_count.items(), key=lambda x: x[1], reverse=True))

    # Identify and run dnsbl.org script of delist
    if args.dnsrbl:
        blacklisted = blacklist.find_blocked(ips, 'dnsrbl.org')
        if blacklisted: delist.dnsrbl(blacklisted)

    print('Finished!')

if __name__ == "__main__":
    main()