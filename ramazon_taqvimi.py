
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from bot14 import * 
from bot17 import keyboardbuxoro, keyboardandijon, keyboardfargona  
from bot17 import keyboardjizzax, keyboardsurxondaryo, keyboardnamangan, keyboardnavoiy, keyboardqashqadaryo, \
    keyboardsirdaryo
from bot17 import keyboardsamarqand, keyboardqoraqalpogiston, keyboardxorazm, keyboardtoshkent
from conf import TOKEN
from bot18 import bugun, hozirgi, bomdod, quyosh, peshin, asr, shom, xufton, ramazon
from datetime import date

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
@dp.message_handler(Command('start'))
async def select_mintaqa(message: types.Message):
    await message.answer(
        text="Assalomu Alaykum va Rahmatullohu va Barakatuh\n<b>Ramazon Taqvimi</b> 2️⃣0️⃣2️⃣3️⃣ \n\n botiga xush kelibsiz\nKerakli bo'limni "
             "tanlang!",
        parse_mode='html',
        reply_markup=keyboardS
    )


# ______________________ ______________________________________________________________________________________________
@dp.message_handler(text='Tarovex namoz tasbexi')
async def send1(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=71,
        from_chat_id=chanel_id,)    
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=72,
        from_chat_id=chanel_id, reply_markup=keyboardM)

@dp.message_handler(text='🤲Namozdan keyingi zikrlar')
async def send_taqvimTaqvim(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=20,
        from_chat_id=chanel_id,)
    await message.answer(
        text="Kerakli bo'limni tanlang!",
        reply_markup=keyboardP
    )


@dp.message_handler(text='Namozdan keyingi zikrlar')
async def send_zikrlar(message: types.Message):
    await message.answer(
        text=f"<b>NAMOZDAN KEYINGI ZIKRLAR</b>\n\n"
             f"Namoz salom bilan tugaydi. Salomdan keyingi amallar <b>(tasbehotu duolar)</b> majburiy emas,"
             f"ammo nihoyatda savoblidir.\n\n"
             f"Farz namozlaridan keyin quyidagi duoni o'qish sunnatdir:\n\n"
             f"<b>Allohumma antas-salam va minkas-salam,\n Taborakta ya zaljalali val ikrom.</b>\n\n"
             f"<i>Mazmuni:</i> Ey Allohim, Sen barcha ayb-nuqsonlardan poksan. Barcha  salomatlik va rahmat Sendandir."
             f"Ey azamat va qudrat egasi bo'lgan Allohim, Sening shoning ulug'dir.\n\n"
             f"Umuman, har namozni tugatgandan so'ng <b>Oyatal Kursi</b> o'qilsa,"
             f"savobi ulug' bo'ladi. ",
        parse_mode='html',
        reply_markup=keyboardP
    )
@dp.message_handler(text='Fotiha surasi')
async def sendf(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=17,
        from_chat_id=chanel_id,)
    await message.answer(
        text=f"<b>Fotiha Surasi</b>\n\n"
             f"A’uzu billahi minash shaytonir rojiym.\n"
             f"Bismillahir rohmanir rohiym.\n"
             f"Al hamdulillahi robbil ‘alamiyn.\n"
             f"Ar-rohmanir rohiym. Maliki yavmiddiyn.\n"
             f"Iyyaka na’budu va iyyaka nasta’iyn.\n"
             f"Ihdinas sirotol mustaqiym.\n"
             f"Sirotollaziyna an’amta ‘alayhim g‘oyril mag‘zubi ‘alayhim valazzolliyn.\n"
             f"<b>Mazmuni:</b>\n"
             f"Allohning dargohidan quvilgan shayton yomonligidan Allohning panohiga qochaman.\n"
             f"Mehribon va rahmli Alloh nomi bilan (boshlayman).\n"
             f"Hamd olamlar rabbi Allohgakim, (U) mehribon, rahmli va hisob-kitob kuni (Qiyomat)ning egasidir.\n"
             f"Sengagina ibodat qilamiz va Sendangina yordam so'raymiz!\n"
             f"Bizni shunday to'g'ri yo'lga boshlaginki, (U) Sen in'om (hidoyat) etganlarning (payg'ambarlar, siddiq va shahidlarning) yo'lidir, g'azabga uchragan (Muso qavmidan itoatsizlarining) va adashgan (Iso qavmining «Allohning farzandi bor» deydigan)larning emas!\n",
        parse_mode='html',
        reply_markup=keyboardW
    )
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=70,
        from_chat_id=chanel_id,)
@dp.message_handler(text='Oyatal Kursi')
async def send_zikrlar(message: types.Message):
    await message.answer(
        text=f"<b>OYATAL KURSIY</b>\n\n"
             f"<b>A'uzi billahi minash-shaytonir rojiym. Bismillahir rohmanir rohiym.</b>\n\n"
             f"<b>«Allohu laa ilaaha illa huval Hayyul Qoyyuum."
             f" Laa ta'xuzuhu sinatuv va laa navm. Lahuu maa fis-samaavaati va maa fil ard."
             f" Man‑zallazii yashfa'u 'indahu illaa bi‑iznih. "
             f"Ya'lamu maa bayna aydiyhim va maa xolfahum va laa yuhituuna bishay'im‑min 'ilmihii illaa bima shaa-a."
             f" Vasi'a kursiyyuuhus-samaavaati val‑ard. Va laa yauduhu hifzuhumaa va huval 'aliyyul 'aziym»</b>\n\n"
             f"<i>Mazmuni:</i>\n\n"
             f"<i>Alloh – Undan o‘zga iloh yo‘q. U Hayy va Qayyumdir."
             f"Uni mudroq ham, uyqu ham olmas. Osmonlaru yerdagi narsalar Unikidir."
             f"Uning huzurida O‘zining iznisiz hеch kim shafoat qila olmas. "
             f" Ularning oldilaridagi narsani ham, ortlaridagi narsani ham bilur. "
             f"Uning ilmidan O‘zi xohlaganidan boshqa hеch narsani ihota qila olmaslar. "
             f"Uning Kursisi osmonlaru yerni qamragan.  Ularni muhofaza qilish unga og‘ir kеlmas. "
             f"Va U Aliy va Aziymdir.</i>",
        parse_mode='html',
        reply_markup=keyboardP
    )
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=69,
        from_chat_id=chanel_id,)
