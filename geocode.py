#!/usr/bin/env python2
# Copyright 2013 onarray <http://www.onarray.com>

'''Geocode govwifi locations.'''

import os.path
import json
import urllib
import urllib2

import pygeocoder

def google_v2(premise):
    '''Geocode the given premise using Google Maps API v2.'''
    url = 'http://maps.google.com.hk/maps/geo?'
    params = { 'q': premise['name'] }
    name = urllib.urlencode(params)
    page = urllib2.urlopen(url + name)
    html = page.read()
    doc = json.loads(html)
    place = doc.get('Placemark', [])
    if len(place) != 0:
        place = place[0]
        accuracy = place['AddressDetails']['Accuracy']
        longitude, latitude = place['Point']['coordinates'][:2]

        premise['latitude'] = latitude
        premise['longitude'] = longitude
        premise['accuracy'] = accuracy

    return premise

def google_v3(premise):
    '''Geocode a premise using the pygeocoder library.'''
    # Workaround pylint unsupporting static methods
    geocoder = pygeocoder.Geocoder()

    address = "{0}, {1}, Hong Kong".format(premise['name'], premise['address'])
    try:
        results = geocoder.geocode(address)
    except pygeocoder.GeocoderError:
        address = "{0}, Hong Kong".format(premise['name'])
        try:
            results = geocoder.geocode(address)
        except pygeocoder.GeocoderError:
            raise
    return results.coordinates

def merge_google_v3(premise, coordinates):
    '''Merge Google geocoding API v3 results.'''
    if premise.has_key('latitude'):
        coords = { 'latitude': coordinates[0], 'longitude': coordinates[1] }
        premise.setdefault('google_v3', coords)
    else:
        premise['latitude'] = coordinates[0]
        premise['longitude'] = coordinates[1]
    return premise

def read(path):
    '''Parse serialised json.'''
    with open(path) as serialised:
        premises = serialised.read()
    return json.loads(premises)

def main():
    '''Start execution of Geocode.'''
    path = os.path.join('res', 'premises-list-geocoded.json')
    premises = read(path)
    import pprint
    pprint.pprint(premises)

if __name__ == '__main__':
    main()
