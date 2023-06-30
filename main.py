import requests
from time import sleep

print('script is running')

while True:
    typing = requests.post('https://discord.com/api/v9/channels/[CHANNELID]/typing', headers={'authorization': '[DISCORDTOKEN]'})
    if not typing.status_code == 204:
        print('error')
        print(f'status code: {typing.status_code}')
        print(f'data: {typing.text}')
        break
    sleep(8)
