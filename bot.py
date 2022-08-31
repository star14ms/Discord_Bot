import discord
from rich import print

from config import token, KST
from persona import GungYe, LastChatReminder, DDorai


class MyClient(discord.Client):
    async def on_ready(self):
        self.GungYe = GungYe()
        self.LastChatReminder = LastChatReminder(tzinfo=KST)
        self.DDorai = DDorai()
        self.is_on_message_running = False

        print('\nLogged on as', self.user)
        print('------')

    async def on_message(self, message):
        # don't respond to ourselves and prevent overlap
        if message.author == self.user or self.is_on_message_running:
            return

        self.is_on_message_running = True
        
        author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
        
        print()
        print(message.created_at.astimezone(KST).replace(microsecond=0))
        print(message.channel, message.guild, sep=' - ') # 메세지 올라온 서버 / 채팅방
        print(author, message.content, sep=': ') # 메세지 친 사람 / 메세지 내용
        
        response_message = await self.GungYe.gwansimbeop(message)
        if not response_message:
            response_message = await self.LastChatReminder.check(message, message.content)
        if not response_message:
            await self.DDorai.check(message)

        print('------')
        self.is_on_message_running = False
    

if __name__ == '__main__':

    intents = discord.Intents.default()
    intents.message_content = True
    
    client = MyClient(intents=intents)
    client.run(token)
