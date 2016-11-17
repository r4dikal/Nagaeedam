# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import urllib
import json
import redis
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
bot = telebot.TeleBot("276747750:AAHVDkuqJ8ySqoOz-uNU71jYGMlgRAlr1S0")
R = redis.StrictRedis(host='localhost', port=6379, db=0)

if not R.get("nagaeedam:inline:used") :
    R.set("nagaeedam:inline:used",0)

@bot.message_handler(commands=['start','help'])
def start(m):
    try:
        text = u"برا تو هم پیش اومده یه وقتی یکی تو یه گروهی یا جای دیگه یکی یه چیزی میگه و میخوای بگی نگاییدم و دوس داشته باشی یه جور خاص بش بگی مثلا رل نگاییدم😁 \n من برات این کارو میکنم😅\nاول  توی باکس ارسال پیام بنویس \n@Nagaeedam_bot \nبعد جلوش یه فاصله بزار و مثلا بنویس \nIn Rell \nبعد بالای باکس چتت یه شکلک میاد ، روش بزن ، هرجا هستی یه استیکر میفرسته که پایینش نوشته : In Rell نگاییدم ( هرچی جای In Rell بزاری همونو مینویسه )\nیا اینکه رو این دکمه که پایین این متنه کلیک کن و یه چت انتخاب کن و بنویس چی رو نگاییدی 😂\nبرو حال کن به رفیقات هم معرفیم کن D:"
        markup = types.InlineKeyboardMarkup()
        R.sadd("nagaeedam:members",m.from_user.id)
        markup.add(types.InlineKeyboardButton(u"برو به حالت اینلاین",switch_inline_query=""))
        bot.send_message(m.chat.id,text,reply_markup=markup)
    except Exception as e:
        print(e)

@bot.message_handler(commands=['stats'])
def stats(m):
    try:
        bot.send_message(m.chat.id,u"*Users* : {}\n*Inline Used* : {}\n\n*Developer* : @Amir\_h".format(R.scard("nagaeedam:members"),R.get("nagaeedam:inline:used")),parse_mode="Markdown")
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query.split()) == 1)
@bot.inline_handler(lambda query: len(query.query.split()) == 2)
@bot.inline_handler(lambda query: len(query.query.split()) == 3)
@bot.inline_handler(lambda query: len(query.query.split()) == 4)
@bot.inline_handler(lambda query: len(query.query.split()) == 5)
def naga(query):
    try:
        nagaeedam = query.query
        R.incrby("nagaeedam:inline:used",1)
        text = urllib.urlencode({u'txtclr': u'000000', u'txt': nagaeedam + u" نـگاییـدم", u'txtfit': u'max', u'txtsize' : u'200', u'txtfont' : u'PT Serif,Bold'})
        text2 = text.replace(u"+",u"%20")
        link = u"http://copierteam.imgix.net/e642-t.png?{}".format(text2)
        urllib.urlretrieve(link, "naga.png")
        filee = open("naga.png","rb")
        mess = bot.send_sticker(-179123621,filee)
        sticker = mess.sticker.file_id
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton(u"برو به حالت اینلاین",switch_inline_query=""))
        markup2.add(types.InlineKeyboardButton(u"!منو استارت کن",url=u"https://telegram.me/Nagaeedam_bot?start=new"))
        r = types.InlineQueryResultCachedSticker('1', sticker)
        r1 = types.InlineQueryResultArticle('2', u'منو به دوستات معرفی کن', types.InputTextMessageContent(u"برا تو هم پیش اومده یه وقتی یکی تو یه گروهی یا جای دیگه یکی یه چیزی میگه و میخوای بگی نگاییدم و دوس داشته باشی یه جور خاص بش بگی مثلا رل نگاییدم😁 \n من برات این کارو میکنم😅\nاول  توی باکس ارسال پیام بنویس \n@Nagaeedam_bot \nبعد جلوش یه فاصله بزار و مثلا بنویس \nIn Rell \nبعد بالای باکس چتت یه شکلک میاد ، روش بزن ، هرجا هستی یه استیکر میفرسته که پایینش نوشته : In Rell نگاییدم ( هرچی جای In Rell بزاری همونو مینویسه )\nیا اینکه رو دکمه اولیه که پایین این متنه کلیک کن و یه چت انتخاب کن و بنویس چی رو نگاییدی 😂\nبرو حال کن به رفیقات هم معرفیم کن D:"),reply_markup=markup2)
        if R.sismember("nagaeedam:members",query.from_user.id) :
            bot.answer_inline_query(query.id,[r,r1])
        elif not R.sismember("nagaeedam:members",query.from_user.id) :
            bot.answer_inline_query(query.id,[r,r1],switch_pm_text="!منو استارت کن",switch_pm_parameter="/start")
    except Exception as e:
        print(e)

bot.polling(True)

