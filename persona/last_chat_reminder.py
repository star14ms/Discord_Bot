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
        now = message.created_at.astimezone(self.tzinfo).replace(microsecond=0) # 마이크로초 생략

        if member in self.latest_time:
            latest_message_time = self.latest_time[member].replace(microsecond=0)
            time_info = f"{latest_message_time.strftime('%Y/%m/%d, %H:%M:%S')}에 ({now - latest_message_time} 전)" # 저장된 시간과 차이
            ran = random.randint(1, 2)
            if ran == 1:
                await message.reply(f'{time_info}\n{member}(이)가 "{self.latest_message[member]}" (이)라고 지껄였구나')
            else:
                await message.reply(f'{time_info}\n{member}(이)가 "{self.latest_message[member]}" (이)라며 나불댔구나')
        else:
            await message.reply(f'{member}(이)는 조용하구나')

        if member in self.latest_time:
            return True
        else:
            return False
    
    def save_last_chat(self, message):
        now = message.created_at.astimezone(self.tzinfo)
        
        # 사람마다 가장 최근의 최근 메세지 보낸 시각, 메세지 내용 저장
        self.latest_time[message.author.name] = now
        self.latest_message[message.author.name] = message.content
        