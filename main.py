import telebot
from telebot import types
import emoji


TOKEN = "5421782372:AAESCpvZ5H5FfoLGrRwJo6rarN6K_2JzNc0"
bot = telebot.TeleBot(TOKEN)

welcome_text = "Здравствуйте!\nВас приветсвует бот, который ответит на ваши вопросы.\nЧтобы посмотреть что я умею, нажмите на кнопку 👇 "
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() ==  "привет"  or message.text.lower() == "start" or message.text.lower() == "/start":
        bot.send_message(message.chat.id, text = welcome_text, reply_markup=welcome_msg_markup)
    elif message.text.lower() == "что ты умеешь?" or message.text.lower() == "что ты умеешь":
        bot.send_message(message.chat.id, text="Чем я могу Вам помочь?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, напишите «привет» ")


keyboard = types.InlineKeyboardMarkup(row_width=1) #кнопки под сообщением чем я могу вам помочь?
btn_1 = types.InlineKeyboardButton(text="Мобильный банкинг", callback_data="1" )
btn_2 = types.InlineKeyboardButton(text="Как получить банковскую карту?", callback_data="2" )
btn_3 = types.InlineKeyboardButton(text="Как открыть счёт в банке?", callback_data="3")
btn_4 = types.InlineKeyboardButton(text="Кредиты", callback_data="4")
keyboard.add(btn_1, btn_2, btn_3, btn_4)

welcome_msg_markup = types.InlineKeyboardMarkup(row_width=1) #кнопки под welcome_text
wlc_btn_1 = types.InlineKeyboardButton(text="Что ты умеешь?", callback_data="wlc_1")
wlc_btn_2 = types.InlineKeyboardButton(text="Карта банкоматов", url="https://www.cbk.kg/ru/atm")
wlc_btn_3 = types.InlineKeyboardButton(text="Связаться со специалистом", url="https://t.me/GooseSaysQuack")
wlc_btn_4 = types.InlineKeyboardButton(text="Контактные данные", callback_data="wlc_2")
welcome_msg_markup.add(wlc_btn_1, wlc_btn_2, wlc_btn_3, wlc_btn_4)

credit_markup = types.InlineKeyboardMarkup(row_width=1) #кнопки с описанием кредитов
crd_btn_1 = types.InlineKeyboardButton(text="Потребительские кредиты", callback_data="crd_1")
crd_btn_2 = types.InlineKeyboardButton(text="Бизнес кредиты", url="https://www.cbk.kg/ru/consumer/loan/biznes-kredity")
crd_btn_3 = types.InlineKeyboardButton(text="Агрокредиты", url="https://www.cbk.kg/ru/consumer/loan/agro-kredity")
crd_btn_4 = types.InlineKeyboardButton(text="Лизинг", url="https://www.cbk.kg/ru/consumer/loan/lizing")
crd_btn_5 = types.InlineKeyboardButton(text="Кредитный калькулятор", url="https://www.cbk.kg/ru/calculator/loan")
credit_markup.add(crd_btn_1, crd_btn_2, crd_btn_3, crd_btn_4, crd_btn_5)

