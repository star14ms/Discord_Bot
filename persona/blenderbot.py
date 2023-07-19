import discord
from transformers import AutoTokenizer, BlenderbotForConditionalGeneration
import googletrans


# Load the model and tokenizer
mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)
translator = googletrans.Translator()


def translate_to_english(func):
    def wrapper(self, content, author):
        lang_input = translator.detect(content).lang
        is_english = lang_input == 'en'

        if not is_english:
            content = translator.translate(content, dest='en').text
            print('en ->', content)
        return_value = func(self, content, author)
        # if not is_english:
        #     print('en ->', return_value)
        #     return_value = translator.translate(return_value, dest=lang_input).text
        
        return return_value

    return wrapper


class Blenderbot:
    def __init__(self):
        self.conversation_history = {}
        self.max_length = 100

    async def run(self, message: discord.message.Message):
        start_time = discord.utils.utcnow()
        response = self._generate_response(message.content.replace('!채팅', '').replace('!chat', '').strip(), message.author)
        time_delta = discord.utils.utcnow() - start_time
        print(f"\nTime: {time_delta.total_seconds():.3f} seconds")

        print("Bot: ", response)

        await message.reply(response)
        return True
    
    @translate_to_english
    def _generate_response(self, content: str, author: str):
        conversation_history = self.conversation_history.get(author, [])
        if conversation_history == []:
            self.conversation_history[author] = conversation_history

        # Add user input to conversation history
        conversation_history.append(content)

        # Prepare model inputs
        model_input = ' '.join(f'<s> {turn} </s>' for turn in conversation_history)
        inputs = tokenizer([model_input], return_tensors="pt")

        while len(inputs["input_ids"][0]) > self.max_length:
            print('input length:', len(inputs["input_ids"][0]))
            conversation_history = conversation_history[1:]
            model_input = ' '.join(f'<s> {turn} </s>' for turn in conversation_history)
            inputs = tokenizer([model_input], return_tensors="pt")

        # Generate a response
        reply_ids = model.generate(**inputs, max_length=self.max_length)
        response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]

        # Add model response to conversation history
        conversation_history.append(response)

        return response
