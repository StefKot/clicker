import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config 

def webapp_builder():
    builder= InlineKeyboardBuilder()
    builder.button(
        text="👶🏼 Let's click! 👶🏼", web_app=WebAppInfo(
            url=config.url
        )
    )
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        "Click! Click! Click!",
        reply_markup=webapp_builder()
        )

async def main():
    bot = Bot(config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())