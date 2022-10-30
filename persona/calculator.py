import discord


class Calculator:
    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널
        
        keys = ['+', '-', 'x', '/']
        functions = [int.__add__, int.__sub__, int.__mul__, int.__truediv__]
    
        for key, func in zip(keys, functions):
            if key in content:
                x, y = map(int, content.split(key))
                answer = func(x, y)
                await message.reply(answer)
                return True
