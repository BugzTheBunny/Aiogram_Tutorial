from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1482545755:AAFi4Y1opYdTSgN468iOhPWTSgB1JbVEEPU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
