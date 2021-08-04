# local
try:
    from . import config
except ImportError:
    import config

import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = f'https://discord.com/api/v{config.load()["misc"]["discord_api_version"]}'

def auth(url): # https://discord.com/developers/docs/topics/oauth2
    try:
        post_url = f'{API_ENDPOINT}/oauth2/token'

        data = {
            'client_id': os.getenv('DISCORD_ID'),
            'client_secret': os.getenv('DISCORD_SECRET'),
            'grant_type': 'authorization_code',
            'code': url.split('?code=')[1],
            'redirect_uri': url.split('?')[0],
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        connection_status = requests.post(url=post_url, data=data, headers=headers).json()
        
        # https://discord.com/developers/docs/resources/user#get-current-user
        account_data = requests.get(url=f'{API_ENDPOINT}/users/@me', headers={'authorization': 'Bearer ' + connection_status['access_token']}).json()

        return int(account_data['id'])
    except:
        return 0

if __name__ == '__main__':
    print(auth(input('URL: ')))