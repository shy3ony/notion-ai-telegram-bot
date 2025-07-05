import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'PASTE_YOUR_TOKEN_HERE')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message):
    await message.answer('Бот работает!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 