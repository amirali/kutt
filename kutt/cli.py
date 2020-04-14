"""
Kutt.it cli
Author: Amirali Esfandiari
License: GPL3
URL: https://github.com/realamirali/kutt-cli/
"""
import json
import os
import sys

import fire

from kutt import kutt

class Kutt:
    """
    Kutt.it cli
    """
    def __init__(self):
        try:
            if sys.platform == "win32":
                self._app_data = os.getenv('APPDATA')
                with open(self._app_data+'\\kutt-cli\\apikey.txt') as api_file:
                    self._api = api_file.read()
                    api_file.close()
            else:
                with open('$HOME/.kutt-cli/apikey.txt') as api_file:
                    self._api = api_file.read()
                    api_file.close()
        except OSError as err:
            print("Get an api key from kutt.it and run `kutt config-api`")
            del err

    def config_api(self):
        """Set the API_KEY from kutt.it"""
        if sys.platform == "win32":
            if not os.path.exists(self._app_data+"\\kutt-cli"):
                os.makedirs(self._app_data+"\\kutt-cli")

            with open(self._app_data+"\\kutt-cli\\apikey.txt", 'w') as api_file:
                api_file.write(input("API: "))
                api_file.close()
        elif sys.platform == 'linux':
            if not os.path.exists("$HOME/.kutt-cli/"):
                os.makedirs("$HOME/.kutt-cli/")

            with open('$HOME/.kutt-cli/apikey.txt', 'w') as api_file:
                api_file.write(input("API: "))
                api_file.close()

    def submit(self, url, customurl=None, password=None, reuse=None):
        """Create a new shorten url object"""
        response = kutt.submit(self._api, url, customurl, password, reuse)
        if (response['code'] == 200) or (response['code'] == 201):
            print('Target: '+response['data']['target'])

            if response['data']['password']:
                print("Your URL is now secured with password")

            print("\nShorted URL is: "+response['data']['link'])

        else:
            print(response['data']['error'])

    def delete(self, target):
        """Delete an object"""
        response = kutt.delete(self._api, target)

        if response['code'] == 200:
            print(response['data']['message'])
        else:
            print(response['data']['error'])

    def links(self, number=5):
        """Show your last created links (default 5)"""
        response = kutt.links(self._api, number)
        print(json.dumps(response, indent=2))

def main():
    """initilaze"""
    fire.Fire(Kutt)
