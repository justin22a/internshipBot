import discord
from discord.ext import commands
import requests

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
GITHUB_API_URL = 'https://api.github.com/repos/SimplifyJobs/Summer2024-Internships/contents/'

bot = commands.Bot(command_prefix='!')

# Set to store seen opportunities
seen_opportunities = set()