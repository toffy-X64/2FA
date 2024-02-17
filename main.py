

from callbacks import *

@dp.message(CommandStart())
async def Menu(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()

    # Робимо клавіатуру
    for i in MainMenu["Big-Buttons"]:
        builder.row(i)

    builder.row(*MainMenu["Links"])



    #photo = "https://yt3.googleusercontent.com/TFfed0DOHKIxo42YNWq5Be7jeOqSienhgRik1kc3L2CsWPQjx8v_IkuFkfwhqUir7w58S2FVNg=s900-c-k-c0x00ffffff-no-rj"
    #await message.answer(f"<a href='{photo}'> </a> Вітаю, {hbold('Toffy')}!\n\nЯ — твій віртуальний помічник у світі {hbold(NAME)}.\n\nДля початку, обери бажану дію: ", photo = photo, reply_markup=builder.as_markup())

    photo = "https://yt3.googleusercontent.com/TFfed0DOHKIxo42YNWq5Be7jeOqSienhgRik1kc3L2CsWPQjx8v_IkuFkfwhqUir7w58S2FVNg=s900-c-k-c0x00ffffff-no-rj"
    
    await message.answer_photo(
        photo=types.URLInputFile(
            url=photo,
            filename=f"picture.png"
        ), caption=f"Вітаю, {hbold('Toffy')}!\n\nЯ — твій віртуальний помічник у світі {hbold(NAME)}.\n\nДля початку, обери бажану дію:", reply_markup=builder.as_markup()
    )



async def main():
    bot = Bot("6787488978:AAEbgz4vFt2nheAzLvLLus49HxUoEzrIx0c", parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream = stdout)
    asyncio.run(main()) # запуск бота


