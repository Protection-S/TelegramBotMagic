import time

import requests

api_url: str = 'https://api.telegram.org/bot'
api_cat_url: str = 'https://aws.random.cat/meow'
bot_token: str = '5753369509:AAFoLfdTTTMbulo3J1tQ4zrwGHA3aH1bJek'

counter: int = 0
off: int = -2
cat_link: str
cat_response: requests.Response

while counter < 100:
    update = requests.get(f'{api_url}{bot_token}/getUpdates?offset={off + 1}').json()
    if update['result']:
        for result in update['result']:
            off = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(api_cat_url)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(
                    f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text=Все говорят - "{result["message"]["text"]}",'
                    f' но держи котика!').json()
                requests.get(f'{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}?text=Здесь должен был быть котик :(')
    counter +=1