@dp.message_handler(text='🤲Namoz duolari')
async def send_namozduo(message: types.Message):
    await message.answer( 
        text='Kerakli bo\'limni tanlang',
        parse_mode='html',
        reply_markup=keyboardW
)
@dp.message_handler(text='Azon aytish🔉')
async def senda(message: types.Message):

    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=68,
        from_chat_id=chanel_id,)
    await message.answer(
        text=f"<b><i>Azon</i></b>\n\n"
             f"Allohu Akbar!\n"
             f"Allohu Akbar!\n"
             f"Allohu Akbar!\n"
             f"Allohu Akbar!\n"
             f"Ashhadu alla ilaha illalloh!\n"
             f"Ashhadu alla ilaha illalloh!\n"
             f"Ashhadu anna Muhammadar rasululloh!\n"
             f"Ashhadu anna Muhammadar rasululloh!\n"
             f"Hayya 'alas-solah!\n"
             f"Hayya 'alas-solah!\n"
             f"Hayya 'alal falah!\n"
             f"Hayya 'alal falah!\n"
             f"Allohu Akbar!\n"
             f"Allohu Akbar!\n"
             f"La ilaha illalloh.\n\n"
             f"<b><i>Tarjimasi</i></b>\n\n"
             f"Alloh buyukdir!\n"
             f"Alloh buyukdir!\n"
             f"Alloh buyukdir!\n"
             f"Alloh buyukdir!\n"
             f"Allohdan o'zga sig'iniladigan (iloh) yo'qligiga iqrorman!\n"
             f"Allohdan o'zga sig'iniladigan (iloh) yo'qligiga iqrorman!\n"
             f"Muhammad Allohning elchisi ekaniga iqrorman!\n"
             f"Muhammad Allohning elchisi ekaniga iqrorman!\n"
             f"Namozga keling, namozga keling!\n"
             f"Najotga keling, najotga keling!\n"
             f"Alloh buyukdir!\n"
             f"Alloh buyukdir!\n"
             f"Allohdan o'zga iloh yo'q!\n",
             parse_mode='html'
    )
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=67,
        from_chat_id=chanel_id,)
@dp.message_handler(text="Zam sura")
async def send_zamsura(message: types.Message):
    # await message.answer_photo(
    #     open(r'/root/ramadan/handlers/ramadan/img/An_nos.jpg', 'rb'))
    await message.answer(
        text=f"<b>KAVSAR SURASI</b>\n\n"
             f"Mazmuni:"
             f"(Ey Muhammad,) ayting: «U — Alloh yagonadir."
             f" Alloh behojat, (lekin) hojatbarordir."
             f" U tug'magan va tug'ilmagan ham."
             f"Shuningdek, Unga teng biror zot yo'qdir»",
        parse_mode='html'
    )
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=42,
        from_chat_id=chanel_id,
    )

    # await message.answer_photo(open(r'/root/ramadan/handlers/ramadan/img/falaq_surasi.jpg', 'rb'))
    await message.answer(
        text=f"<b>FALAQ SURASI</b>\n\n"
             f"Qul a’uzu birobbil falaq. Min sharri ma xolaq. Va min sharri g‘osiqin iza vaqob."
             f"Va min sharrin-naffasati fil ‘uqod. Va min sharri hasidin iza hasad.\n",
        parse_mode='html'
    )
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=36,
        from_chat_id=chanel_id,
    )

    # await message.answer_photo(open(r'/root/ramadan/handlers/ramadan/img/ixlos_surasi.jpg', 'rb'))
    await message.answer(
        text=f"Qul huvallohu ahad.\n"
             f'Allohus-somad.Lam yalid.\n'
             f'Va lam yuvlad va lam yakullahu kufuvan ahad.\n')
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=40,
        from_chat_id=chanel_id,
    )

@dp.message_handler(text='Namoz o\'qishni o\'rganamiz')
async def seng(message: types.Message):
    await message.answer(text='Kerakli bo\'limni tanlang:', reply_markup=keyboardD)

@dp.message_handler(text='Bamdod namozi')
async def sendt(message: types.Message):
   await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=32,
        from_chat_id=chanel_id,
        reply_markup=keyboardD) 
@dp.message_handler(text='Peshin namozi')
async def sendt(message: types.Message):
   await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=34,
        from_chat_id=chanel_id,
        reply_markup=keyboardD) 
@dp.message_handler(text='Asr namozi')
async def sendt(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=31,
        from_chat_id=chanel_id,
        reply_markup=keyboardD) 
@dp.message_handler(text='Shom namozi')
async def sendt(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=33,
        from_chat_id=chanel_id,
        reply_markup=keyboardD) 
                        
@dp.message_handler(text='Xufton namozi')
async def sendt(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=35,
        from_chat_id=chanel_id,
        reply_markup=keyboardD) 
    
