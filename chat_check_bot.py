import discord
import random
from config import token, KST

latest_time = {}
latest_message = {}

class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user)
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
        now = message.created_at.astimezone(KST).replace(microsecond=0) # 마이크로초 생략
        
        print()
        print(author) # 메세지 친 사람
        print(now) # 메세지 친 시각
        print(message.content) # 메세지 내용

        if message.content in latest_time:
            ran = random.randrange(0, 2)
            await message.channel.send(f"{latest_time[message.content]} ({now - latest_time[message.content]} 전)") # 저장된 시간과 차이
            if ran == 0:
                await message.channel.send(f'"{latest_message[message.content]}" 라고 지껄였다')
            else:
                await message.channel.send(f'"{latest_message[message.content]}" 라며 나불댔다')


        elif message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == '응~':
            await message.channel.send('아니야~')
        
        elif message.content == '...':
            await message.channel.send('점점점...')
        
        else:
            ran = random.randrange(1,20)
            if ran == 1:
                await message.channel.send('어쩌라고')
            elif ran == 2:
                await message.channel.send('응 아니야~')
            elif ran == 3:
                await message.channel.send('그래서 뭐')

        # 사람마다 가장 최근의 최근 메세지 보낸 시각, 메세지 내용 저장
        latest_time[author] = now
        latest_message[author] = message.content


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = MyClient(intents=intents)
    client.run(token)

################################################################################

# from discord.ext import commands

# bot = commands.Bot(command_prefix='>')

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run(token)

################################################################################

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run('your token here')