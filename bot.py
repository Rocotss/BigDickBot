import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from config_reader import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Start BigDickBot!")


@dp.message()
async def any_message(message):
    await message.reply(
        f"Hello, {message.from_user.id}"
    )


async def main():
    dp.message.register(any_message)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
