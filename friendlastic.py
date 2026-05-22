import discord
from discord.ext import commands
import random

class FantasticAsPlasticProject:
    need: str = ""
    htd: str = ""
    resolution: str = ""
    def __init__(self, arg_need, arg_htd, arg_resolution):
        self.need = arg_need
        self.htd = arg_htd
        self.resolution = arg_resolution

projects_fap : list[FantasticAsPlasticProject] = []
tips : list[str] = [
    "Sacolas plásticas do mercado podem ser\n reutilizadas para guardar coisas!",
    "Plástico reciclado pode passar por este processo inúmeras vezes,\neconomizando litros de petróleo e energia elétrica!"
]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents= intents)

@bot.event
async def on_ready():
    print("-- Conectado com êxito. Friendlastic Debug --")

@bot.event
async def on_message(message):
    if message.autor == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def daily_tips(ctx):
    await ctx.send("Dica do Dia:\n"+random.choice(tips))

@bot.command()
async def fantastic_as_plastic(ctx):
    project : FantasticAsPlasticProject = random.choice(projects_fap)
    await ctx.send(
        "Materiais:\n"+project.need+"\n\n"+
        "Como fazer:\n"+project.htd+"\n\n"+
        project.resolution+"\n"
                   )