import json
import requests

base_url = "https://kutt.it"

def submit(apikey, url, customurl=None, password=None, reuse=False):
    headers = {'X-API-Key': apikey}

    payload = {}
    payload['target'] = url

    if customurl:
        payload['customurl'] = customurl
    if password:
        payload['password'] = password
    if reuse:
        payload['reuse'] = True

    r = requests.post(base_url+'/api/v2/links', data=payload, headers=headers)
    if not ((r.status_code == 200) or (r.status_code == 201)):
        err = r.json()
        return {'code': r.status_code, 'data': err}
    else:
        data = r.json()
        return {'code': r.status_code, 'data': data}


def delete(apikey, target):
    headers = {'X-API-Key': apikey}

    if "/" in target:
        id = target.split('/')[-1]
    else:
        id = target

    payload = {"id": id}

    r = requests.post(base_url+'/api/url/deleteurl', headers=headers, data=payload)

    if not r.status_code == 200:
        err = r.json()
        return {'code': r.status_code, 'data': err}
    else:
        data = r.json()
        return {'code': r.status_code, 'data': data}


def links(apikey, limit=1):
    headers = {'X-API-Key': apikey}

    r = requests.get(base_url+'/api/v2/links?limit='+str(limit), headers=headers)
    data = r.json()
    return data['data']
