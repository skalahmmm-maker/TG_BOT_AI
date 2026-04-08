from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import app.keybords as kb
from app.generateGROK import ai_generate2
from app.generateDEEP import ai_generate

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Выберите модель ИИ",
        reply_markup=kb.vibor
    )


# Храним выбранную модель для каждого пользователя
user_states = {}


@router.callback_query(F.data.in_(["Deep", "Gr", "SF"]))
async def model_selection(callback: CallbackQuery):
    # Удаляем инлайн клавиатуру после выбора
    await callback.message.edit_reply_markup(reply_markup=None)
    
    
    model_name = {
        "Deep": "DeepSeek",
        "Gr": "Grok",
    }[callback.data]
    
    # Сохраняем выбор пользователя
    user_states[callback.from_user.id] = callback.data
    
    await callback.message.edit_text(f"Вы выбрали {model_name}. Введите ваш запрос:")
    await callback.answer()

@router.message()
async def handle_user_query(message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        await message.answer("Пожалуйста, сначала выберите модель ИИ с помощью команды /start")
        return
    
    model = user_states[user_id]
    query = message.text
    
    # Отправляем сообщение о том, что запрос обрабатывается
    processing_msg = await message.answer("Обрабатываю ваш запрос...")
    
    try:
        if model == "Gr":
            response = await ai_generate2(query)
        elif model == "Deep":
            response = await ai_generate(query)
        
            
        await processing_msg.edit_text(f"Ответ от {model}:\n\n{response}", reply_markup=kb.back)
    
    except Exception as e:
        await processing_msg.edit_text(f"Произошла ошибка: {str(e)}")
        print(f"Error: {e}")

@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        "Выберите модель ИИ",
        reply_markup=kb.vibor
    )
    return

@router.callback_query(F.data == 'next')
async def next_query(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_states:
        await callback.answer("Ошибка: модель не выбрана", show_alert=True)
        return
    
    model_name = {
        "Deep": "DeepSeek",
        "Gr": "Grok"
    }[user_states[user_id]]
    
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"Вы выбрали {model_name}. Введите ваш запрос:")
    await callback.answer()