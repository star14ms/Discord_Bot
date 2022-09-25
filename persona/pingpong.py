import discord


class PingPong:
    def __init__(self) -> None:
        pass

    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널

        if content == 'ping':
            await channel.send('pong') # 채널에 메세지 보내기
            return True
