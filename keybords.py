from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


vibor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='DeepSeek', callback_data='Deep')],
    [InlineKeyboardButton(text='Grok', callback_data='Gr')]])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернутся к выбору модели', callback_data='back')],
    [InlineKeyboardButton(text='Следущий запрос', callback_data='next')]
])