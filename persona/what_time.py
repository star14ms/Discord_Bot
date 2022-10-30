import discord
from datetime import datetime


days = ['월', '화', '수', '목', '금', '토', '일']


class WhatTime:
    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널
    
        if '몇 시' in content or ('언제' in content and ('궁금' in content or '알' in content)):
            now = datetime.now() # 현재 시간 정보
    
            day_code = now.weekday() # 0~7
            day = days[day_code]
    
            datetime_str = now.strftime('%Y년 %m월 %d일 %H시 %M분')
    
            await channel.send(f'{datetime_str} ({day})')
            return True
