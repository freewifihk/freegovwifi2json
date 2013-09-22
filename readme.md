# Free Government WiFi Locations (Hong Kong)

The Hong Kong government provides free wifi hotspots in government buildings and
parks throughout Hong Kong.

However, they do not provide a free machine-readable (`json` etc.) list of these
locations.

This project remedies this by first scraping the human-readable list then
geocoding each premise using the Google Maps API before returning a `json` file.

Two versions of the API are used; the first version two, and the second version
three. The former is preferred (and used as the default) since it provides an
accuracy measure (0-9) which is omitted in the newer API. This is useful since
the accuracy of both API's are imperfect.

## Usage

1. `pip-2.7 install beautifulsoup4`
2. `python2 ./govwifi2json.py`

## Author

© 2013 onarray <http://www.onarray.com>

## License

Released under the [MIT license](http://onarray.mit-license.org).