menu_markup = types.InlineKeyboardMarkup(row_width=1) #кнопка возврата в меню
menu_btn_1 = types.InlineKeyboardButton(text="Вернуться в основное меню", callback_data="menu_1")
menu_markup.add(menu_btn_1)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1":
        bot.send_message(call.message.chat.id, '''MBank Online\n
Простой и удобный сервис позволяющий управлять 
своими денежными средствами, оплачивать около 300 услуг, 
совершать переводы между счетами, получать информацию
об операциях по Вашим счетам и многое другое с помощью 
мобильного телефона в любое время, в любом месте!\n
✅Все операции производятся с помощью любого мобильного устройства\n
✅Оплата около 300 услуг круглосуточно (24/7), даже при нулевом балансе телефона\n
✅Подключение услуги — бесплатно,никакой абонентской платы!\n
Подробнее вы можете прочитать по ссылке https://www.cbk.kg/mobile-banking?utm_source=cbk&utm_campaign=mbank&utm_medium=homepage\n
Так же можете устовить приложение MBANK по ссылке https://play.google.com/store/apps/details?id=com.maanavan.mb_kyrgyzstan
''', reply_markup=menu_markup)
    elif call.data == "2":
        bot.send_message(call.message.chat.id, '''✅Отличный баланс цена-качество\n
✅Принимаются во всех странах мира\n
✅Для платежей за границей и в Интернете\n
Стоимость выпуска – 350 сом\n
Годовое обслуживание 300 сом\n
Для выпуска банковской карты Вам нужно прийти в офис нашего банка или оформить её онлайн по ссылке https://www.cbk.kg/cards/apply/vc\n
Сроки готовности карт:
по г. Бишкек – 48 часов.
Остальные населенные пункты КР – 72 часа
Карта выдается лично владельцу при предоставлении оригинала паспорта и оплаты.
Подробнее вы можете прочитать по ссылке https://www.cbk.kg/cards?utm_source=cbk&utm_campaign=visa&utm_medium=homepage
''', reply_markup=menu_markup)
    elif call.data == "wlc_1":
        bot.send_message(call.message.chat.id, "Чем я могу Вам помочь?", reply_markup=keyboard)
    elif call.data == "3":
        bot.send_message(call.message.chat.id, '''Можно открыть счёт в сомах или иностранной валюте\n
✅Ведение счета осуществляется бесплатно\n
✅Минимальный остаток на счете не требуется\n
✅Все виды расчетно-кассового обслуживания физическим лицам предоставляются по выгодной тарифной сетке\n
Услуги для владельца счета в рамках расчетно-кассового обслуживания:\n
· Зачисление на счет средств, поступивших в безналичном порядке
· Перевод (перечисление) денежных средств со счета\n
Операции с наличными :\n
· Прием и выдача денежных средств
· Пересчет и проверка денежных купюр
· Конверсионные и валютно-обменные операции
· Покупка и продажа наличной иностранной валюты по курсу банка с зачислением средств на счет
· Информирование об операциях по счетам - смс оповещение\n
Подробнее с тарифами на расчетно-кассовое обслуживание можете ознакомиться по ссылке https://www.cbk.kg/ru/consumer/fares
''', reply_markup=menu_markup)
    elif call.data == "4":
        bot.send_message(call.message.chat.id, "Какой вид кредита вас интересует?", reply_markup=credit_markup)
    elif call.data == "crd_1":
        bot.send_message(call.message.chat.id, '''«Потребительский кредит»\n
Описание кредита:\n
· Кредит предоставляется физическим лицам, индивидуальным предпринимателям
· Целевое назначение: любые потребительские цели;
· Валюта кредита: сом;
· Сумма кредита: от 5 000 сом до 2 500 000 сом;
· Срок кредита: от 3 до 60 месяцев;
· Процентная ставка: от 22%-29,988%
· График платежей: аннуитет (ежемесячно равными платежами)\n
ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ВЫ МОЖЕТЕ ПОЛУЧИТЬ ДВУМЯ СПОСОБАМИ:\n
1. В режиме офлайн -  с посещением офиса Банка:\n
· до 150 000 сом – НУЖЕН ТОЛЬКО ПАСПОРТ! БЕЗ ЗАЛОГА И ПОРУЧИТЕЛЬСТВА! Выдача кредита всего за 1 день!
· от 150 001 до 250 000 сом – БЕЗ ЗАЛОГА, ПОД ПОРУЧИТЕЛЬСТВО! Выдача кредита всего за 1 день!
· от 250 001 до 2 500 000 сом – Выдача кредита всего за 2 рабочих дня, под залог недвижимости!
· Процентная ставка - от 22% годовых;
· Комиссия - 0%!\n
2. В режиме онлайн - удаленно, находясь в любом месте:\n
· До 100 000 сом - в течение 1 часа, с 08:30 до 20:00, без выходных!
· Без залога и поручительства!
· Без посещения офиса Банка!
· Без документов!
· Процентная ставка: 29,58% годовых
· Комиссия за дистанционное обслуживание клиентов - 0%\n
При оформлении онлайн кредита Вам не нужно ехать в офис банка, у вас есть возможность получить кредит, находясь в любом месте!\n
Инструкцию по оформлению онлайн кредита вы можете посмотреть по ссылке https://www.cbk.kg/ru/consumer/loan/online-kredit-mbank\n
3. «Кредит за час»\n
Описание кредита:\n
· Кредит предоставляется физическим лицам, индивидуальным предпринимателям
· Целевое назначение: покупка товаров/услуг у Партнеров Банка;
· Валюта кредита: сом;
· Сумма кредита: от 5 000 сом до 250 000 сом, в течение 1 часа;
· Срок кредита: От 3 до 24 месяцев;
· Процентная ставка:  29,988%;
· Обеспечение: приобретаемый товар;
· График платежей: аннуитет (ежемесячно равными платежами);\n
4. Ипотечный кредит «Мой дом»\n
Описание кредита:\n
· Кредит предоставляется физическим лицам, индивидуальным предпринимателям
· Целевое назначение: на приобретение/реконструкцию и утепление жилой недвижимости; завершение строительства жилой недвижимости рефинансирование не проблемных ипотечных кредитов в других ФКО;
· Валюта кредита: сом;
· Сумма: от 400 000 сом до 8 000 000 сом;
· Процентная ставка: от 17,99 %;
· Срок кредита: до 10 лет;
· Залоговое обеспечение: приобретаемая жилая недвижимость;
· Обязательное условие: первоначальный взнос - от 30% покупной стоимости жилой недвижимости. При отсутствии собственного вклада у участника, допускается предоставление дополнительного залога в виде недвижимости;\n
5. Автокредит\n
Описание кредита:\n
· Кредит предоставляется физическим лицам, индивидуальным предпринимателям
· Целевое назначение: покупка автотранспорта;
· Валюта кредита: сом;
· Сумма: от 50 000 сом до 1 000 000 сом;
· Процентная ставка: от 24 %*;
· Срок кредита: до 36 месяцев;
· Залоговое обеспечение: приобретаемый автотранспорт;\n
Обязательное условие: первоначальный взнос - от 30% покупной стоимости автотранспорта
''', reply_markup=menu_markup)
    elif call.data == "wlc_2":
        bot.send_message(call.message.chat.id, '''ЦЕНТРАЛЬНЫЙ ОФИС\n
ул. Тоголок Молдо, 54а
Бишкек, Кыргызстан, 720033\n
📞 3333(О!, Beeline, Megacom)
+996 (312) 61 33 33
+996 (556) 61 33 33
+996 (770) 33 33 69
+996 (701) 33 33 69\n
8 (800) 551 47 22
(бесплатно для номеров РФ)
''', reply_markup=menu_markup)
    elif call.data == "menu_1":
        bot.send_message(call.message.chat.id, text="Чем я могу Вам помочь?", reply_markup=keyboard)

bot.polling()