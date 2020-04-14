"""Kutt.it API wrapper"""
import requests

BASE_URL = "https://kutt.it"

def submit(apikey, url, customurl=None, password=None, reuse=False):
    """Create a new shorten url object"""
    headers = {'X-API-Key': apikey}

    payload = {}
    payload['target'] = url

    if customurl:
        payload['customurl'] = customurl
    if password:
        payload['password'] = password
    if reuse:
        payload['reuse'] = True

    res = requests.post(BASE_URL+'/api/v2/links', data=payload, headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}

def delete(apikey, target):
    """Delete a shorten url object"""
    headers = {'X-API-Key': apikey}

    if "/" in target:
        link_id = target.split('/')[-1]
    else:
        link_id = target

    payload = {"id": link_id}

    res = requests.post(BASE_URL+'/api/url/deleteurl', headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def links(apikey, limit=1):
    """List last url objects"""
    headers = {'X-API-Key': apikey}

    res = requests.get(BASE_URL+'/api/v2/links?limit='+str(limit), headers=headers)
    data = res.json()
    return data['data']
