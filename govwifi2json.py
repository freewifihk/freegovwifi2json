#!/usr/bin/env python2
# Copyright 2013 onarray <http://www.onarray.com>

'''Scrape freegovwifi locations as json.'''

import os
import json
import urllib2

import bs4

def read(local_path='premises-list.html',
         url='http://www.gov.hk/mobile/en/wifi/location/launched.htm'):
    '''Return the html of the local file or given url.'''
    if os.path.isfile(local_path):
        with open(local_path) as local_file:
            return local_file.read()
    else:
        response = urllib2.urlopen(url)
        return response.read()

def extract(html):
    '''Extract premises from the given freegovwifi page.'''
    soup = bs4.BeautifulSoup(html)
    # First: planned, last: webstats
    districts = soup.html.body.find_all('div')[1:-1]
    premises = []
    for district in districts:
        locations = district.find_all('p')
        for location in locations:
            name_address = location.text.split('\n')
            premises.append(dict(name=name_address[0], address=name_address[1]))
    return premises

def main():
    '''Start execution of freegovwifi.'''
    local = os.path.join(os.path.dirname(__file__), 'res', 'premises-list.html')
    html = read(local_path=local)
    premises = extract(html)
    print(json.dumps(premises))

if __name__ == '__main__':
    main()
