
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from urllib.parse import quote

import os
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Не найден BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🔎 SHADOW FINDER\n\n"
        "Добро пожаловать!\n"
        "/nick — поиск по нику\n"
        "/help — помощь"
    )

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "🔎 Команды бота:\n"
        "/nick username — поиск публичной информации"
    )

@dp.message(Command("nick"))
async def nick(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer("Напиши: /nick username")
        return

    username = parts[1].strip().lstrip("@")

    if len(username) > 50:
        await message.answer("Слишком длинный ник.")
        return

    query = quote(username)

    await message.answer(
        f"🔎 Поиск: @{username}\n\n"
        f"Google: https://www.google.com/search?q={query}\n"
        f"Bing: https://www.bing.com/search?q={query}\n"
        f"GitHub: https://github.com/{username}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
