from settings import Domen, minutes, seconds, link, bot
import requests
import datetime
import re
import time

def BotSendMessang(text):
    req = requests.get(bot + text).text


def mainTask(Domen, link):
    for key in link:
        link2 = link[key]
        for key2 in link2:
            time.sleep(1)
            req = requests.get(Domen+link2[key2]).text
            if req == '[]':
                req = 'no signal'
                text = key + ': ' + key2 + ' Term - ' + req

            else:
                req = re.split(r'\[', req)[-1].split(']')
                text = key + ': ' + key2 + ' Term - ' + req[0]
            BotSendMessang(text)


def start(minutes, seconds):
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    if min == minutes and seconds == sec:
        BotSendMessang(text=f'Новые сигналы - {datetime.datetime.now().hour}:{datetime.datetime.now().minute} {datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}')
        mainTask(Domen, link)


while True:
    start(minutes, seconds)