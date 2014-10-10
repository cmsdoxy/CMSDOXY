# aaltunda - ali.mehmet.altundag@cern.ch
# mtaze    - maric.taze@cern.ch

import urllib2, httplib, os

def read(url, request = False):
    if request: return readCert(url, request)
    URLObj = urllib2.urlopen(url)
    data   = URLObj.read()
    return data

def readCert(url, request, retries = 2):
    conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'),
                                          key_file  = os.getenv('X509_USER_PROXY'))
    r1=conn.request("GET", request)
    r2=conn.getresponse()
    request = r2.read()
    return request
