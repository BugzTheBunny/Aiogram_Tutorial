from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # מושכים מה שאנצנו צריכים בשביל המקלדת

# כפתור
btn_hello = KeyboardButton("Hello!")

# מקלדת
welcome_keyboard = ReplyKeyboardMarkup().add(btn_hello)


## מקלדת שניה

# כפתור
btn_tuna = KeyboardButton("עם טונה")
btn_oliv = KeyboardButton("עם זיתים")
btn_cheese = KeyboardButton("עם אקסטרה גבינה")

# מקלדת
pizza_keyboard = ReplyKeyboardMarkup(
                                    resize_keyboard=True, # הקטנה המקשים.
                                    one_time_keyboard=True # עשייתה של המקלדת חד פעמית
                                    ).add(btn_tuna).add(btn_oliv).add(btn_cheese)



## מקלדת שלישית

# כפתור
btn_big = KeyboardButton("גדולה")
btn_huge = KeyboardButton("ענקית")
btn_double = KeyboardButton("כפולה")

middle_button = KeyboardButton("ממש סופר ענקית")


# מקלדת
size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_big, btn_huge, btn_double).add(middle_button)

