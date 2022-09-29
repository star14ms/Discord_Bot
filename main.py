import discord
from discord.ext import commands

try:
    from rich import print # rich 라이브러리 설치 시 로그가 더 멋있어짐
except:
    pass

from config import token, KST
from persona import Persona


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
persona = Persona()


@bot.event # 봇이 실행될 때
async def on_ready():
    bot.is_on_message_running = False

    print('\nLogged on as', bot.user)
    print('------')


@bot.event # 서버에서 메세지를 감지했을 때
async def on_message(message: discord.message.Message):
    # don't respond to ourselves and prevent overlap
    if message.author == bot.user or bot.is_on_message_running:
        return

    bot.is_on_message_running = True
    
    author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
    now = message.created_at.astimezone(KST).replace(microsecond=0)
    
    print()
    print(f'{now}, {message.guild} - {message.channel}') # 메세지 올라온 시각 / 서버 / 채널
    print(author, message.content, sep=': ') # 메세지 친 사람 / 메세지 내용
    
    if message.content.startswith('!'):
        await bot.process_commands(message)
    else:
        await persona.use(message)

    print('------')
    bot.is_on_message_running = False
    

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.


@bot.command(name='마지막채팅')
async def _lastchat(ctx, member: str = None):
    if member is not None:
        await persona.LastChatReminder.check(ctx.message, member)
    else:
        await ctx.message.reply('!마지막채팅 [유저이름]')
    

if __name__ == '__main__':
    bot.run(token)
