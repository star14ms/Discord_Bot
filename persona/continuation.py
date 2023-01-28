import discord
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import random

from utils.unicode import check_hangul, is_hangul_compat_jamo, split_syllable_char, join_jamos_char


class Continuation:
    def __init__(self):
        self.last_char_dict = {}

    @staticmethod
    def get_html_soup(url: str):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req)
        soup = bs(html, "html.parser")
        return soup


    async def check(self, message: discord.message.Message):
        content = message.content # 메세지 내용
        channel = message.channel # 메세지 보낸 채널

        try:
            for char in content:
                check_hangul(char)
                assert not is_hangul_compat_jamo(char)
        except:
            return False

        last_char = self.last_char_dict.get(f'{message.guild} - {channel}')
    
        word_exists = Continuation._word_exists(content)
        is_continue_word = last_char is None or last_char == content[0]

        if not is_continue_word:
            last_char_secondary = Continuation._get_last_char_secondary(last_char)
            is_continue_word = last_char_secondary == content[0] 

        if not is_continue_word or not word_exists:
            if not word_exists:
                await message.reply('그런 단어는 없다!')
            elif not is_continue_word:
                secondary_info = f'({last_char_secondary})' if last_char_secondary is not None else ''
                await message.reply(f"'{last_char}{secondary_info}'(으)로 시작하는 말이 아니다!")
            
            await channel.send('내가 이겼다')
    
            # words = Continuation._search_answer_words(last_char)
            # words = random.sample(words, min(len(words), 5))
            last_char = None
            # await channel.send('({})'.format(', '.join(words)))
        else:
            words = Continuation._search_answer_words(content)

            if len(words) > 0:
                word = random.choice(words)
                last_char = word[-1]
                last_char_secondary = Continuation._get_last_char_secondary(last_char)
                secondary_info = f'({last_char_secondary})' if last_char_secondary is not None else ''
                await message.reply(word + secondary_info)
            else:
                last_char = None
                await channel.send('내가 졌다')

        self.last_char_dict.update([(f'{message.guild} - {channel}', last_char)])
    
        return True

    @staticmethod
    def _word_exists(content):
        url = f"https://kkukowiki.kr/&search={quote_plus(content)}&fulltext=1"
        soup = Continuation.get_html_soup(url)
        result = soup.find('ul', 'mw-search-results')
        
        if result is None:
            url = f"https://kkukowiki.kr/w/{quote_plus(content)}"
            try:
                Continuation.get_html_soup(url)
                # soup = Continuation.get_html_soup(url)
                # result = soup.find('div', 'mw-parser-output')
            except HTTPError as e:
                if not e.status == 404:
                    raise
                return False
    
        return True

    @staticmethod
    def _get_last_char_secondary(last_char):
        (initial, medial, final) = split_syllable_char(last_char)

        if initial in 'ㄴㄹ' and medial in 'ㅑㅕㅖㅛㅠㅣ':
            return join_jamos_char('ㅇ', medial, final)
        elif initial in 'ㄹ' and medial in 'ㅏㅐㅗㅚㅜㅡ':
            return join_jamos_char('ㄴ', medial, final)

    @staticmethod
    def _search_answer_words(content, is_secondary_search=False):
        last_char = content[-1]
        url = f"https://kkukowiki.kr/w/{quote_plus(f'역대_단어/한국어/{last_char}', safe='/')}"

        def _search_secondary_answer_words():
            if is_secondary_search:
                return []
            else:
                last_char_secondary = Continuation._get_last_char_secondary(last_char)
                if last_char_secondary is None:
                    return [] 
                else:
                    return Continuation._search_answer_words(last_char_secondary, is_secondary_search=True)

        try:
            soup = Continuation.get_html_soup(url)
        except HTTPError as e:
            if not e.status == 404:
                raise
            return _search_secondary_answer_words()

        tr_tags = soup.find('table', 'sortable').find_all('tr')
    
        if len(tr_tags) < 3:
            return _search_secondary_answer_words()
    
        words = [list(tr_tag.children)[-1].text.strip() for tr_tag in tr_tags[2:]]
        words = words + _search_secondary_answer_words()

        return words
