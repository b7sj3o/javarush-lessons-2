from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

BTN_CHATBOT = "Чат-бот"
BTN_FACT = "Цікавий факт"
BTN_FAMOUS_PERSON = "Відома особистість"
BTN_SETTINGS = "Налаштувананя"


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BTN_CHATBOT),
            KeyboardButton(text=BTN_FACT),
            KeyboardButton(text=BTN_FAMOUS_PERSON),
        ],
        [
            KeyboardButton(text=BTN_SETTINGS)
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Обери пункт меню",
)


famous_people = {
    "famous_person_1": "Арнольд Шварцнегер",
    "famous_person_2": "Ілон Маск",
    "famous_person_3": "Віталій Федитник"
}

famous_people_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=name, callback_data=callback)]
        for callback, name in famous_people.items()
    ]
)