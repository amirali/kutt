"""Kutt.it API wrapper"""
import requests

BASE_URL = "https://kutt.it/api/v2/links"

def submit(apikey, url, description=None, expire_in=None, password=None, customurl=None, reuse=False, domain=None):
    """Create a new shorten url object"""
    headers = {'X-API-Key': apikey}

    payload = {'target': url, 'description' : description, 'expire_in' : expire_in, 'password' : password, 'customurl' : customurl, 'reuse' : reuse, 'domain' : domain}
    res = requests.post(BASE_URL, data=payload, headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def delete(apikey, id):
    """Delete a shorten url object"""
    headers = {'X-API-Key': apikey}

    res = requests.delete(f"{BASE_URL}/{id}", headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def update(apikey, id, url, address, description=None, expire_in=None): 
    """Update a shorten url object"""
    headers = {'X-API-Key': apikey}
    
    payload = {'target': url, 'address' : address, 'description' : description, 'expire_in' : expire_in}
    res = requests.patch(f"{BASE_URL}/{id}", headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def links(apikey, limit=10, skip=0, all=False):
    """Get list of links"""
    headers = {'X-API-Key': apikey}
   
    payload = {'limit': limit, 'skip' : skip, 'all' : all}
    res = requests.get(BASE_URL, headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def stats(apikey, id):
    """Get link stats"""
    headers = {'X-API-Key': apikey}
   
    res = requests.get(f"{BASE_URL}/{id}/stats", headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}