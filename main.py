import requests
import urllib
import time
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/774522814144315393/B5jhcofKdNvrStqdKq_hyPgALDaO_2yDJ8lCcBw8_lvlsmL9ogQELFSy_ntfkqWAYfzZ')

def executeSomething():

 while True:
     response = requests.get('https://meme-api.herokuapp.com/gimme/' + "jennie")
     resjson = response.json()
     urllib.request.urlretrieve(resjson["url"], "img.jpg")

     # bot
     with open("img.jpg", "rb") as f:
         webhook.add_file(file=f.read(), filename='example.jpg')

     response = webhook.execute()

     time.sleep(5)

executeSomething()
