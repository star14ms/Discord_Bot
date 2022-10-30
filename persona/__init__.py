import discord

from persona.copycat import CopyCat
from persona.gif_villain import GIF_Villain
from persona.gungye import GungYe
from persona.last_chat_reminder import LastChatReminder
from persona.pingpong import PingPong
from persona.wa_sans import WASans


class Persona:
    def __init__(self) -> None:
        self.CopyCat = CopyCat()
        self.PingPong = PingPong()
        self.GIF_Villain = GIF_Villain()
        self.GungYe = GungYe()
        self.LastChatReminder = LastChatReminder()
        self.WASans = WASans()

        self.personas = [ # 페르소나 적용하는 곳 (위에서부터 하나씩 실행됨)
            self.PingPong.check, 
            self.CopyCat.copy,
        ]

    async def use(self, message: discord.message.Message):
        message_sended = False

        for persona in self.personas:
            if not message_sended: # 여러 페르소나가 동시에 메세지를 보내지 않게 만들기
                message_sended = await persona(message)
            else:
                break
        
        self.LastChatReminder.save_last_chat(message)


persona = Persona()
