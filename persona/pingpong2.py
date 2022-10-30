import discord


class PingPong2:
    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널
    
        if '안녕' in content: # 특정 글자를 포함하면
            await message.reply('반가워')
            return True
