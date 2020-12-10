from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1482545755:AAFi4Y1opYdTSgN468iOhPWTSgB1JbVEEPU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# פקודות
@dp.message_handler(commands=['עזרה', 'start'])
async def handle_command(message: types.Message):
    """
    הפונקציה הזאת תגיד לפקודות ספציפיות.
    כלומר אם תכתבו לבוט start/ למשל

    הערה - ברגע שהפונקציה הזאת טיפלה בהודעה, הפונקציות אחריה לא יופפעלו, כלומר, לא תקבלו את מה שקיבלתם מפונקציית echo
    """
    await message.reply("היי! הכנסת את אחת הפקודות!")


# טקסט ספציפי
@dp.message_handler(lambda message: message.text == 'שלום')
async def handle_shalom_text(message: types.Message):
    """
    הפונקציה הזאת תגיב אך ורק לטקסט "שלום"
    """
    await message.reply("שלום גם לך!")


# מילה בתוך טקסט
@dp.message_handler(lambda message: "פיצה" in message.text)
async def handle_shalom_in_text_handler(message: types.Message):
    """
    הפונקציה הזאת תגיב, במקרה ויש את המילה "שלום" בטקסט
    """
    await message.reply("שלום! אנחנו מקום ממש לא דמיוני וכן קיים שמחלק פיצה ובירה חינם, מה תרצו להזמין?")


# --------------------- קוד מחלק א

@dp.message_handler()
async def echo(message: types.Message):
    """
    הפונקציה הזאת תגיב לכל סוג של הודעת טקסט
    ותחזיר לכם מה שכתבתם
    """
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
