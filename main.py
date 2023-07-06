import requests
from time import sleep

channelid = '[CHANNELID]'
token = '[DISCORDTOKEN]'

print('script is running')

while True:
    typing = requests.post(f'https://discord.com/api/v9/channels/{channelid}/typing', headers={'authorization': token})
    if not typing.status_code == 204:
        print('error')
        print(f'status code: {typing.status_code}')
        print(f'data: {typing.text}')
        break
    sleep(8)
