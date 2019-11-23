from discord.ext import commands
import os
import traceback
import pandas as pd

df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred'],
    'English' : [12, 34, 56, 78, -1, 90],
    'Math'    : [88, 66, -1, 44, 22, -1]    
})
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時のメッセージ
@bot.event
async def on_ready():
    # 起動時にメッセージの送信
    channel = bot.get_channel(634876781073268739)
    await channel.send('プリン参上なのー')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
    channel = bot.get_channel(647861424432873483)
    await channel.send('pong!!')

@bot.command()
async def makoto_apology(ctx):
    await ctx.send('ごめん、ユイ・・・・！')

@bot.command()
async def a(ctx, *, message: str):
    await ctx.send(message + 'さんお疲れ様なのー')

@bot.command()
async def b(ctx):
    await ctx.send(df)

bot.run(token)
