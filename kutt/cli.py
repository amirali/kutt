"""
Kutt.it cli
Author: Amirali Esfandiari
License: MIT
URL: https://github.com/realamirali/kutt/
"""
import json
import os
import sys

import fire
import toml

from kutt import kutt

class Kutt:
    """
    Kutt.it cli
    """
    def __init__(self):
        try:
            if sys.platform == "win32":
                self._app_data = os.getenv('APPDATA')
                with open(self._app_data+'\\kutt-cli\\config.toml') as config:
                    config = toml.loads(config.read())
            else:
                self._home = os.path.expanduser('~')
                with open(self._home+'/.kutt-cli/config.toml') as config:
                    config = toml.loads(config.read())

            self._config = config
            cli_config = config.get('config')
            default_host = cli_config.get('default')
            host_config = config.get(default_host)
            self._host_url = host_config.get('url')

            if not host_config.get('api'):
                print("Please add your api key, see `kutt config`")
                return

            self._api = host_config.get('api')

        except OSError as err:
            init_config = {'config': {'default': 'kutt'}, 'kutt': {'url': "https://kutt.it"}}
            if sys.platform == "win32":
                if not os.path.exists(self._app_data+"\\kutt-cli"):
                    os.makedirs(self._app_data+"\\kutt-cli")

                with open(self._app_data+"\\kutt-cli\\config.toml", 'w') as config_file:
                    config_file.write(toml.dumps(init_config))

            else:
                if not os.path.exists(self._home+"/.kutt-cli/"):
                    os.makedirs(self._home+"/.kutt-cli/")

                with open(self._home+"/.kutt-cli/config.toml", 'w') as config_file:
                    config_file.write(toml.dumps(init_config))

            del err


    def config(self, action=None, arg1=None, arg2=None):
        """Config - see `kutt config help`"""
        config = self._config

        if action == 'api':
            api = arg1
            if api == None:
                print("You can't leave api blank!", "kutt config api <APIKEY> <HOST>", sep='\n')
                return

            else:
                host = arg2 or 'kutt'
                config[host]['api'] = api

        elif action == 'url':
            if arg2 == None or arg2 == 'kutt':
                print("You can't change kutt host url")
                return

            else:
                url = arg1
                if url == None:
                    print("You can't leave URL blank!", "kutt config url <URL> <HOST>", sep='\n')
                    return
                else:
                    host = arg2
                    config[host]['url'] = url

        elif action == "new-host":
            print("New host setup")
            host = input("Host name: ")
            url = input("Host URL: ")
            api = input("API KEY: ")
            if host and url and api:
                config[host] = {}
                config[host]['api'] = api
                config[host]['url'] = url

            else:
                print("You can't Leave anything blank!")
                return

        elif action == "set-host":
            host = arg1 or 'kutt'
            if not host in config.keys():
                print("You most choose the default host from your hosts")
                return

            else:
                config['config']['default'] = host

        elif action == "show":
            print(toml.dumps(config))
            return

        else:
            print("use config with following commands (Leave host blank for default kutt host)",
                  "To set api key for a host:",
                  "> kutt config api <APIKEY> <HOST>\n",
                  "To set url for a host:",
                  "> kutt config url <URL> <HOST>\n",
                  "To add a new host prompt:",
                  "> kutt config new-host\n",
                  "To set default host:",
                  "> kutt config set-host <HOST>\n",
                  "To show your config",
                  "> kutt config show\n",
                  "To show this help:",
                  "kutt config help", sep='\n')

            return

        if sys.platform == "win32":
            with open(self._app_data+"\\kutt-cli\\config.toml", 'w') as config_file:
                config_file.write(toml.dumps(config))

        elif sys.platform == 'linux':
            with open(self._home+'/.kutt-cli/config.toml', 'w') as config_file:
                config_file.write(toml.dumps(config))

    def submit(self, url, customurl=None, password=None, domain=None, reuse=None):
        """Create a new shorten url object"""
        response = kutt.submit(apikey=self._api, url=url, customurl=customurl,
                               password=password, domain=domain, reuse=reuse, host_url=self._host_url)
        if (response['code'] == 200) or (response['code'] == 201):
            print('Target: '+response['data']['target'])

            if response['data']['password']:
                print("Your URL is now secured with password")

            print("\nShorted URL is: "+response['data']['link'])

        else:
            print(response['data']['error'])

    def delete(self, target):
        """Delete an object"""
        response = kutt.delete(apikey=self._api, target=target, host_url=self._host_url)

        if response['code'] == 200:
            print(response['data']['message'])
        else:
            print(response['data']['error'])

    def links(self, limit=5):
        """Show your last created links (default 5)"""
        response = kutt.links(apikey=self._api, limit=limit, host_url=self._host_url)
        print(json.dumps(response, indent=2))

def main():
    """initilaze"""
    fire.Fire(Kutt)
