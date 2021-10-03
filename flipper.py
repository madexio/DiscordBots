import discord
import random
from secret.flipper_secret import token
from secret.flipper_secret import guild_ids
from discord_slash import SlashCommand # Importing the newly installed library.
from discord_slash.utils.manage_commands import create_option

#Store the discord client
client = discord.Client()
#Tells the client that we will have slash commands
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

#Check for when it has connected
@client.event
async def on_ready():
    print("Ready!")

#Create and store a json for a slash command called /coin
@slash.slash(
    name="coin",
    description="Flip a coin n times",
    guild_ids=guild_ids,
    options=[
        create_option(
            name="number",
            description="Total number of flips",
            option_type=4,
            required=False
        )
    ]
)

#define the function for coin which will take in the message from the user and an additional argument
async def coin(c, number=1):
    #Heads and tails
    h = 0
    t = 0
    #If the user only flips a single coin print out either heads or tails
    if number == 1:
        a = random.randrange(100)
        if (a < 50):
            await c.send(f"Heads")
        else:
            await c.send(f"Tails")
    #If the user wants more than one, roll number times and print all results
    else:
        for i in range(number):
            a = random.randrange(100)
            if (a < 50):
                h += 1
            else:
                t += 1
        await c.send(f"You flip {number} times\nHeads: {h}\t Tails: {t}")

#Run the client
client.run(token)