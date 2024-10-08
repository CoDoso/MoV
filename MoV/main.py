from discord.ext import commands
import discord
import yaml
import os

bot = commands.Bot(command_prefix="T!", intents=discord.Intents.all())  # bot (variable) creation


@bot.event  # Bot Setup
async def on_ready():  # Activates at start-up
    print(f'{bot.user} is now running!')
    game_init_()


def game_init_():
    file_found: bool = False
    for file in [f for f in os.listdir("MoV/") if os.path.isfile(f)]:
        if file == 'users.yml':
            file_found = True
            break
        else:
            pass
    if not file_found:
        with open(f"users.yml", 'x') as File:
            yaml.safe_dump("", File)


if __name__ == "__main__":
    bot.run('MTEwOTUwNjkwODk3MDI5OTQ3Mg.GlNp9v.BmW5-KOHEVULjIbZZak4OPCeBRCV4PBVhoZN20')
