import discord
import random
import time
import asyncio

TOKEN = "OTU2MTkyNTUwMjkxNjY5MDIy.YjsptQ.eFCF_QwKld-_MVBmnVEtgzItlsY"

client = discord.Client()


@client.event
async def on_message(message):
        if message.auther == client.user:
            return

        if message.client.startswitch(".ping"):
                await message.channel.send("pong")

        if message.content.startswitch(".say"):
            mes = message.content.plit()
            output = ""
            for word in mes[1]:
                output += word
                output += " "
            await message.channl.send(output)
            await message.delete()

@client.event
async def on_ready():
    print("Kører")

client.run(TOKEN)
print(client.user.name)