chanel_id=-1001857306751
@dp.message_handler(text='Tashahhud')
async def t(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=14,
        from_chat_id=chanel_id,)
    await message.answer(
        text=f'Attahiyyatu lillahi vas-solavatu vattoyyibat.\n'
             f'Assalamu ‘alayka ayyuhan-nabiyyu va rohmatullohi va barokatuh.\n'
             f'Assalamu ‘alayna va ‘ala ibadillahis-solihiyn.\n'
             f'Ashhadu alla ilaha illallohu va ashhadu anna Muhammadan ‘abduhu va rosuluh.')
    
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=48,
        from_chat_id=chanel_id,
     )

@dp.message_handler(text='📿Tasbeh')
async def send_zikrlar(message: types.Message):
    await message.answer(
        text=f"📿TASBEH\n\n"
             f"<b>Subhanalloh (33 marta)</b>\n"
             f"<b>Alhamdulillah (33 marta)</b>\n"
             f"<b>Allohu akbar (33 marta)</b>",
        parse_mode='html',
        reply_markup=keyboardP
    )


@dp.message_handler(text='Kalimai Tavhid')
async def send_zikrlar(message: types.Message):
    await message.answer(
        text=f"<b>KALIMAI TAVHID</b>\n\n"
             f"<b>«Ashhadu allaa ilaaha illallohu vahdahu laa sharika lah,"
             f" lahul mulku va lahul hamd, yuhyii va yumiyt va huva hayyul laa yamuut, "
             f"biyadihil xoyr va huva 'alaa kulli shay'in qodiyr».</b>\n\n"
             f"<i>Mazmuni:</i>\n\n"
             f"<i>Allohdan o‘zga iloh yo‘qligiga guvohlik bеraman. Allohning shеrigi yo‘qdir,"
             f"barcha mulk Unikidir, maqtovlar Ungadir, U tiriltiradi va o‘ldiradi,"
             f"ammo O‘zi tirikdir, o‘lmaydi. Yaxshilik Uning ixtiyoridadir va U hamma narsaga qodirdir.</i>",
        parse_mode='html',
        reply_markup=keyboardP
    )
@dp.message_handler(text='Salovat')
async def sent(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=23,
        from_chat_id=chanel_id,   )
    await message.answer(
        text=f"<b>Salovat</b>\n\n"
             f"Allohumma solli ‘ala Muhammadiv-va ‘ala ali Muhammad.\n"
             f" Kama sollayta ‘ala Ibrohima va ‘ala ali Ibrohim.\n"
             f" Innaka hamidum-majid.\n\n"
             f" Allohumma barik ‘ala Muhammadiv-va ‘ala ali Muhammad.\n"
             f" Kama barokta ‘ala Ibrohima va ‘ala ali Ibrohim.\n"
             f" Innaka hamidum-majid.",
        parse_mode='html',
        reply_markup=keyboardW     
    )   
#@dp.message_handler(state='t1443_v')
#async def d(message: types.Message, state:FSMContext):
    #if message.text(text='1-3 kunlar'):

       # id1 = 2
     # #  id2 = 4
      #  for n in range(id1, id2 +1):
     #       try:
      #          await bot.copy_message(chat_id=message.from_user.id,
     #                               from_chat_id=1001705654629,
     #                               message_id=n,
     #                               caption=f"{c1[n-2]}, {islomuz}"
          #      )
         #  except Exception as err:
         #       await message.answer(err)
        
#@dp.message_handler(text='📅To\'liq taqvim')
#async def sendm(message: types.Message):
  #  viloyat = ('')
  #  await message.answer(text='Hali yangilanadi bot sinovda')
    
# ______________________________________________________________________________________________________________________
@dp.message_handler(text='📆Ramadan taqvimi')
async def send_taqvimTaqvim(message: types.Message):
    await message.answer(
        text='Mintaqani tanlang',
        reply_markup=keyboard1
    )
today = date.today()
date_23M = date(2023, 3, 23)
dateB = str(date_23M - today)


