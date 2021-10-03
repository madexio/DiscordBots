import discord
import random
from secret.flipper_secret import token
from secret.flipper_secret import guild_ids
from discord_slash import SlashCommand # Importing the newly installed library.
from discord_slash.utils.manage_commands import create_option

client = discord.Client()
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("Ready!")

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
            ])

async def coin(c, number=1):
    h = 0
    t = 0
    if number == 1:
        a = random.randrange(100)
        if (a < 50):
            await c.send(f"Heads")
        else:
            await c.send(f"Tails")
    else:
        for i in range(number):
            a = random.randrange(100)
            if (a < 50):
                h += 1
            else:
                t += 1
        await c.send(f"You flip {number} times\nHeads: {h}\t Tails: {t}")

client.run(token)