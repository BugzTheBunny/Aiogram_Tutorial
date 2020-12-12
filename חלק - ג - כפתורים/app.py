from aiogram import Bot, Dispatcher, executor, types
import keyboard # מושכים את המקלדת

API_TOKEN = '1482545755:AAFi4Y1opYdTSgN468iOhPWTSgB1JbVEEPU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(message.text, 
                        reply_markup=keyboard.welcome_keyboard # קריאה למקלדת בתור תשובה
                        )

#  אז נראה להיות מנומסים ולהגיב לוHello! הכפתור כותב את המילה 
@dp.message_handler(lambda message: message.text == 'Hello!')
async def handle_shalom_text(message: types.Message):
    await message.reply("Hello to you!, איזה תוספות תרצה על הפיצה?",
                        reply_markup=keyboard.pizza_keyboard # מקלדת פיצה
                       )
# יגיב לתוספות על הפיצה, ויציע גודל של פיצה    
@dp.message_handler(lambda message: message.text in ['עם אקסטרה גבינה','עם זיתים','עם טונה'])
async def handle_shalom_text(message: types.Message):
    await message.reply("Size of pizza?",
                        reply_markup=keyboard.size_keyboard # מקלדת פיצה
                       )
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
