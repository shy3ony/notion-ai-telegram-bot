import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

TELEGRAM_TOKEN = "8129671831:AAEvmBKaF0oGcV5O-S-lnpuI4yvF3hL0SvQ"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

web3_url = "https://notion-and-ai-bot.vercel.app"  # Публичная страница

@dp.message(Command("start"))
async def start_handler(message: Message):
    photo = FSInputFile("static/img/brain.png")
    caption = (
        "<b>Notion & AI — сообщество для обмена опытом, идеями и инструментами по работе с искусственным интеллектом и Notion.</b>\n\n"
        "Здесь вы найдёте полезные материалы, уроки, новости и сможете пообщаться с единомышленниками!"
    )
    await message.answer_photo(photo, caption=caption, parse_mode="HTML")
    # Одна кнопка callback, вторая с url
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть меню группы Notion & AI", url=web3_url)],
            [InlineKeyboardButton(text="Instagram группы", url="https://www.instagram.com/notion.and.ai/?igsh=eHRzcXByODJtaWsx#")]
        ]
    )
    await message.answer(
        "<b>Добро пожаловать!</b> Нажмите одну из кнопок ниже, чтобы открыть меню группы Notion & AI или Instagram.\n\n/help — список команд и их описание.",
        reply_markup=inline_kb, parse_mode="HTML"
    )

@dp.message(Command("help"))
async def help_handler(message: Message):
    text = (
        "<b>Доступные команды:</b>\n"
        "/start — приветствие, картинка, кнопка для перехода в меню группы и на сайт.\n"
        "/link_for_notion_and_ai — получить приглашение в группу и приветственное сообщение для новых участников.\n"
        "/help — список команд и их описание.\n"
        "\n"
        "<b>Примечание:</b> Кнопки для перехода на сайт-меню появляются после команды /start.\n"
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(Command("link_for_notion_and_ai"))
async def link_for_notion_and_ai_handler(message: Message):
    group_link = "https://t.me/+1iaRRpDUcos3MjMy"
    text = (
        "<b>Приветствую тебя, Путник,</b> который пытается разобраться в нейросетях.\n"
        "<b>Проходи по ссылке</b> и <b>присоединяйся</b> к нам, чтобы путь был легче и уверенней!\n\n"
        f"{group_link}"
    )
    await message.answer(text, parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 