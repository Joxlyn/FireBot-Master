import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!8ball"):
        await client.send_message(message.channel, random.choice(["Nop :8ball:",
                                                                  "Yes :8ball:",
                                                                  "No estoy seguro... :8ball:",
                                                                  "Sin Duda alguna! :8ball:",
                                                                  "Puede ser... :8ball:",
                                                                  "50%/50% :8ball:",
                                                                  "Dudoso... Kappa :8ball:"]))

    elif message.content.startswith("!random number"):
        await client.send_message(message.channel, random.choice(["1 :game_die:"]))

        
                                  
client.run("your token here")
                                  
