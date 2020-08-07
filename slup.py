#!/usr/bin/env python3
import os
import sys
import requests
import configparser



def run_update(auth, records):
    confd = {}
    confd.update(auth)
    confd.update(records)
    r = requests.get('https://dnsup.sitelutions.com/dnsup', params=confd)
    if r.text.strip() != 'success':
        print("Encountered an error. API responded with [{}]".format(r.text.strip()))

def get_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    cdict = dict(config._sections)
    auth = cdict['auth']
    records = cdict['records']
    return auth, records

def main(filename):
    auth, records = get_config(filename)
    run_update(auth, records)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '{}/.config/slup.conf'.format(os.environ['HOME'])
    else:
        filename = sys.argv[1]
    main(filename)
