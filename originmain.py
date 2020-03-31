from discord.ext import commands
from botinfo import TOKEN
from bot_commands import SearchingRank, Guide



#bot setting

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#input bot commands

@bot.command()
async def 테스트(ctx, arg):
    print('bot said {0}'.format(arg))
    await ctx.send(arg)

@bot.command()
async def 도움말(ctx):
    text = Guide()
    await ctx.send(text)

@bot.command()
async def 전적검색(ctx, arg):
    text = SearchingRank(arg, None)
    await ctx.send(text)

#run discord bot
bot.run(TOKEN)

