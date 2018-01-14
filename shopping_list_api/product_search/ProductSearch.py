import http.client, urllib.request, urllib.parse, urllib.error, base64

from rest_framework.utils import json


class ProductSearch:

    def __init__(self):
        self.headers = {
            # API key
            'Ocp-Apim-Subscription-Key': '8e0a76066aca4e3e8c406e4ab7a3ef6b',
        }

    def by_barcode(self, gtin):
        params = urllib.parse.urlencode({
            'gtin': gtin
        })
        try:
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/product/?%s" % params, "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return json.loads(data)
        except Exception as e:
            print("Tesco API Error {0}".format(e))
            return None

    def by_name(self, name):
        try:
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/grocery/products/?query=%s&offset=%s&limit=%s" % (name, '', ''),
                         "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return json.loads(data)
        except Exception as e:
            print("Tesco API Error {0}".format(e))
            return None
