#!/usr/bin/env python3
# By @undersfx

'''
Command line interface with tools to parse and analyze data from Hetrixtools API.
'''

from argparse import ArgumentParser
from pprint import pprint
import blacklist
import monitors
import delist
import json
import os

# Enviroment Variables Setup
MONITORS_START_URL = os.environ['MONITORS_START_URL']

# CLI Parser config
parser = ArgumentParser(
    prog='rbl',
    description='Tools to maintain my sanity',)

parser.add_argument('-u', action='store_true',
                    help='update cache file')

parser.add_argument('-c', action='store_true',
                    help='count blacklisted ips')

parser.add_argument('-l', action='store_true',
                    help='list all ips blacklisted and its blacklist')

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
        '''Write a new cache file in disk

        :type ips: list
        :param ips: result of monitor api request (monitor.get_data)
        '''

        with open('cached_data.json', 'w') as f:
            json.dump(ips, f)
            print('New cache saved')

    if args.u:
        # Force cache file to be updated
        ips = monitors.get_data(MONITORS_START_URL)
        update_cache(ips)
    else:
        # Try to load a existing cache file
        try:
            ips = load_cache()
        except FileNotFoundError:
            ips = monitors.get_data(MONITORS_START_URL)
            update_cache(ips)

    # Print the blacklist count
    if args.c:
        bl_count = blacklist.count(ips)
        bl_count = sorted(bl_count.items(), key=lambda x: x[1], reverse=True)
        for bl in bl_count:
            print('{:5} {}'.format(bl[1], bl[0]))

    # List all ips blacklisted
    if args.l:
        todos = blacklist.list_all(ips)
        for i in todos.items():
            print('{:5}: {}'.format(i[0], i[1]))

    # Identify and run dnsrbl.org script of delist
    if args.dnsrbl:
        blacklisted = blacklist.find_blocked(ips, 'dnsrbl.org')
        if blacklisted: delist.dnsrbl(blacklisted)

    print('Finished!')

if __name__ == "__main__":
    main()
