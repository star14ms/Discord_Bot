import random

import discord
from discord.ext import commands
from discord.ext.commands.context import Context
try:
    import googletrans
except:
    pass

from persona import persona


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def ping(ctx: Context):
    await ctx.send(f'pong! {round(round(ctx.bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.


@bot.command(name='뽑기')
async def random_choose(ctx: Context, number: int = None, n_choice: int = None):
    if number is None and n_choice is None:
        await ctx.message.reply('```!뽑기 [총 숫자] [뽑을 숫자]```')
    elif n_choice is None:
        choice = random.sample(range(1, number+1), 1)
        await ctx.message.reply(f'뽑은 숫자\n{sorted(choice)}')
    else:
        choice = random.sample(range(1, number+1), n_choice)
        await ctx.message.reply(f'뽑은 숫자\n{sorted(choice)}')


@bot.command(name='마지막채팅')
async def lastchat(ctx: Context, member: str = None):
    if persona.lastchatreminder is None:
        return 

    if member is None:
        await ctx.message.reply('```!마지막채팅 [유저이름]```')
    else:
        await persona.lastchatreminder.run(ctx.message, member)


@bot.command(aliases=['번역', 'translate'])
async def _translate(ctx: Context, *args):
    if googletrans is None:
        return await ctx.reply('```pip install googletrans```')

    embed = discord.Embed(
        title='언어 코드 종류',
        url='https://developers.google.com/admin-sdk/directory/v1/languages/',
        description='Languages Codes'
    )
    help = '```!번역 [언어 코드] [텍스트]```'

    if len(args) == 0:
        await ctx.message.reply(help, embed=embed)
        return
    elif len(args) == 1:
        lang, text = 'en', args[0]
    else:
        lang, text = args[0], args[1]

    try:
        translator = googletrans.Translator()
        result = translator.translate(text, dest=lang).text

        await ctx.message.reply(f"{text} => {result}")

    except ValueError as e:
        await ctx.message.reply(help, embed=embed)

    except Exception as e:
        print(repr(e))


@bot.command(aliases=['채팅'], help='clear user\'s conversation history')
async def chat(ctx):
    if not persona.blenderbot:
        return

    await persona.blenderbot.run(ctx.message)