@dp.message_handler(text='Andijon')
async def send_taqvimAndijon(message: types.Message):
    await message.answer(
        text=f"☪️ Ramazon taqvimi:\n\n"
             f"<b>Bugun {bugun('andijon')}"
             f"{hozirgi('andijon')}</b>"
             f"( Andijon shahri )\n\n"
             f"🏙 <b>Saharlik</b>: {bomdod('andijon')} 🕰 <b>gacha </b>\n\n\n"
             f"🌆 <b>Iftorlik</b>: {shom('andijon')} 🕰 <b> dan so'ng </b>\n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )

@dp.message_handler(text='Buxoro')
async def send_taqvimBuxoro(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('buxoro')}"
                 f"{hozirgi('buxoro')}</b>"
                 f"( Buxoro shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('buxoro')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('buxoro')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text="Farg'ona")
async def send_taqvimFargona(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('fargona')}"
                 f"{hozirgi('fargona')}</b>"
                 f"( Farg'ona shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('fargona')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('fargona')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Jizzax')
async def send_taqvimJizzax(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('jizzax')}"
                 f"{hozirgi('jizzax')}</b>"
                 f"( Jizzax shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('jizzax')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('jizzax')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Xorazm')
async def send_taqvimXorazm(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('urganch')}"
                 f"{hozirgi('urganch')}</b>"
                 f"( Urganch shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('urganch')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('urganch')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Namangan')
async def send_taqvimNamangan(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('namangan')}"
                 f"{hozirgi('namangan')}</b>"
                 f"( Namangan shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('namangan')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('namangan')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Navoiy')
async def send_taqvimNavoiy(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('navoiy')}"
                 f"{hozirgi('navoiy')}</b>"
                 f"( Navoiy shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('navoiy')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('navoiy')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Qashqadaryo')
async def send_taqvimQashqadaryo(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('qarshi')}"
                 f"{hozirgi('qarshi')}</b>"
                 f"( Qarshi shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('qarshi')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('qarshi')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Sirdaryo')
async def send_taqvimSirdaryo(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('sirdaryo')}"
                 f"{hozirgi('sirdaryo')}</b>"
                 f"( Sirdaryo shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('sirdaryo')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('sirdaryo')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Samarqand')
async def send_taqvimSamarqand(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('samarqand')}"
                 f"{hozirgi('samarqand')}</b>"
                 f"( Samarqand shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('samarqand')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('samarqand')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text="Qoraqalpog'iston")
async def send_taqvimQoraqalpogiston(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('nukus')}"
                 f"{hozirgi('nukus')}</b>"
                 f"( Nukus shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('nukus')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('nukus')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Surxondaryo')
async def send_taqvimSurxondaryo(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('termiz')}"
                 f"{hozirgi('termiz')}</b>"
                 f"( Termiz shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('termiz')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('termiz')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


@dp.message_handler(text='Toshkent')
async def send_taqvimtoshkent(message: types.Message):
    # await bot.send_photo(
    #     message.chat.id, open('G:/bot projects/RamadanTaqvim/images/Duo.JPG', 'rb'),
    #     reply_markup=keyboardM
    # )
    if date_23M > today:
        await message.answer(
            text=f"<b>Ramazon boshlanishiga {dateB} qoldi</b>\n\n"
                 f"Ramazon rasman <i>23-Mart</i> dan boshlanadi",
            parse_mode='html',
            reply_markup=keyboardM
        )
    else:
        await message.answer(
            text=f"☪️ Ramazon taqvimi:\n\n"
                 f"<b>Bugun {bugun('toshkent')}"
                 f"{hozirgi('toshkent')}</b>"
                 f"( Toshkent shahri )\n\n"
                 f"🏙 <b>Saharlik</b>: {bomdod('toshkent')} 🕰 <b>gacha </b>\n\n\n"
                 f"🌆 <b>Iftorlik</b>: {shom('toshkent')} 🕰 <b> dan so'ng </b>\n\n"
                 f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
            disable_web_page_preview=True,
            parse_mode='html',
            reply_markup=keyboardM
        )


# this is for inside menyu______________________________________________________________________________________________
@dp.message_handler(text='🤲Duo')
async def send_taqvimDuo(message: types.Message):
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=66,
        from_chat_id=-1001857306751,
        
    )
    await message.answer(
        text=f"<b>Ro'za tutish duosi\n (saharlik, og'iz yopish)</b>\nNavaytu an asuma sovma shahri"
             f" Ramazona minai fajri ilal mag'ribi, xolisan lillahi ta'ala Allohu akbar.\n\n"
             f"<i>Ma'nosi:\n Ramazon oyining ro'zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh "
             f"uchun "
             f"Alloh buyukdir.</i>\n\n\n"
             f"<b>Iftorlik duosi (og'iz ochish)\n\n</b>"
             f"Allohumma laka sumtu va bika amantu va a'layka tavakkaltu va a'la rizqika aftartu"
             f", fag'firliy ma qoddamtu va maa axxortu birohmatika yaa"
             f" arhamar roohimiyn.\n\n"
             f"<i>Ma'nosi:\n Ey Alloh, ushbu Ro'zamni Sen uchun tutdim"
             f"va Senga iymon keltirdim va Senga tavakkal qildim."
             f"Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi "
             f"gunohlarimni mag'firat qilgin.</i>",
        parse_mode="html",
        reply_markup=keyboardM
        )
   


@dp.message_handler(text='⬅️Bosh Menyu')
async def back(message: types.Message):
    await message.answer(
        text="Kerakli bo'limni tanlang",
        reply_markup=keyboardS
    )


@dp.message_handler(text='⬅️bosh menyu')
async def back(message: types.Message):
    await message.answer(
        text="Kerakli bo'limni tanlang",
        reply_markup=keyboardS
    )


@dp.message_handler(text='🇺🇿Mintaqa')
async def send_taqvimMintaqa(message: types.Message):
    await message.answer(
        text='Kerakli mintaqani tanlang!',
        reply_markup=keyboard1
    )


# this is for main menyu________________________________________________________________________________________________
@dp.message_handler(text='🤲Duo')
async def send_taqvimDuo(message: types.Message):   
    await bot.copy_message(
        chat_id=message.from_user.id,
        message_id=73,
        from_chat_id=chanel_id,)
    await message.answer(
        text=f"<b>Ro'za tutish duosi\n (saharlik, og'iz yopish)</b>\nNavaytu an asuma sovma shahri"
             f" Ramazona minai fajri ilal mag'ribi, xolisan lillahi ta'ala Allohu akbar.\n\n"
             f"<i>Ma'nosi:\n Ramazon oyining ro'zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh "
             f"uchun "
             f"Alloh buyukdir.</i>\n\n\n"
             f"<b>Iftorlik duosi (og'iz ochish)\n\n</b>"
             f"Allohumma laka sumtu va bika amantu va a'layka tavakkaltu va a'la rizqika aftartu"
             f", fag'firliy ma qoddamtu va maa axxortu birohmatika yaa"
             f" arhamar roohimiyn.\n\n"
             f"<i>Ma'nosi:\n Ey Alloh, ushbu Ro'zamni Sen uchun tutdim"
             f"va Senga iymon keltirdim va Senga tavakkal qildim."
             f"Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi "
             f"gunohlarimni mag'firat qilgin.</i>",
        parse_mode="html",
        reply_markup=keyboardS
    )


