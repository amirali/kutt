"""Kutt.it API wrapper"""
import requests

BASE_URL = "https://kutt.it/api/v2/links"

def submit(apikey, url, description=None, expire_in=None, password=None, customurl=None, reuse=False, domain=None, host_url=BASE_URL):
    """Create a new shorten url object"""
    headers = {'X-API-Key': apikey}

    payload = {'target': url, 'description' : description, 'expire_in' : expire_in, 'password' : password, 'customurl' : customurl, 'reuse' : reuse, 'domain' : domain}
    res = requests.post(host_url, data=payload, headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def delete(apikey, id, host_url=BASE_URL):
    """Delete a shorten url object"""
    headers = {'X-API-Key': apikey}

    res = requests.delete(f"{host_url}/{id}", headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def update(apikey, id, url, address, description=None, expire_in=None, host_url=BASE_URL):
    """Update a shorten url object"""
    headers = {'X-API-Key': apikey}

    payload = {'target': url, 'address' : address, 'description' : description, 'expire_in' : expire_in}
    res = requests.patch(f"{host_url}/{id}", headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def links(apikey, limit=10, skip=0, all=False, host_url=BASE_URL):
    """Get list of links"""
    headers = {'X-API-Key': apikey}

    payload = {'limit': limit, 'skip' : skip, 'all' : all}
    res = requests.get(host_url, headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def stats(apikey, id, host_url=BASE_URL):
    """Get link stats"""
    headers = {'X-API-Key': apikey}

    res = requests.get(f"{host_url}/{id}/stats", headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}
