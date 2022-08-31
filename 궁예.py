import discord
import random
import time, datetime

token = '' ## 여기다 자신의 봇 토큰 붙여넣기 ##
latest_time = {}
latest_message = {}

class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user)
        self.opening = False
        self.achoo = False
        self.sin = False
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
        
        print()
        print(author) # 메세지 친 사람
        print(message.content) # 메세지 내용
        print(message.channel)
    

        if message.content == 'ping':
            await message.channel.send('pong')

        elif '궁예' in message.content and not self.opening:
            self.opening = True
            await message.channel.send('도대체 그대들이 이 나라의 벼슬아치들인지,')
            time.sleep(1)
            await message.channel.send('아니면 뒷간의 똥막대기인지')
            time.sleep(1)
            await message.channel.send('그걸 알 수가 없단 말이야.')
            time.sleep(5)
            await message.channel.send('그대들 모두 하나같이')
            time.sleep(1)
            await message.channel.send('똥으로 가득차있어, 똥 말이야')

        elif '에취' in message.content and self.achoo == False:
            await message.channel.send('누구인가?')
            time.sleep(2)
            await message.channel.send('지금 누가 기침 소리를 내었어?')
            self.achoo = True

        elif '신이옵니다' in message.content and self.achoo == True:
            await message.channel.send('참으로 딱하구나.')
            time.sleep(1)
            await message.channel.send('짐이 지금 관심법을 하고 있는데,')
            time.sleep(1)
            await message.channel.send('어찌 기침을 할 수 있느냐 이 미련한 것아아!!')
            self.sin = True

        elif ('송구하옵니다' in message.content or '용서하여 주시옵소서' in message.content) and self.sin == True:
            await message.channel.send('내가 가만히 보니,')
            time.sleep(1)
            await message.channel.send('니놈 머릿속엔 마구니가 가득찼구나.')
            await message.channel.send('이제 더 이상의 대사는 없다.')

        # 사람마다 가장 최근의 최근 메세지 보낸 시각, 메세지 내용 저장
        latest_message[author] = message.content

        print('------')
    

if __name__ == '__main__':

    intents = discord.Intents.default()
    intents.message_content = True
    
    client = MyClient(intents=intents)
    client.run(token)