# this is for about bot_________________________________________________________________________________________________
@dp.message_handler(text='📚Bot haqida')
async def send_bothaqaida(message: types.Message):
    await message.answer(
        text=f"👨🏻‍💻 Loyiha asoschisi — Young Dev va ImYago\n"
             f"📜 Ma'lumotlar: \n "
             f"➖islom.uz \n"
             f"➖namozvaqti.uz\n "
             f"sahifalardan olindi \n"
             f"📩 Murojaatlar uchun — @young_developer_07",
        reply_markup=keyboardS
    )


@dp.message_handler(text='🕍Namoz vaqtlari')
async def send_bothaqaida(message: types.Message):
    await message.answer(
        text="Namoz vaqtlari🕍\n\n"
             "Kerakli bo'limni tanlang!",
        reply_markup=keyboardI
    )


# buxoro tumanlari uchun _______________________________________________________________________________________________
@dp.message_handler(text="buxoro")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardbuxoro
    )


@dp.callback_query_handler(text='buxoro')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('buxoro')}"
             f"{hozirgi('buxoro')}\n</b>"
             f"( Buxoro shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('buxoro')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('buxoro')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('buxoro')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('buxoro')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('buxoro')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('buxoro')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='jondor')
async def random_value(query: types.CallbackQuery):

    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('jondor')}"
             f"{hozirgi('jondor')}\n</b>"
             f"( Jondor shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('jondor')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('jondor')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('jondor')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('jondor')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('jondor')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('jondor')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='qorakol')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('qorakol')}"
             f"{hozirgi('qorakol')}\n</b>"
             f"( Qorakol shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('qorakol')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('qorakol')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('qorakol')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('qorakol')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('qorakol')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('qorakol')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='gijduvon')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('gijduvon')}"
             f"{hozirgi('gijduvon')}\n</b>"
             f"( G'ijduvon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('gijduvon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('gijduvon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('gijduvon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('gijduvon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('gijduvon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('gijduvon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='gazli')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('gazli')}"
             f"{hozirgi('gazli')}\n</b>"
             f"( Gazli shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('gazli')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('gazli')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('gazli')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('gazli')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('gazli')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('gazli')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# andijon uchun ________________________________________________________________________________________________________
@dp.message_handler(text="andijon")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardandijon
    )


@dp.callback_query_handler(text='andijon')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('andijon')}"
             f"{hozirgi('andijon')}\n</b>"
             f"( Andijon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('andijon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('andijon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('andijon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('andijon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('andijon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('andijon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='xonobod')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('xonobod')}"
             f"{hozirgi('xonobod')}\n</b>"
             f"( Xonobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('xonobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('xonobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('xonobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('xonobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('xonobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('xonobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='xojaobod')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('xojaobod')}"
             f"{hozirgi('xojaobod')}\n</b>"
             f"( Xo'jaobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('xojaobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('xojaobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('xojaobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('xojaobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('xojaobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('xojaobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='asaka')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('asaka')}"
             f"{hozirgi('asaka')}\n</b>"
             f"( Asaka shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('asaka')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('asaka')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('asaka')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('asaka')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('asaka')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('asaka')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='marhamat')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('marhamat')}"
             f"{hozirgi('marhamat')}\n</b>"
             f"( Marhamat shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('marhamat')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('marhamat')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('marhamat')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('marhamat')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('marhamat')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('marhamat')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='paytug')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('paytug')}"
             f"{hozirgi('paytug')}\n</b>"
             f"( Poytug' shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('paytug')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('paytug')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('paytug')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('paytug')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('paytug')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('paytug')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text='boston')
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('boston')}"
             f"{hozirgi('boston')}\n</b>"
             f"( Bo'ston shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('boston')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('boston')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('boston')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('boston')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('boston')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('boston')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# fargona uchun ________________________________________________________________________________________________________
@dp.message_handler(text="farg'ona")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardfargona
    )


@dp.callback_query_handler(text="fargona")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('fargona')}"
             f"{hozirgi('fargona')}\n</b>"
             f"( Farg'ona shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('fargona')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('fargona')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('fargona')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('fargona')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('fargona')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('fargona')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="qoqon")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('qoqon')}"
             f"{hozirgi('fargona')}\n</b>"
             f"( Qo'qon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('qoqon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('qoqon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('qoqon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('qoqon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('qoqon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('qoqon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="margilon")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('margilon')}"
             f"{hozirgi('fargona')}\n</b>"
             f"( Margilon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('margilon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('margilon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('margilon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('margilon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('margilon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('margilon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="quva")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('quva')}"
             f"{hozirgi('quva')}\n</b>"
             f"( Quva shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('quva')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('quva')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('quva')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('quva')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('quva')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('quva')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="rishton")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('rishton')}"
             f"{hozirgi('rishton')}\n</b>"
             f"( Rishton shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('rishton')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('rishton')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('rishton')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('rishton')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('rishton')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('rishton')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="bogdod")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('bogdod')}"
             f"{hozirgi('bogdod')}\n</b>"
             f"( Bog'dod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('bogdod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('bogdod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('bogdod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('bogdod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('bogdod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('bogdod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="oltiariq")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('oltiariq')}"
             f"{hozirgi('oltiariq')}\n</b>"
             f"( Oltiariq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('oltiariq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('oltiariq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('oltiariq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('oltiariq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('oltiariq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('oltiariq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# jizzax uchun ________________________________________________________________________________________________________
