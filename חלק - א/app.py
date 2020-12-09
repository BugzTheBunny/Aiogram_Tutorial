from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1482545755:AAFi4Y1opYdTSgN468iOhPWTSgB1JbVEEPU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    print(message)  # ידפיס לכם את ההודעה איך שהיא נראית בשביל הפונקציה
    # await message.answer("Hello!") יחזיר לנו רק hello
    await message.answer(message.text)  # יחזיר לנו את הטקסט שאנחנו כתבנו


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
