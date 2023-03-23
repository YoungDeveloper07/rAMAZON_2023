from aiogram import types


# keyboard for Mintaqa
keyboard1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard1.add(
    types.KeyboardButton(text='Andijon'),
    types.KeyboardButton(text='Buxoro'),
    types.KeyboardButton(text="Farg'ona"),
    types.KeyboardButton(text='Jizzax'),
    types.KeyboardButton(text='Surxondaryo'),
    types.KeyboardButton(text='Namangan'),
    types.KeyboardButton(text='Navoiy'),
    types.KeyboardButton(text='Qashqadaryo'),
    types.KeyboardButton(text='Sirdaryo'),
    types.KeyboardButton(text='Samarqand'),
    types.KeyboardButton(text="Qoraqalpog'iston"),
    types.KeyboardButton(text='Xorazm'),
    types.KeyboardButton(text='Toshkent'),

)


# keyboard after start the bot
keyboardS = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardS.add(
    types.KeyboardButton(text='📆Ramadan taqvimi'),
    types.KeyboardButton(text='🕍Namoz vaqtlari'),
 #   types.KeyboardButton(text='📖Quroni Karim tarjimalari'),
    types.KeyboardButton(text='🤲Namozdan keyingi zikrlar'),
    types.KeyboardButton(text='🤲Namoz duolari'),
    types.KeyboardButton(text='Namoz o\'qishni o\'rganamiz'),
    types.KeyboardButton(text='📚Bot haqida')
)

# keyboard after button the mintaqa
keyboardM = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardM.add(
    types.KeyboardButton(text='🤲Duo'),
#    types.KeyboardButton(text='📅To\'liq taqvim'),
    types.KeyboardButton(text='Tarovex namoz tasbexi')
)
keyboardM.add(
    types.KeyboardButton(text='🇺🇿Mintaqa'),
    types.KeyboardButton(text='⬅️Bosh Menyu')
)

# buttons for zikr after prayer

keyboardP = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardP.add(
    types.KeyboardButton(text='Namozdan keyingi zikrlar'),
    types.KeyboardButton(text='Oyatal Kursi'),
    types.KeyboardButton(text='📿Tasbeh'),
    types.KeyboardButton(text='Kalimai Tavhid'),
    types.KeyboardButton(text='⬅️Bosh Menyu')
)


keyboardI = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardI.add(
    types.KeyboardButton(text='andijon', callback_data='andijon'),
    types.KeyboardButton(text='buxoro', callback_data='buxoro'),
    types.KeyboardButton(text="farg'ona", callback_data="fargona"),
    types.KeyboardButton(text='jizzax', callback_data='jizzax'),
    types.KeyboardButton(text='surxondaryo', callback_data='surxondaryo'),
    types.KeyboardButton(text='namangan', callback_data='namangan'),
    types.KeyboardButton(text='navoiy', callback_data='navoiy'),
    types.KeyboardButton(text='qashqadaryo', callback_data='qashqadaryo'),
    types.KeyboardButton(text='sirdaryo', callback_data='sirdaryo'),
    types.KeyboardButton(text='samarqand', callback_data='samarqand'),
    types.KeyboardButton(text="qoraqalpog'iston", callback_data="qoraqalpogiston"),
    types.KeyboardButton(text='xorazm', callback_data='xorazm'),
    types.KeyboardButton(text='toshkent', callback_data='toshkent'),
    types.KeyboardButton(text='⬅️bosh menyu', callback_data='menyu'),
)
keyboardW = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardW.add(
    #types.KeyboardButton(text='Namoz o\'qishni o\'rganish'),
    types.KeyboardButton(text='Fotiha surasi'),
    types.KeyboardButton(text='Tashahhud'),
    types.KeyboardButton(text='Salovat'),
    types.KeyboardButton(text='Zam sura'),
    types.KeyboardButton(text='⬅️Bosh Menyu')

)
keyboardD = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboardD.add(
    types.KeyboardButton(text='Azon aytish🔉'),
    types.KeyboardButton(text='Bamdod namozi'),
    types.KeyboardButton(text='Peshin namozi'),
    types.KeyboardButton(text='Asr namozi'),
    types.KeyboardButton(text='Shom namozi'),
    types.KeyboardButton(text='Xufton namozi'),
    types.KeyboardButton(text='⬅️Bosh Menyu')
)