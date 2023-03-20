import time
import requests
from random import choice

texts = ['Жопа съела трусы', 'А почему бы и да?', 'Я считаю, что вам нужно пойти нахуй!', 'ПОЛУЧАЕТСЯ ТАК, ДА!']

api_url : str = 'https://api.telegram.org/bot'
bot_token : str = '5753369509:AAFoLfdTTTMbulo3J1tQ4zrwGHA3aH1bJek'
max_count : int = 100

count : int = 0
off : int = -2
chat_id : int


while count < max_count:
    upd = requests.get(f'{api_url}{bot_token}/getUpdates?offset={off + 1}').json()
    if upd['result']:
        for result in upd['result']:
            off = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text=Все говорят - {result["message"]["text"]},'
                         f' а ты купи слона!').json()
    time.sleep(1)
    count +=1
