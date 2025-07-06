import discord
from openai import OpenAI

import os
from dotenv import load_dotenv


class OpenAIChat:
    def __init__(self):
        load_dotenv()
      
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI()
        self.system_message = \
'''Act as if you are a playful member of a discord server about coding. Reply chats casually in their language.'''

    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널

        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": content},
            ]
        )
        
        await message.reply(completion.choices[0].message.content)
        
        return True
