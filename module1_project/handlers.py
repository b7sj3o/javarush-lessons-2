import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards as kb

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    logging.info(f"Користувач {message.from_user.id} натиснув /start")

    await message.answer(
        text=f"Привіт, {message.from_user.first_name}!\n"
        "Тут ти можеш поспілкуватись з відомими особистомями, пройти квіз та дізнатись випадковий факт",
        reply_markup=kb.main_menu_kb
    )


@router.message(Command(commands=["help"]))
async def handle_start(message: Message):
    await message.answer(
        "Доступні команди:\n"
        "/start - Розпочати\n"
        "/help - Ця команда\n"
        "/random - Випадковий факт\n"
        "/gpt - Чат-бот"
    )


# @router.message(F.text.lower() == "привіт")
# async def handle_text(message: Message):
#     await message.answer("І тобі привіт!")


# F.text.in_({"так", "ні"}) # один із варіантів
# F.text.contains("бот") # підрядок
# F.text.regexp(r"^\d{4}$") # регулярний вираз
# F.text.len() > 100 # довжина
# F.from_user.id == 123456789 # конкретний користувач
# F.chat.type == "private" # лише приватні чати

# @router.message(F.photo | F.video)
# async def handle_photo_or_video(message: Message):
#     await message.answer("Це фото або відео")
#
#
# @router.message((F.text == "/admin") & (F.from_user.id == 1234567890))
# async def handle_photo_or_video(message: Message):
#     await message.answer("Це фото або відео")
#
#
# @router.message(F.text & ~F.text.startswith("/"))
# async def handle_random(message: Message):
#     await message.answer("Це не команда")
#
#
@router.message(F.text == kb.BTN_CHATBOT)
async def handle_text(message: Message):
    await message.answer("Заглушка чатбот")


@router.message(F.text == kb.BTN_FAMOUS_PERSON)
async def handle_text(message: Message):
    await message.answer("Обери особистість, з якою ти б хотів поспілкуватись:", reply_markup=kb.famous_people_inline_kb)


@router.callback_query(F.data.startswith("famous_person_"))
async def handle_famous_person(callback: CallbackQuery):
    await callback.message.answer(f"Ти натиснув: {kb.famous_people[callback.data]}")

    await callback.answer("Все ок!")
