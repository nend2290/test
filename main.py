import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена из переменной окружения
TOKEN = os.getenv('DISCORD_TOKEN')

# Настройки намерений
intents = discord.Intents.default()
intents.message_content = True

# Создание клиента бота с новым префиксом "!"
bot = commands.Bot(command_prefix='!', intents=intents)

replacement_dict = {
    'a': '丹', 'b': '乃', 'c': '匚', 'd': 'Ð', 'e': 'ê', 'f': '下', 'g': 'g',
    'h': '卄', 'i': '工', 'j': 'ʝ', 'k': 'Ｋ', 'l': 'l', 'm': '爪', 'n': 'ñ',
    'o': '口', 'p': 'ㄗ', 'q': 'Ｑ', 'r': '尺', 's': 'Ṡ', 't': 't', 'u': '∪',
    'v': 'v', 'w': 'w', 'x': '×', 'y': 'ㄚ', 'z': '乙'
}

def replace_letters(text):
    result = []
    for char in text:
        if char.lower() in replacement_dict:
            if char.isupper():
                result.append(replacement_dict[char.lower()].upper())
            else:
                result.append(replacement_dict[char.lower()])
        else:
            result.append(char)
    return ''.join(result)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Создание команды !fakechat
@bot.command()
async def fc(ctx, tag: str, *, message: str = 'No message provided'):
    if ctx.channel.name != 'fakechat':
        await ctx.send("dawg use it only in https://discord.com/channels/1272180732768555119/1272450701217370225 .")
        return
    
    formatted_message = f'{"#" * 57}[{tag}]: {message}'
    await ctx.send(f'```{formatted_message}```')

@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")  # отладка
    
    if message.author == bot.user:
        return

    # Замена букв только в канале Bypasser
    if message.channel.name == 'bypasser':
        transformed_text = replace_letters(message.content)
        
        if transformed_text:
            await message.channel.send(f'```{transformed_text}```')

    # Обработка команд
    await bot.process_commands(message)

# Запуск бота
bot.run(TOKEN)