@dp.message_handler(text="jizzax")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardjizzax
    )


@dp.callback_query_handler(text="jizzax")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('jizzax')}"
             f"{hozirgi('jizzax')}\n</b>"
             f"( Jizzax shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('jizzax')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('jizzax')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('jizzax')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('jizzax')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('jizzax')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('jizzax')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )
'''@dp.callback_quary_handler(text='To\'liq taqvim')
async def toliq(query: types.CallbackQuery):
    await query.message.answer(
        text=f"Ramazon To'liq Taqvim"
             f"<b>B</b>{TOLIQ}\n\n"
             f"Ramazon muborak bo'lsin",
        disable_web_page_preview=True,
        parse_mode='html', 
    )'''
@dp.callback_query_handler(text="zomin")
async def random_valuezomin(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('zomin')}"
             f"{hozirgi('zomin')}\n</b>"
             f"( Zomin shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('zomin')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('zomin')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('zomin')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('zomin')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('zomin')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('zomin')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="forish")
async def random_valueforish(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('forish')}"
             f"{hozirgi('forish')}\n</b>"
             f"( Forish shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('forish')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('forish')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('forish')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('forish')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('forish')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('forish')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="gallaorol")
async def random_valuegallaorol(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('gallaorol')}"
             f"{hozirgi('gallaorol')}\n</b>"
             f"( G'allaorol shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('gallaorol')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('gallaorol')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('gallaorol')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('gallaorol')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('gallaorol')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('gallaorol')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# surxondaryo uchun ____________________________________________________________________________________________________
@dp.message_handler(text="surxondaryo")
async def inline_keyboardsurxondaryo(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardsurxondaryo
    )


@dp.callback_query_handler(text="termiz")
async def random_valuetermiz(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('termiz')}"
             f"{hozirgi('termiz')}\n</b>"
             f"( Termiz shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('termiz')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('termiz')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('termiz')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('termiz')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('termiz')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('termiz')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="boysun")
async def random_valueboysun(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('boysun')}"
             f"{hozirgi('boysun')}\n</b>"
             f"( Boysun shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('boysun')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('boysun')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('boysun')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('boysun')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('boysun')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('boysun')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="denov")
async def random_valuedenov(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('denov')}"
             f"{hozirgi('denov')}\n</b>"
             f"( Denov shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('denov')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('denov')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('denov')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('denov')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('denov')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('denov')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="sherobod")
async def random_valuesherobod(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('sherobod')}"
             f"{hozirgi('sherobod')}\n</b>"
             f"( Sherobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('sherobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('sherobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('sherobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('sherobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('sherobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('sherobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="shorchi")
async def random_valuesherobod(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('shorchi')}"
             f"{hozirgi('shorchi')}\n</b>"
             f"( Sho'rchi shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('shorchi')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('shorchi')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('shorchi')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('shorchi')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('shorchi')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('shorchi')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# namangan uchun _______________________________________________________________________________________________________
@dp.message_handler(text="namangan")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardnamangan
    )


@dp.callback_query_handler(text="namangan")
async def random_valuenamangan(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('namangan')}"
             f"{hozirgi('namangan')}\n</b>"
             f"( Namangan shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('namangan')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('namangan')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('namangan')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('namangan')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('namangan')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('namangan')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="chortoq")
async def random_valuechortoq(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('chortoq')}"
             f"{hozirgi('chortoq')}\n</b>"
             f"( Chortoq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('chortoq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('chortoq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('chortoq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('chortoq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('chortoq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('chortoq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="chust")
async def random_valuechust(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('chust')}"
             f"{hozirgi('chust')}\n</b>"
             f"( Chust shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('chust')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('chust')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('chust')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('chust')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('chust')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('chust')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="pop1")
async def random_valuepop(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('pop1')}"
             f"{hozirgi('pop1')}\n</b>"
             f"( Pop shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('pop1')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('pop1')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('pop1')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('pop1')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('pop1')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('pop1')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="uchqorgon")
async def random_valueuchqorgon(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('uchqorgon')}"
             f"{hozirgi('uchqorgon')}\n</b>"
             f"( Uchqo'rg'on shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('uchqorgon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('uchqorgon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('uchqorgon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('uchqorgon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('uchqorgon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('uchqorgon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="mingbuloq")
async def random_valuemingbuloq(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('mingbuloq')}"
             f"{hozirgi('mingbuloq')}\n</b>"
             f"( Mingbuloq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('mingbuloq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('mingbuloq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('mingbuloq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('mingbuloq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('mingbuloq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('mingbuloq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# navoiy uchun ________________________________________________________________________________________________________
@dp.message_handler(text="navoiy")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardnavoiy
    )


@dp.callback_query_handler(text="navoiy")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('navoiy')}"
             f"{hozirgi('navoiy')}\n</b>"
             f"( Navoiy shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('navoiy')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('navoiy')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('navoiy')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('navoiy')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('navoiy')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('navoiy')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="zarafshon")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('zarafshon')}"
             f"{hozirgi('zarafshon')}\n</b>"
             f"( Zarafshon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('zarafshon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('zarafshon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('zarafshon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('zarafshon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('zarafshon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('zarafshon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="konimex")
async def random_valuekonimex(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('konimex')}"
             f"{hozirgi('konimex')}\n</b>"
             f"( Konimex shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('konimex')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('konimex')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('konimex')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('konimex')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('konimex')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('konimex')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="nurota")
