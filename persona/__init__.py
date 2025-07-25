import discord

from persona.copycat import CopyCat # 난이도 순 (제일 쉬움)
from persona.pingpong import PingPong
from persona.pingpong2 import PingPong2
from persona.part_timer import PartTimer
from persona.calculator import Calculator
from persona.wa_sans import WASans
from persona.android_no18 import Android_No18
from persona.gungye import GungYe
from persona.what_time import WhatTime
from persona.last_chat_reminder import LastChatReminder
from persona.gif_villain import GIF_Villain
from persona.continuation import Continuation
from persona.openai_chat import OpenAIChat
# try:
#     from persona.blenderbot import Blenderbot
# except ImportError:
#     pass


class Persona:
    def __init__(self) -> None:
        # The place where personas are applied (Executed one by one until a message is sent
        # 페르소나 적용하는 곳 (위에서부터 하나씩 메세지를 보낼 때까지 실행됨)
        self.personas = [ # Change the order of the personas to change the priority
            PingPong(),
            GIF_Villain(), 
        ]
        # self.personas = [ # Change the order of the personas to change the priority
        #     # OpenAIChat(),
        #     Continuation(),
        # ]

        for persona in self.personas:
            self.__setattr__(persona.__class__.__name__.lower(), persona)

    async def reply(self, message: discord.message.Message):
        message_sended = False

        for persona in self.personas:
            # Prevent multiple personas from sending messages at the same time
            # 여러 페르소나가 동시에 메세지를 보내지 않게 만들기
            if not message_sended and persona.check is not None:
                message_sended = await persona.check(message)
            else:
                break

        if hasattr(self, 'lastchatreminder'):
            self.lastchatreminder.save_last_chat(message)


persona = Persona()
