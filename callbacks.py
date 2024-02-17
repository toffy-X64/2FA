from config import *



# Інформація
@dp.callback_query(F.data == "info_callback") # Перехватити калбек ( треба імпортувати F  )
async def send_rand_val(callback: types.CallbackQuery):
    await callback.message.answer( "INFORMATION" )
    await callback.answer(text = "+", show_alert=True) # Показати вспливаюче вікно


# Прив'язати ігровий акаунт
@dp.callback_query(F.data == "connect_game_account")
async def connect_account(callback: types.CallbackQuery):
    user = callback.from_user

    chat_id = callback.message.chat.id
    print(chat_id)
    user_id = user.id


    code = randint(100000, 999999)
    
    query = mta.callFunction('2FA', 'AddNewCode', code, chat_id, user_id)

    if query[0] == "code_already_is":
        code = randint(100000, 999999)
        query = mta.callFunction('2FA', 'AddNewCode', code, chat_id, user_id)
    elif query[0] == "ok":
        await callback.message.answer(f"Ваш код - {hbold(code)}\nУ грі відкрийте меню (F1) Налаштування -> 2FA Та введіть цей код.\nПісля чого ваш акаунт буде прив'язано\n{hbold('Код дійсний 5 хвилин!')}")
    elif query[0] == "no-code":
        await callback.message.answer(f"{hbold('Нажать сталася помилка на стороні серверу.')}\nСпробуйте пізніше")
    else:
        await callback.message.answer(f"{hbold('Нажать сталася помилка на стороні серверу.')}\nСпробуйте пізніше")

    
