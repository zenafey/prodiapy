import discord
from discord.ext import commands
import prodia

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
prodia.Client(api_key='your-api-key')

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.command()
async def dream(ctx, *, prompt):
    msg = await ctx.reply(f"Generating... {prompt}")
    image = prodia.txt2img(prompt=prompt)
    await msg.edit(f"**{prompt}**\n\n{image}")

bot.run('your-bot-token')