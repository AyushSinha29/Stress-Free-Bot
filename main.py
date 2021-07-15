import discord
import os
import requests
import json
import random
from replit import db
from alive import keep_alive
import calendar
from datetime import datetime
from datetime import date
import pytz

today = date.today()

client = discord.Client()

sad_words = [
    "sad", "depressed", "unhappy", "anxiety", "tensed", "mental problem",
    "dillema", "tension", "don't know what to do", "helpless",
    "bahot tension h boss", "feeling low"
]

st_encouragements = [
    "cheer up buddy", "chill baba , sab theek ho jayega",
    "do shots maar sab sahi ho jayega", "aaal izz well",
    "good things take time"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('=quote'):
        quote = get_quote()
        await message.channel.send(quote)
    if db["responding"]:
        options = st_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("=new"):
        encouraging_message = msg.split("=new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send(
            "Your encouraging message has been added ! Thank you!")

    if msg.startswith("=list"):
        encouragements = []
        if "encouragements" in db.keys():

            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("Oye bot"):
        await message.channel.send(
            "Hey , kyaa haal chaal? Sab changa!! \nSee my commands by typing =botcmd!"
        )

    if msg.startswith("=Ayush's Playlist"):
        await message.channel.send(
            "-p https://www.youtube.com/watch?v=5sYsSrvWnqQ&list=RD5sYsSrvWnqQ&start_radio=1"
        )

    if msg.startswith("=del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("#del", 1)[1])
            delete_encouragements(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("Hello bot"):
        await message.channel.send("Hey , kyaa haal chaal? Sab changa!!")

    if msg.startswith("Ok"):
        await message.channel.send("Ok!")

    if msg.startswith(" bc "):
        await message.channel.send("Kripya tameez se baat karein!")

    if msg.startswith("Hi bot"):
        await message.channel.send(
            "Hi there , whats up? Hope everything is fine . Keep visiting this server!"
        )

    if msg.startswith("=calendar.Jan"):
        await message.channel.send(calendar.month(2021, 1))
    if msg.startswith("=calendar.Feb"):
        await message.channel.send(calendar.month(2021, 2))
    if msg.startswith("=calendar.Mar"):
        await message.channel.send(calendar.month(2021, 3))
    if msg.startswith("=calendar.Apr"):
        await message.channel.send(calendar.month(2021, 4))
    if msg.startswith("=calendar.May"):
        await message.channel.send(calendar.month(2021, 5))
    if msg.startswith("=calendar.Jun"):
        await message.channel.send(calendar.month(2021, 6))
    if msg.startswith("=calendar.Jul"):
        await message.channel.send(calendar.month(2021, 7))
    if msg.startswith("=calendar.Aug"):
        await message.channel.send(calendar.month(2021, 8))
    if msg.startswith("=calendar.Sep"):
        await message.channel.send(calendar.month(2021, 9))
    if msg.startswith("=calendar.Oct"):
        await message.channel.send(calendar.month(2021, 10))
    if msg.startswith("=calendar.Nov"):
        await message.channel.send(calendar.month(2021, 11))
    if msg.startswith("=calendar.Dec"):
        await message.channel.send(calendar.month(2021, 12))

    if msg.startswith("=today"):
        d2 = today.strftime("%B %d, %Y")

        await message.channel.send(d2)
    if msg.startswith("=time"):
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        await message.channel.send(datetime_ist.strftime(' %H:%M:%S %Z %z'))

    if msg.startswith("=links"):
        await message.channel.send(
            "\n1.AEC:(mailed before the class)\n2.AEC LAB: https://meet.google.com/lookup/fxop6hqolk \n3.BEE and BEE LAB: https://meet.google.com/ptx-uibr-cev \n4.BMS PRAC: https://meet.google.com/baq-jyjp-atf?authuser=0 \n5.PHYSICS LAB: https://meet.google.com/iwu-vkto-sgb?authuser=0 \n6.EVS: https://meet.google.com/lookup/ceicg6qj3c?authuser=0&hs=179\n7.MATHS: https://meet.google.com/lookup/hjy7klio6v?authuser=0&hs=179"
        )

    if msg.startswith("=botcmd"):
        await message.channel.send(
            "\n1.=quote - for inspirational quotes.\n2.=new - for adding new encouraging message \n3.=list - for the list of encouraging messages \n4.=del - to delete an encouraging message. \n5.=links- for all links of classes. \n6.=today- for today's date \n7.=time - for current IST"
        )

    if msg.startswith("Bye bot"):
        await message.channel.send(
            "Bye dude! It was nice talking to you ! , Keep smiling , sit back and chill !!"
        )

    if msg.startswith("What's your job bot?"):
        await message.channel.send(
            "Hey there , my job is to talk to you guys and make you a little stress free!"
        )

    if msg.startswith("Hanji sab changa"):
        await message.channel.send("Oh balle balle !!")

    if msg.startswith("Good boi"):
        await message.channel.send("Sab aapki kripa !")

    if msg.startswith("Ye lo chummi lo"):
        await message.channel.send("Isshh , ye sab dm m !")

    if msg.startswith("song help"):
      await message.channel.send("Pick a genre and type g(space)serial number of genre:\n1.Bollywood lofi     \n2.Bollywood EDM\n3.Hollywood")

    if msg.startswith("g 1"):
      await message.channel.send("https://www.youtube.com/watch?v=077mXFFnm2A&list=RD077mXFFnm2A&start_radio=1&t=0")
    
    if msg.startswith("g 2"):
      await message.channel.send("youtube.com/watch?v=l2Yb4bz9ONk&list=RDGMEMdXq5-clz9aWDcRBQn1xu2w&start_radio=1")    

    if msg.startswith("g 3"):
      await message.channel.send("https://www.youtube.com/watch?v=d_HlPboLRL8&list=RDFxUi08fzJfs&index=24")    
    if msg.startswith("g 4"):
      await message.channel.send("https://www.youtube.com/watch?v=wK3TgKAwHS8&list=RDwK3TgKAwHS8&start_radio=1&rv=wK3TgKAwHS8&t=0") 
      
        

    if msg.startswith("responding"):
        value = msg.split("responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Response from the bot is on")
        else:
            db["responding"] = False
            await message.channel.send("Response from the bot is off")


keep_alive()
client.run(os.getenv('SECURITY'))
