import sys
import os

import click
import requests
import json

from kutt import kutt

base_url = "https://kutt.it"
try:
    if sys.platform == "win32":
        APPDATA = os.getenv('APPDATA')
        with open(APPDATA+'\\kutt-cli\\apikey.txt') as f:
            API = f.read()
            f.close()
    else:
        with open('$HOME/.kutt-cli/apikey.txt') as f:
            API = f.read()
            f.close()
except:
    print ("Get an API key from kutt.it and run `kutt config-api`")



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

    Links(example):

        > kutt links
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
    response = kutt.submit(API, url, customurl, password, reuse)
    
    if (response['code'] == 200) or (response['code'] == 201):
        click.echo('Target: '+response['data']['target'])

        if response['data']['password']:
            click.echo("Your URL is now secured with password")

        click.echo("\nShorted URL is: "+response['data']['link'])

    else:
        click.echo(response['data']['error'])

@click.command('delete', short_help="Delete a shorted link (Give me url id or url shorted)")
@click.argument('target', type=click.STRING)
def delete(target):
    response = kutt.delete(API, target)

    if response['code'] == 200:
        click.echo(response['data']['message'])
    else:
        click.echo(response['data']['error'])

@click.command('links', short_help="List of last URL objects. (default is 1)")
@click.option('-n', '--number', type=click.INT)
def links(number):
    if not number:
        number = 1
    response = kutt.links(API, number)
    click.echo(json.dumps(response, indent=2))

cli.add_command(submit)
cli.add_command(delete)
cli.add_command(links)
cli.add_command(config_api)

if __name__ == "__main__":


    cli()