async def random_valuenurota(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('nurota')}"
             f"{hozirgi('nurota')}\n</b>"
             f"( Nurota shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('nurota')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('nurota')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('nurota')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('nurota')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('nurota')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('nurota')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="uchquduq")
async def random_valueuchquduq(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('uchquduq')}"
             f"{hozirgi('uchquduq')}\n</b>"
             f"( Uchquduq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('uchquduq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('uchquduq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('uchquduq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('uchquduq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('uchquduq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('uchquduq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Qashqadaryo uchun ____________________________________________________________________________________________________
@dp.message_handler(text="qashqadaryo")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardqashqadaryo
    )


@dp.callback_query_handler(text="qarshi")
async def random_valueqarshi(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('qarshi')}"
             f"{hozirgi('qarshi')}\n</b>"
             f"( Qarshi shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('qarshi')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('qarshi')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('qarshi')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('qarshi')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('qarshi')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('qarshi')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="dehqonobod")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('dehqonobod')}"
             f"{hozirgi('dehqonobod')}\n</b>"
             f"( Dehqonobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('dehqonobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('dehqonobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('dehqonobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('dehqonobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('dehqonobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('dehqonobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="muborak")
async def random_valuemuborak(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('muborak')}"
             f"{hozirgi('muborak')}\n</b>"
             f"( Muborak shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('muborak')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('muborak')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('muborak')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('muborak')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('muborak')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('muborak')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="shahrisabz")
async def random_valueshahrisabz(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('shahrisabz')}"
             f"{hozirgi('shahrisabz')}\n</b>"
             f"( Shahrisabz shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('shahrisabz')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('shahrisabz')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('shahrisabz')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('shahrisabz')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('shahrisabz')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('shahrisabz')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="guzor")
async def random_valueguzor(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('guzor')}"
             f"{hozirgi('guzor')}\n</b>"
             f"( Guzor shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('guzor')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('guzor')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('guzor')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('guzor')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('guzor')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('guzor')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Sirdaryo uchun _______________________________________________________________________________________________________
@dp.message_handler(text="sirdaryo")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardsirdaryo
    )


@dp.callback_query_handler(text="sirdaryo")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('sirdaryo')}"
             f"{hozirgi('sirdaryo')}\n</b>"
             f"( Sirdaryo shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('sirdaryo')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('sirdaryo')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('sirdaryo')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('sirdaryo')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('sirdaryo')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('sirdaryo')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="guliston")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('guliston')}"
             f"{hozirgi('guliston')}\n</b>"
             f"( Guliston shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('guliston')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('guliston')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('guliston')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('guliston')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('guliston')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('guliston')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="sardoba")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('sardoba')}"
             f"{hozirgi('sardoba')}\n</b>"
             f"( Sardoba shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('sardoba')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('sardoba')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('sardoba')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('sardoba')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('sardoba')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('sardoba')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="boyovut")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('boyovut')}"
             f"{hozirgi('boyovut')}\n</b>"
             f"( Boyovut shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('boyovut')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('boyovut')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('boyovut')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('boyovut')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('boyovut')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('boyovut')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="paxtaobod")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('paxtaobod')}"
             f"{hozirgi('paxtaobod')}\n</b>"
             f"( Paxtaobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('paxtaobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('paxtaobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('paxtaobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('paxtaobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('paxtaobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('paxtaobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Samarqand uchun ______________________________________________________________________________________________________
@dp.message_handler(text="samarqand")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardsamarqand
    )


@dp.callback_query_handler(text="samarqand")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('samarqand')}"
             f"{hozirgi('samarqand')}\n</b>"
             f"( Samarqand shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('samarqand')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('samarqand')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('samarqand')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('samarqand')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('samarqand')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('samarqand')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="ishtixon")
async def random_value(query: types.CallbackQuery):

    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('ishtixon')}"
             f"{hozirgi('ishtixon')}\n</b>"
             f"( Ishtixon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('ishtixon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('ishtixon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('ishtixon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('ishtixon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('ishtixon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('ishtixon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="mirbozor")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('mirbozor')}"
             f"{hozirgi('mirbozor')}\n</b>"
             f"( Mirbozor shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('mirbozor')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('mirbozor')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('mirbozor')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('mirbozor')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('mirbozor')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('mirbozor')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="kattaqorgon")
async def random_value(query: types.CallbackQuery):

    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('kattaqorgon')}"
             f"{hozirgi('kattaqorgon')}\n</b>"
             f"( Kattaqo'rg'on shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('kattaqorgon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('kattaqorgon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('kattaqorgon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('kattaqorgon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('kattaqorgon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('kattaqorgon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="urgut")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('urgut')}"
             f"{hozirgi('urgut')}\n</b>"
             f"( Urgut shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('urgut')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('urgut')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('urgut')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('urgut')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('urgut')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('urgut')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Qoraqalpog'iston uchun _______________________________________________________________________________________________
@dp.message_handler(text="qoraqalpog'iston")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardqoraqalpogiston
    )


