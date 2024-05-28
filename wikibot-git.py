import discord
from discord.ext import commands
import wikipediaapi
import textwrap

# Replace 'bot_token' with your bot's token from Discord
TOKEN = 'bot_token'

# Create an instance of Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent='wikibot_sb')

# Intents are required by Discord to fetch certain events
intents = discord.Intents.default()
intents.message_content = True  # Ensure the intent for message content is enabled

# Define the bot and its command prefix
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Embed the Wikipedia page to avoid character limits.
@bot.command(name='wiki', help='Search Wikipedia for a given query.')
async def wiki(ctx, *, query):
    page = wiki_wiki.page(query)
    if page.exists():
        embed = discord.Embed(title=page.title, url=page.fullurl, description=page.summary)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'No Wikipedia page found for "{query}"')


# Run the bot
bot.run(TOKEN)
