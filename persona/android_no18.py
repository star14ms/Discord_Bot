import discord
import random
import time


class Android_No18:
    def __init__(self) -> None:
        self.eojjeol_stack = 0
        self.eojjeol_flows = ['어쩔티비', '저쩔티비', '어쩔냉장고', '저쩔세탁기', '어쩔스타일러', '저쩔가습기', '어쩔초고속진공블랜딩믹서기']
        self.turned_on = False
    async def check(self, message: discord.message.Message):
        content = message.content
        channel = message.channel
        
        if not self.turned_on:
            ran = random.randint(1, 10)
            if ran == 1:
                await channel.send('시끄럽네')
                self.turned_on = True
                return True
            else:
                return False

        if content == 'ping':
            await message.reply('pong')
            
        elif content == '?':
            await channel.send('?')

        elif content == '응~':
            await channel.send('아니야~')
        
        elif content.rstrip('!') in ['와', 'WA']:
            await message.reply('샌즈' + '!' * content.count('!'))

        elif '샌즈' in content:
            await message.reply('와! 언더테일 아시는구나!')
            time.sleep(0.8)
            await channel.send('겁.나.어.렵.습.니.다.')

        elif content == '어쩔초고속진공블랜딩믹서기' or (
            ('어쩔' in content or '저쩔' in content) and self.eojjeol_stack >= 3):
            await message.reply('어쩔어쩔~ 저쩔저쩔~')
            time.sleep(0.8)
            await channel.send('안물티비~ 안궁티비~ 뇌절티비~')
            time.sleep(0.8)
            await channel.send('우짤래미~ 저짤래미~ 쿠쿠루삥뽕')
            time.sleep(0.8)
            self.eojjeol_stack = 0

        elif content in self.eojjeol_flows:
            text = self.eojjeol_flows[self.eojjeol_flows.index(content)+1]
            await message.reply(text)
            self.eojjeol_stack += 1
        
        else:
            ran = random.randint(1, 50)
            if ran == 1:
                await channel.send('어쩔티비')
            elif ran == 2:
                await channel.send('띠용')
            elif ran == 3:
                await channel.send('뿡')
            elif ran == 4:
                await message.pin()
            elif ran == 5:
                await channel.send('저기요, 뭐라고요?')
            elif ran == 6:
                await channel.send('바ㅡ보!!!! 나랑 17호는 쌍둥이 남매야!')
                time.sleep(2)
                await channel.send('그렇다고 날 넘볼 생각 하지 마! 폭탄 제거한 것도 안 고마워!')
                time.sleep(2)
                await channel.send('이 문어 대가리야!')
                time.sleep(5)
                await channel.send('https://media1.tenor.com/m/gHetGKnjtPEAAAAC/krillin-android-18.gif')
                time.sleep(3)
                await channel.send('https://media1.tenor.com/m/qA3Eb9VhDHUAAAAC/krillin-eyebrows.gif')
                time.sleep(1)
                await channel.send('https://media1.tenor.com/m/bfwyHpyc3W0AAAAC/krillin-taunt.gif')
                time.sleep(3)
                await channel.send('https://media1.tenor.com/m/TPm5pDK5FmIAAAAC/hu006.gif')
            elif ran == 7:
                await channel.send('https://media1.tenor.com/m/itnjbqBkYqkAAAAC/android18-vegeta.gif')
            elif ran == 8:
                await channel.send('https://media1.tenor.com/m/Pn_PPHCwH44AAAAd/watch-yo-tone-vegeta.gif')
            elif ran == 9:
                await channel.send('https://media1.tenor.com/m/_cu_D0m8aDMAAAAC/dragonball-z-anime.gif')
            elif ran == 10:
                await channel.send('https://media1.tenor.com/m/mAFgmLidlTAAAAAC/dbz.gif')
            elif ran == 11:
                await channel.send('https://media1.tenor.com/m/963xvnBPiAwAAAAC/what-do-you-want-what-are-you-doing.gif')
            elif ran == 12:
                await channel.send('https://media1.tenor.com/m/YdlLsVPIVJ4AAAAC/dragon-ball-dragon-ball-z.gif')
            elif ran == 13:
                await channel.send('https://media1.tenor.com/m/beD39Ueb6poAAAAC/dbz-android18.gif')
            elif ran == 14:
                self.turned_on = False
            elif ran in range(15, 20):
                return False
            else:
                return True

        return True # 전송한 메세지 - 있음:True / 없음:False
        