@dp.callback_query_handler(text="nukus")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('nukus')}"
             f"{hozirgi('nukus')}\n</b>"
             f"( Nukus shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('nukus')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('nukus')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('nukus')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('nukus')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('nukus')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('nukus')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="moynoq")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('moynoq')}"
             f"{hozirgi('moynoq')}\n</b>"
             f"( Mo'ynoq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('moynoq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('moynoq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('moynoq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('moynoq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('moynoq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('moynoq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="taxtakopir")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('taxtakopir')}"
             f"{hozirgi('taxtakopir')}\n</b>"
             f"( Taxtako'pir shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('taxtakopir')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('taxtakopir')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('taxtakopir')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('taxtakopir')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('taxtakopir')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('taxtakopir')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="tortkol")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('tortkol')}"
             f"{hozirgi('tortkol')}\n</b>"
             f"( To'rtko'l shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('tortkol')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('tortkol')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('tortkol')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('tortkol')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('tortkol')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('tortkol')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="qongirot")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('qongirot')}"
             f"{hozirgi('qongirot')}\n</b>"
             f"( Qo'ng'irot shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('qongirot')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('qongirot')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('qongirot')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('qongirot')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('qongirot')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('qongirot')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Xorazm uchun ________________________________________________________________________________________________________
@dp.message_handler(text="xorazm")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardxorazm
    )


@dp.callback_query_handler(text="urganch")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('urganch')}"
             f"{hozirgi('urganch')}\n</b>"
             f"( Urganch shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('urganch')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('urganch')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('urganch')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('urganch')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('urganch')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('urganch')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="hazorasp")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('hazorasp')}"
             f"{hozirgi('hazorasp')}\n</b>"
             f"( Hazorasp shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('hazorasp')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('hazorasp')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('hazorasp')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('hazorasp')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('hazorasp')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('hazorasp')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="xonqa")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('xonqa')}"
             f"{hozirgi('xonqa')}\n</b>"
             f"( Xonqa shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('xonqa')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('xonqa')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('xonqa')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('xonqa')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('xonqa')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('xonqa')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="yangibozor")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('yangibozor')}"
             f"{hozirgi('yangibozor')}\n</b>"
             f"( Yangibozor shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('yangibozor')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('yangibozor')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('yangibozor')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('yangibozor')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('yangibozor')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('yangibozor')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="shovot")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('shovot')}"
             f"{hozirgi('shovot')}\n</b>"
             f"( Shovot shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('shovot')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('shovot')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('shovot')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('shovot')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('shovot')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('shovot')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# Toshkent uchun _______________________________________________________________________________________________________
@dp.message_handler(text="toshkent")
async def inline_keyboard(message: types.Message):
    await message.answer(
        text="Kerakli shaharni tanlang!",
        reply_markup=keyboardtoshkent
    )


@dp.callback_query_handler(text="tashkent")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('toshkent')}"
             f"{hozirgi('toshkent')}\n</b>"
             f"( Toshkent shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('toshkent')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('toshkent')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('toshkent')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('toshkent')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('toshkent')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('toshkent')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="angren")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('angren')}"
             f"{hozirgi('angren')}\n</b>"
             f"( Angren shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('angren')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('angren')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('angren')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('angren')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('angren')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('angren')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="piskent")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('piskent')}"
             f"{hozirgi('piskent')}\n</b>"
             f"( Piskent shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('piskent')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('piskent')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('piskent')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('piskent')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('piskent')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('piskent')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="bekobod")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('bekobod')}"
             f"{hozirgi('bekobod')}\n</b>"
             f"( Bekobod shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('bekobod')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('bekobod')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('bekobod')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('bekobod')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('bekobod')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('bekobod')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="parkent")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('parkent')}"
             f"{hozirgi('parkent')}\n</b>"
             f"( Parkent shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('parkent')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('parkent')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('parkent')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('parkent')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('parkent')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('parkent')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="gazalkent")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('gazalkent')}"
             f"{hozirgi('gazalkent')}\n</b>"
             f"( G'azalkent shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('gazalkent')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('gazalkent')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('gazalkent')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('gazalkent')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('gazalkent')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('gazalkent')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="olmaliq")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('olmaliq')}"
             f"{hozirgi('olmaliq')}\n</b>"
             f"( Olmaliq shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('olmaliq')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('olmaliq')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('olmaliq')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('olmaliq')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('olmaliq')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('olmaliq')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="boka")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('boka')}"
             f"{hozirgi('boka')}\n</b>"
             f"( Boka shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('boka')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('boka')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('boka')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('boka')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('boka')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('boka')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="yangiyol")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('yangiyol')}"
             f"{hozirgi('yangiyol')}\n</b>"
             f"( Yangiyo'l shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('yangiyol')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('yangiyol')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('yangiyol')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('yangiyol')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('yangiyol')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('yangiyol')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


@dp.callback_query_handler(text="nurafshon")
async def random_value(query: types.CallbackQuery):
    await query.message.answer(
        text=f"☪️ Namoz vaqtlari:\n\n"
             f"<b>Bugun {bugun('nurafshon')}"
             f"{hozirgi('nurafshon')}\n</b>"
             f"( Nurafshon shahri )\n\n"
             f"🏙 <b>Bomdod</b>: {bomdod('nurafshon')} 🕰 <b>gacha (Saharlik)</b>\n\n"
             f"🌅 <b>Quyosh</b>: {quyosh('nurafshon')} 🕰\n\n"
             f"🏞 <b>Peshin</b>: {peshin('nurafshon')} 🕰\n\n"
             f"🌇 <b>Asr</b>: {asr('nurafshon')} 🕰\n\n"
             f"🌆 <b>Shom</b>: {shom('nurafshon')} 🕰 <b>so'ng (Iftor)</b>\n\n"
             f"🌃 <b>Xufton</b>: {xufton('nurafshon')} 🕰 \n\n"
             f"Ma'lumotlar namozvaqti.uz sahifasidan olindi!",
        disable_web_page_preview=True,
        parse_mode='html',
    )


# ______________________________________________________________________________________________________________________

if __name__ == '__main__':
    executor.start_polling(dp)
