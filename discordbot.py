from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時のメッセージ
@bot.event
async def on_ready():
    # 起動時にメッセージの送信
    channel = client.get_channel(634876781073268739)
    await channel.send('起動したのー')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
    await ctx.send('647861424432873483','pong!!')

@bot.command()
async def makoto_apology(ctx):
    await ctx.send('ごめん、ユイ・・・・！')


bot.run(token)
