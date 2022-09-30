import discord


class PingPong:
    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널

        if content == 'ping':
            await message.reply('pong') # 답장 보내기
            return True
