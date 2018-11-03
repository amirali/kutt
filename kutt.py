import sys
import os

import click
import requests
import json

base_url = "https://kutt.it"
try:
    if sys.platform == "win32":
        APPDATA = os.getenv('APPDATA')
        with open(APPDATA+"kutt-cli\\apikey.txt") as f:
            API = f.read()
            f.close()
    else:
        with open('$HOME/.kutt-cli/apikey.txt') as f:
            API = f.read()
            f.close()
except:
    print ("Get an API key from kutt.it and run `kutt config-api`")

try:
    headers = {"X-API-Key": API}
except:
    pass
    
@click.group()
def cli():
    """
    Submit(options):

        -c, --customurl STRING          Custom ID for custom URL

        -p, --password STRING           Password for the URL

        -r, --reuse                     Return last object of target if exists

    Submit(example):

        > kutt submit -c '[CUSTOM]' -p '[PASSWORD]' -r "[URL]"


    Delete(example):

        > kutt delete [URL/ID]

    List(example):

        > kutt list
    """
    pass

@click.command()
def config_api():
    pyv = int(sys.version[0])
    if sys.platform == "win32":
        APPDATA = os.getenv('APPDATA')
        if not os.path.exists(APPDATA+"\\kutt-cli"):
            os.makedirs(APPDATA+"\\kutt-cli")
        with open(APPDATA+"\\kutt-cli\\apikey.txt", 'w') as f:
            if pyv < 3:
                f.write(raw_input("API: "))
            else:
                f.write(input("API: "))
            f.close()
    elif sys.platform == 'linux':
        if not os.path.exists("$HOME/.kutt-cli/"):
            os.makedirs("$HOME/.kutt-cli/")
        with open('$HOME/.kutt-cli/apikey.txt', 'w') as f:
            if pyv < 3:
                f.write(raw_input("API: "))
            else:
                f.write(input("API: "))
            f.close()

@click.command('submit', short_help="Submit a new short URL")
@click.argument('url', type=click.STRING)
@click.option('-c', '--customurl', type=click.STRING)
@click.option('-p', '--password', type=click.STRING)
@click.option('-r', '--reuse', is_flag=True)
def submit(url, customurl, password, reuse):
    payload = {}
    payload['target'] = url

    if customurl:
        payload['customurl'] = customurl
    if password:
        payload['password'] = password
    if reuse:
        payload['reuse'] = True

    r = requests.post(base_url+'/api/url/submit', data=payload, headers=headers)
    if not r.status_code == 200:
        err = r.json()
        click.echo(err['error'])
    else:
        data = r.json()
        click.echo('Target: '+data['target'])

        if data['reuse']:
            click.echo("your target is exists! i show you last object of this target")
            if data['password']:
                click.echo("Your url has a password. we don't know whats that.")
        else:
            if data['password']:
                click.echo("Password: "+password)
            if customurl:
                click.echo("your url customed to: "+data['id'])

        click.echo("\nShorted URL is: "+data['shortUrl'])

@click.command('delete', short_help="Delete a shorted link (Give me url id or url shorted)")
@click.argument('target', type=click.STRING)
def delete(target):
    if "/" in target:
        id = target.split('/')[-1]
    else:
        id = target

    payload = {'id': id}
    r = requests.post(base_url+'/api/url/deleteurl', headers=headers, data=payload)

    if not r.status_code == 200:
        err = r.json()
        click.echo(err['error'])
    else:
        msg = r.json()
        click.echo(msg['message'])

@click.command('list', short_help="List of last 5 URL objects.")
def list():
    r = requests.get(base_url+'/api/url/geturls', headers=headers)
    data = r.json()
    for item in data['list']:
        click.echo(json.dumps(item, indent=2))
        click.echo('\n')

"""TODO: stats
@click.command('stats', short_help="Status of a url")
@click.argument('target', type=click.STRING)
def stats():
    if "/" in target:
        id = target.split('/')[-1]
    else:
        id = target

"""

cli.add_command(submit)
cli.add_command(delete)
cli.add_command(list)
cli.add_command(config_api)

if __name__ == "__main__":


    cli()
