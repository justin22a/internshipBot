import discord
from discord.ext import commands
import requests

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
GITHUB_API_URL = 'https://api.github.com/repos/SimplifyJobs/Summer2024-Internships/contents/'

bot = commands.Bot(command_prefix='!')

# Set to store seen opportunities
seen_opportunities = set()


@bot.command()
async def internships(ctx):
    global seen_opportunities

    response = requests.get(GITHUB_API_URL)

    if response.status_code == 200:
        data = response.json()

        new_opportunities = set()

        for item in data:
            if item['type'] == 'file':
                company_name = item['name'].replace('.md', '')
                file_url = item['html_url']

                # If this opportunity hasn't been seen yet
                if file_url not in seen_opportunities:
                    await ctx.send(f'Company: {company_name}\nLink: {file_url}\n')
                    new_opportunities.add(file_url)

        # Update the set with the newly seen opportunities
        seen_opportunities.update(new_opportunities)

        if not new_opportunities:
            await ctx.send("No new internship opportunities found.")

    else:
        await ctx.send("Couldn't fetch the data. Please try again later.")


bot.run(TOKEN)
