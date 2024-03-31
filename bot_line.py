import sys
sys.path.append("/Users/macky/anaconda3/lib/python3.10/site-packages")

import os
import discord
import requests
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
LINE_TOKEN=os.getenv("LINE_TOKEN")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
def send_line_msg(msg):
    acc_token = LINE_TOKEN
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)
@client.event
async def on_voice_state_update(user, before, after):
    if before.channel != after.channel:
        if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID:
            send_line_msg(after.channel.name+ "に" + user.display_name + "が参加しました")
client.run(DISCORD_TOKEN)
