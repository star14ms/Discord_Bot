import discord


class PartTimer:
    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널
    
        if '주문할게요' in content:
            answer = content.replace('주문할게요', '주문 받았습니다') # 문자 교체
            await message.reply(answer)
            return True
