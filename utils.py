from rich.syntax import Syntax
from rich.text import Text
from rich import print
import discord


def getattrs_and_print_all(something):
    """특정 개체가 가지고 있는 모든 속성에 접근해본다."""
    
    for attr_name in dir(something):
        try:
            attr = getattr(something, attr_name)
            attr_name_str = Text(f'~.{attr_name}')

            if callable(attr):
                print(Syntax(f'{attr_name_str} = {attr()}', "python", theme="monokai", word_wrap=True))
            elif attr is None:
                print(Syntax(f'{attr_name_str} = {None}', "python", theme="monokai", word_wrap=True))
            else:
                print(Syntax(f'{attr_name_str} = {attr}', "python", theme="monokai", word_wrap=True))
        except:
            pass



def get_channel(channel_name: str, message: discord.message.Message = None, guild: discord.guild.Guild = None):
    """채널 이름을 넣으면 그 채널 오브젝트를 돌려준다. (메세지나 서버(길드) 필요)"""

    if message:
        guild = message.guild

    channels = list(filter(lambda x: x.name == channel_name, guild.text_channels))
    
    if len(channels) == 0:
        return None
    elif len(channels) == 1:
        return channels[0]
    else:
        return channels
