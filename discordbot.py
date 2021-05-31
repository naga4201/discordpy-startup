from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def gia(ctx):
    await ctx.send(':ElrV7StVkAEnJXn:')

@client.command()
async def addch(ctx, channel_name):
    thread_category = bot.get_channel(786837217041055785)  
    await ctx.guild.create_text_channel(channel_name, category=thread_category)
    await ctx.send(f"スレッド[ {channel_name} ]を作成しました！")    
    
bot.run(token)
