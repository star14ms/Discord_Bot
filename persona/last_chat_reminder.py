import discord
import random
import datetime


KST = datetime.timezone(datetime.timedelta(hours=9)) # UTC+9 대한민국 (KST)


class LastChatReminder:
    def __init__(self, tzinfo: datetime.tzinfo = KST) -> None:
        self.tzinfo = tzinfo
        self.latest_time = {}
        self.latest_message = {}

    async def check(self, message: discord.message.Message, member: str):
        author, sharp_num = str(message.author).split('#') # 이름#1234 형태를 #을 기준으로 분리
        now = message.created_at.astimezone(self.tzinfo).replace(microsecond=0) # 마이크로초 생략
        content = message.content
        channel = message.channel

        if member in self.latest_time:
            ran = random.randrange(0, 2)
            await channel.send(f"{self.latest_time[content]}에 ({now - self.latest_time[content]} 전)") # 저장된 시간과 차이
            if ran == 0:
                await channel.send(f'{member}(이)가 "{self.latest_message[content]}" (이)라고 지껄였구나')
            else:
                await channel.send(f'{member}(이)가 "{self.latest_message[content]}" (이)라며 나불댔구나')
    
        # 사람마다 가장 최근의 최근 메세지 보낸 시각, 메세지 내용 저장
        self.latest_time[author] = now
        self.latest_message[author] = content
        
        if member in self.latest_time:
            return True
        else:
            return False