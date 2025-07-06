import discord
import datetime

try:
    from rich import print # Extra cool logs when rich library is installed (rich 라이브러리 설치 시 로그가 더 멋있어짐)
except:
    pass

from bot_base.command import bot
from persona import persona, Continuation


KST = datetime.timezone(datetime.timedelta(hours=9)) # UTC+9 Korea (KST) (한국 시간대)


@bot.event # When the bot is ready (봇이 준비되었을 때)
async def on_ready():
    bot.is_on_message_running = False

    print('\nLogged on as', bot.user)
    print('------')


@bot.event # When a message is sent (메세지가 올라올 때)
async def on_message(message: discord.message.Message):
    author = message.author.name
    now = message.created_at.astimezone(KST).replace(microsecond=0)
    
    print()
    print('{}, {} - {}'.format(now, message.guild, message.channel)) # now, server name - channel name
    print('{}: {}'.format(author, message.content)) # author: message content

    # don't respond to ourselves and prevent overlap
    if message.author == bot.user or bot.is_on_message_running:
        return
    # elif message.author == 'star14ms':
    #     return
        
    bot.is_on_message_running = True
    
    try:
        if message.content.startswith(bot.command_prefix):
            await bot.process_commands(message)
        elif message.guild is None or (
            'Continuation' not in [persona.__class__.__name__ for persona in persona.personas] and message.channel.name in ['병기실험장', '놀이터', '봇실험실']) or (
            'Continuation' in [persona.__class__.__name__ for persona in persona.personas] and message.channel.name in ['끝말잇기', 'continuation']
        ):
            await persona.reply(message)
    except Exception as e:
        print(e)

    print('------')
    bot.is_on_message_running = False
