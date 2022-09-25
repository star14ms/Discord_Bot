import discord

from config import KST
from persona.ddorai import DDorai
from persona.gungye import GungYe
from persona.last_chat_reminder import LastChatReminder
from persona.pingpong import PingPong


class Persona:
    def __init__(self) -> None:
        self.PingPong = PingPong()
        self.GungYe = GungYe()
        self.LastChatReminder = LastChatReminder(tzinfo=KST)
        self.DDorai = DDorai()

    async def use(self, message: discord.message.Message):
        message_sended = await self.PingPong.check(message)
        if not message_sended: # 여러 페르소나가 동시에 메세지를 보내지 않게 만들기
            message_sended = await self.GungYe.gwansimbeop(message)
        if not message_sended:
            message_sended = await self.DDorai.check(message)
        
        self.LastChatReminder.save_last_chat(message)
