"""Kutt.it API wrapper"""
import requests

BASE_URL = "https://kutt.it"

def submit(apikey, url, customurl=None, domain=None, description=None, password=None, reuse=False, host_url=BASE_URL):
    """Create a new shorten url object"""
    headers = {'X-API-Key': apikey}

    payload = {}
    payload['target'] = url

    if customurl:
        payload['customurl'] = customurl
    if description:
        payload['description'] = description
    if password:
        payload['password'] = password
    if domain:
        payload['domain'] = domain
    if reuse:
        payload['reuse'] = 'true'

    res = requests.post(host_url+'/api/v2/links', data=payload, headers=headers)

    data = res.json()
    return {'code': res.status_code, 'data': data}

def delete(apikey, target, host_url=BASE_URL):
    """Delete a shorten url object"""
    headers = {'X-API-Key': apikey}

    if "/" in target:
        link_id = target.split('/')[-1]
    else:
        link_id = target

    payload = {"id": link_id}

    res = requests.post(host_url+'/api/url/deleteurl', headers=headers, data=payload)

    data = res.json()
    return {'code': res.status_code, 'data': data}


def links(apikey, limit=1, host_url=BASE_URL):
    """List last url objects"""
    headers = {'X-API-Key': apikey}

    if limit == "all":
        res = requests.get(host_url+'/api/v2/links?all=true', headers=headers)

    else:
        res = requests.get(host_url+'/api/v2/links?limit='+str(limit), headers=headers)

    data = res.json()
    return data['data']
