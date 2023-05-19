import pandas as pd
import gspread
import time
from telebot import types
from gspread_formatting import *
from datetime import datetime
import random
from pytz import timezone
import openai
from keep_alive import keep_alive
import telebot

bot = telebot.TeleBot("6027423492:AAFr0Ly8H9DuTN2JuKq9VwG0PNaSSkDyoC8")
openai.api_key = "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"

bot.set_my_commands([
    types.BotCommand(command="/fill_the_form", description="ابدأ بتعبئة النموذج"),
    types.BotCommand(command="/direct_question5", description="ضع الظرف بشكل مباشر"),
    types.BotCommand(command="/cancel", description="للإلغاء"),
    types.BotCommand(command="/submission", description="تسليم ملفات"),
    types.BotCommand(command="/reminder", description="خاص بالمسؤولين"),
    types.BotCommand(command="/ai_bot", description="بوت الذكاء الاصطناعي نسخة تجريبية"),
    types.BotCommand(command="/help", description="للمساعدة")

])

#######################################
gc = gspread.service_account(filename="data_ltl.json")
sh = gc.open("احصائيات الفصل الثاني")
wks = sh.worksheet("الاسبوع رقم(7) ")

#######################################
sh2 = gc.open("استرداد")
wks2 = sh2.worksheet("الورقة1")
#######################################

###############################################################################################################################
################################################### GET DATA FROM #############################################################

link = "https://docs.google.com/spreadsheets/d/"

sheat_id = "13-AisgWgw5lVFlenPszq8pvFO02jusY-MDKZPLZzRIk"

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheat_id}/export?format=csv", index_col=False)

###############################################################################################################################
all_data = []
data_msg = {}


def data():
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheat_id}/export?format=csv", index_col=False)

    for count in range(len(df['المعرف'])):
        i = str(df['المعرف'][count]).replace("\n", "")
        a = str(df['اسم المتطوع'][count]).replace("\n", "")
        s = str(df['اسم الطالب'][count]).replace("\n", "")

        all_data.append(["0" + str(i), a, s])

        masseag = f"a : {a}\ns : {s}\ni : 0{i}"
        msg = masseag.replace("a", "اسم المتطوع").replace("s", "اسم الطالب").replace("i", "رقم الهاتف (المعررف)")
        data_msg["0" + str(i)] = msg


data()

################################################################################################################
##############################################################################################
##################################################################################


#######################################################
dataframe = wks2.row_values(2)
#######################################################
if dataframe != []:
    wks = sh.worksheet(dataframe[1])

#######################################################

start_time = time.time()

############################  Time  #############################
#

t = 0
timee = 60 * 60 * 24 * 7  #
if dataframe != []:
    t = dataframe[0].replace("٫", ".")
    t = float(t)
    timee = timee - t

#################################################################

chat_id_users = []

##############################################################


#################################################################
###########################important 1###########################
#################################################################
if dataframe != []:
    a = str(dataframe[2].replace("[", "").replace("]", "")).split(",")
    if a != ['']:
        for i in a:
            if int(i) not in chat_id_users:
                chat_id_users.append(int(i))


#################################################################
###########################important 2###########################
#################################################################
def test_chat_id_users():
    T = []
    F = []
    for i in chat_id_users:
        try:
            m = bot.send_message(i, "تجريب......")
            bot.delete_message(m.chat.id, m.message_id)
            T.append(i)
        except:
            F.append(i)

    print(T, "\n\n")
    print(F)


#################################################################
###########################important 3###########################
#################################################################


message_privet = ["{واللَّه ولي المتقين}(الجاثية 19).",
                  "{وَالْعَاقِبَةُ لِلْمُتَّقِينَ}(الأعراف 128).",
                  "{ولَكن البر من اتقى}(البقرة 189).",
                  "{ومن يتق اللَّه يجعل له من أمره يسرًا}(الطلاق 4).",
                  "{واتقوا اللَّه لعلكم تفلحون}(آل عمران 200).",
                  "﴿ فاذكروني أذكركم واشكروا لي ولا تكفرون ﴾[البقرة: 152].",
                  "﴿ يا أيها الذين آمنوا إذا لقيتم فئةً فاثبتوا واذكروا اللَّه كثيرًا لعلكم تفلحون ﴾[الأنفال: 45].",
                  "﴿ كل من عليها فانٍ * ويبقى وجه ربّك ذو الجلال والإكرام ﴾[الرحمن: 26 – 27].",
                  "﴿ ادعوا ربكم تضرعًا وخفيةً إنه لا يحب المعتدين ﴾[الأعراف: 55].",
                  "﴿ الذين آمنوا وتطمئن قلوبهم بذكر اللَّهِ ألا بذكر اللَّه تطمئِن القلوب ﴾[الرعد: 28].",
                  "﴿ واذكر اسم ربّك وتبتل إليه تبتيلًا ﴾[المزمل: 8].",
                  "﴿ قد أفلح من تزكى * وذكر اسم ربه فصلى ﴾[الأعلى: 14، 15].",
                  "{وَلَوْ أَنَّهُمْ آمَنُوا وَاتَّقَوْا لَمَثُوبَةٌ مِنْ عِنْدِ اللَّهِ خَيْرٌ ۖ لَوْ كَانُوا يَعْلَمُونَ}﴿ البقرة 103﴾.",
                  "{اللَّه ولي الذين آمنوا يخرجهم من الظلمات إلى النور} ﴿البقرة ٢٥٧ ﴾.",
                  "{إن أكرمكم عند اللَّه أتقاكم إن اللَّه عليم خبير} (الحجرات 13) .",
                  "﴿ وأنفقوا في سبيل اللَّه ولا تلقوا بِأيديكم إلى التهلكة وأحسنوا إن اللَّهَ يحب المحسنين ﴾[البقرة: 195].",
                  "﴿ ولا تصعر خدك للناس ولا تمش في الأرض مرحًا إن اللَّه لا يحب كل مختالٍ فخورٍ ﴾[لقمان: 18].",
                  "﴿ ولا تقولن لشيءٍ إني فاعل ذلك غدًا * إلا أن يشاء اللَّه واذكر ربك إذا نسيت وقل عسى أن يهدين ربي لأقرب من هذا رشدًا ﴾[الكهف: 23، 24].",
                  ]

txt_prv = [
    "قـالَ تَـعَالَى : ",
    "كيفكم؟...🌿😊😊😍😍",
    "إن شاء الله تكونوا بخير...",
    "ما بحب اكون ثقيل عليكم...🙁🙁😍",
    "بس حبيت اذكركم *تعبوا النموذج* لأنه كثير مهم",
    " وبس وللّه...😂😊❤️"
]


############################################################################################################################################################################################
################################################################################################################################


@bot.message_handler(commands=["remiss246"])
def remiss(message):
    if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:

        bot.send_message(message.chat.id, "قد يستغرق الامر بعض من الوقت يرجى الانتظار....")
        gc_name = gspread.service_account(filename="data_ltl.json")

        sh_name = gc_name.open("احصائيات الفصل الثاني")

        #####################################################################################
        worksheet_list = sh_name.worksheets()

        wsl = []
        for i in worksheet_list:
            wsl.append(i.index)

        all_name_moqser = []
        for num_p in wsl[:-1]:
            a1 = sh_name.get_worksheet(num_p).get('A2:A')
            a2 = sh_name.get_worksheet(num_p).get('J2:J')
            for (x, y) in zip(a1, a2):
                if y not in [[], [" "], ["  "], [""], [None]]:
                    all_name_moqser.append(x[0])

        l = all_name_moqser
        name_with_number = dict((x, l.count(x)) for x in set(l))

        namelist1 = []
        namelist2 = []
        namelist3 = []
        namelist4 = []
        namelist5 = []

        for i in name_with_number.keys():
            if name_with_number[i] == 1:
                namelist1.append((i + ":" + (" " * (25 - len(i))) + "مقصر(1)"))

            if name_with_number[i] == 2:
                namelist2.append(i + ":" + (" " * (25 - len(i))) + "مقصر(2)")

            if name_with_number[i] == 3:
                namelist3.append(i + ":" + (" " * (25 - len(i))) + "مقصر(3)")

            if name_with_number[i] == 4:
                namelist4.append(i + ":" + (" " * (25 - len(i))) + "مقصر(4)")

            if name_with_number[i] > 4:
                namelist5.append(i + ":" + (" " * (25 - len(i))) + "مقصر(اكثر من 4 مقصر)")

        moqsr1 = ""
        moqsr2 = ""
        moqsr3 = ""
        moqsr4 = ""
        moqsr5 = ""

        for i in namelist1:
            moqsr1 += i + "\n"

        for i in namelist2:
            moqsr2 += i + "\n"

        for i in namelist3:
            moqsr3 += i + "\n"

        for i in namelist4:
            moqsr4 += i + "\n"

        for i in namelist5:
            moqsr5 += i + "\n"

        if moqsr5 == "":
            moqsr5 = """
.........

لا يوجد أحد عليه (اكثر من 4 مقصر)  ‼️‼️

.........
"""
        bot.send_message(message.chat.id, moqsr1)
        bot.send_message(message.chat.id, moqsr2)
        bot.send_message(message.chat.id, moqsr3)
        bot.send_message(message.chat.id, moqsr4)
        bot.send_message(message.chat.id, moqsr5)

    else:
        bot.send_message(message.chat.id, "شكراً لـ اهتمامك و اكتشاف الأوامر هاي بس هذا الأمر خاص بالمسؤولين فقط...")


##################################################################################
###############################################################################################
#################################################################################################################
@bot.message_handler(commands=["add"])
def add(message):
    if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:
        data()
        bot.send_message(message.chat.id, "تم إجراء التعديل بنجاح...")
    else:
        bot.send_message(message.chat.id, "شكراً لـ اهتمامك و اكتشاف الأوامر هاي بس هذا الأمر خاص بالمسؤولين فقط...")


###############################################################################################################################
def sheet_format():
    wks.format("A1:K1", {
        "backgroundColor": {
            "red": -249,
            "green": -203,
            "blue": -156
        },
        "horizontalAlignment": "RIGHT",
        "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            },
            "fontSize": 14,
            "bold": True
        }
    })

    wks.format("A2:K200", {
        "backgroundColor": {
            "red": 1,
            "green": 1,
            "blue": 1
        },
        "horizontalAlignment": "RIGHT",
        "textFormat": {
            "foregroundColor": {
                "red": 0,
                "green": 0,
                "blue": 0
            },
            "fontSize": 12,
            "bold": False
        }
    })
    wks.format("J", {
        "backgroundColor": {
            "red": -204,
            "green": 255,
            "blue": 255
        },
        "horizontalAlignment": "RIGHT",
        "textFormat": {
            "foregroundColor": {
                "red": 1,
                "green": 1,
                "blue": 1
            },
            "fontSize": 13,
            "bold": True
        }
    })
    wks.format("J1", {
        "horizontalAlignment": "RIGHT",
        "textFormat": {
            "foregroundColor": {
                "red": 1,
                "green": 1,
                "blue": 1
            },
            "fontSize": 14,
            "bold": True
        }

    })
    set_column_width(wks, 'A:K', 220)
    set_column_width(wks, 'I', 280)
    set_row_height(wks, "1", 55)
    wks.format("A1:Z200", {"wrapStrategy": "WRAP"})
    set_right_to_left(wks, True)


############################################################################################################################################################################################
################################################################################################################################
@bot.message_handler(commands=["format"])
def format(message):
    if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:
        sheet_format()
        bot.send_message(message.chat.id, "تم عمل فورمات (تنسيق) للشيت بنجاح......")
    else:
        bot.send_message(message.chat.id, "انت/ي كبيرة كثير بـِ عيونا بس منعتذر منك مش مسؤول بـِ المبارة...")


############################################################
############################################################################################################################################################################################
@bot.message_handler(commands=["pin", "unpin"])
def pin_message(message):
    if message.text == "/pin":
        if message.chat.id in [1066196464, 989404678, 5767317562]:
            bot.send_message(message.chat.id, "ارجو ادخال الرسالة التي تريد تثبيتها عند جميع الاعضاء :")
            bot.register_next_step_handler(message, pin2)
        else:
            bot.send_message(message.chat.id, "انت/ي كبيرة كثير بـِ عيونا بس منعتذر منك مش مسؤول بـِ المبارة...")
    if message.text == "/unpin":
        if message.chat.id in [1066196464, 989404678, 5767317562]:
            bot.send_message(message.chat.id, "قيد التطوير.....")
        else:
            bot.send_message(message.chat.id, "انت/ي كبيرة كثير بـِ عيونا بس منعتذر منك مش مسؤول بـِ المبارة...")


def pin2(message):
    if message.text == "/cancel":
        bot.send_message(message.chat.id, "تم الالغاء")
    else:
        for i in chat_id_users:
            msg = bot.send_message(i, str(message.text))
            bot.pin_chat_message(i, msg.message_id)
            bot.send_message(message.chat.id, str(msg.message_id))


############################################################################################################################################################################################
############################################################################################################################################################################################
############################################################################################################################################################################################
ai = []


@bot.message_handler(commands=["ai_bot"])
def ai_bot(message):
    if message.chat.id not in chat_id_users:
        chat_id_users.append(message.chat.id)
    if message.text == "/cancel":
        bot.send_message(message.chat.id, "أراك لاحقا...😊👋")

        if "@admin0" not in ai:
            if ai != []:
                ai.pop(0)
                if ai != []:
                    ai.pop(0)

    else:

        if message.text == "@admin0":
            bot.send_message(message.chat.id, "تم ايقاف البوت من قبل المسؤول يرجى التواصل معهم.")

        if message.text == "/ai_bot":
            bot.send_message(message.chat.id,
                             'مرحبا..😊❤️\n\n انا اسمي بوت نحب لنحيا..\n\n انا بوت ذكاء إصطناعي نسخة *تجريبية* بقدر اساعد في اشياء مثل :\n\n اجد لك نتائج بحث ,, ابحثلك عن موضوع ,, اذا بدك اسئلة لمادة ولصف معين ..\n\n انا بوت تجريبي لازم تكون رسالتك دقيقة عشان اقدر اساعدك مثال :\n\n"ارسل لي موضوع عن مرض سرطان الاطفال في 20 سطر " \n\n بتقدر تعمل إغلاق عن طريق أمر :(/cancel).. \n\nماذا تريد مني ان افعل الان؟')
            message.text = ""
            bot.register_next_step_handler(message, ai2)

        if message.text == "ai_bot2":
            bot.send_message(message.chat.id, " ماذا تريد مني ان افعل ايضا؟\n\n للخروج من البوت اضغط (/cancel)")
            bot.register_next_step_handler(message, ai2)

        if "@admin0" in ai:
            bot.send_message(message.chat.id, "تم ايقاف البوت من قبل المسؤول يرجى التواصل معهم.")


def ai2(message):
    if message.text == "/cancel":
        ai_bot(message)

    else:
        if message.text == "@admin0":
            ai.append("@admin0")

        if message.text == "@admin1":
            if ai != []:
                ai.pop(0)
                ai.append("@admin1")
            else:
                ai.append("@admin1")

        if "@admin1" in ai:
            for admin in [1066196464, 989404678, 5767317562]:
                bot.send_message(admin, "البوت عاد للعمل :) ")
            ai.pop(0)

        if "@admin0" in ai:
            for admin2 in [1066196464, 989404678, 5767317562]:
                bot.send_message(admin2, "تم تعطيل البوت حاليا :( ")
            message.text = "@admin0"
            ai_bot(message)


        else:
            if message.text == "@admin1":
                message.text = "/ai_bot"
                ai_bot(message)

            else:

                try:
                    mes = bot.send_message(message.chat.id, "يرجى الإنتظار حتى انتهي من العمل...")
                    sh3 = gc.open("نتائج بحث بوت الذكاء الاصطناعي")
                    wks3 = sh3.worksheet("ورقة(1)")

                    wks3.append_row(
                        [message.text, str(message.chat.id), message.from_user.username, message.from_user.first_name])
                    wks3.format("A1:Z200", {"wrapStrategy": "WRAP"})
                    set_right_to_left(wks3, True)

                    prompt = str(message.text)

                    # Generate a response using the `davinci-codex-arabic` engine
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=prompt,
                        max_tokens=3500,
                        n=1,
                        temperature=0.7,
                        presence_penalty=0.6,
                        frequency_penalty=0

                    )

                    # Print the generated response
                    bot.send_message(message.chat.id, "البوت :")
                    bot.send_message(message.chat.id, response.choices[0].text)
                    bot.delete_message(message.chat.id, mes.message_id)
                    message.text = "ai_bot2"
                    ai_bot(message)

                except:
                    sh3 = gc.open("نتائج بحث بوت الذكاء الاصطناعي")
                    wks3 = sh3.worksheet("ورقة(1)")

                    wks3.append_row(
                        [message.text, str(message.chat.id), message.from_user.username, message.from_user.first_name,
                         "مخرب"])

                    wks3.format("A1:Z200", {"wrapStrategy": "WRAP"})
                    set_right_to_left(wks3, True)
                    bot.send_message(message.chat.id,
                                     "يوجد مشكلة بالبوت  في حال تكرر ظهور هذه الرسالة مع تائج بحث محتلفة يرجى اخبار المسؤول باسرع وقت ممكن....")
                    for i in [1066196464, 989404678, 5767317562]:
                        bot.send_message(i,
                                         f"‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️\nيوجد مخرب ببوت الذكاء الاصطناعي ارجو ان يتم الطلب منه عمل تصوير شاشة للبوت.. \n المخرب هو : @{message.from_user.username}")


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

@bot.message_handler(commands=["start"])
def welcom(message):
    if message.chat.id not in chat_id_users:
        chat_id_users.append(message.chat.id)

    bot.send_message(message.chat.id,
                     '''
                     اهلا فيكم  ببوت التلجرام الخاص بمبادرة  نُحب لنحيا...
                     
                     كيفكم شو الاخبار...؟
                     
                     من البداية فكرة البوت مٌنطَلِقة من مَبدَأ التطوير و التسهيل على مٌتسبين المبادرة وتحمل المسؤولية الي جِدًا كبيرة وعظيمة...
                     
                     "أسأل الله لي ولكم التوفيق والهداية، وأسأله أن يجمع شملنا ويوحّد كلمتنا، وأن يتولانا بعين رعايته، وأن يحفظنا وإياكم من كل مكروه"
                     
                     
                     شرح بسيط عن أوامر البوت :
                     
                     1- /fill_the_form  :
                     يستخدم هذا الأمر لبدأ تعبئة النموذج وهوه خاص بالمتطوعين...
                     
                     2- /direct_question5
                     اذا كانت لديك مشكلة او ظرف ولم تتمكن من الاعطاء خلال الاسبوع ادخل هذا الأمر... 
                     
                     3- /cancel  :
                     يستخدم هذا الأمر لإلغاء تعبئة النموذج اثناء تعبئة الموذج او الغاء تسليم الملفات او حتى عمل بوت الذكاء الاصطناعي...
                     
                     4- /submission  :
                     يستخدم هذا الأمر لتسليم أي شيء تريد تسليمه (فيديو ,صور , ملف ورد ,ملف pdf ,رسالة عادية ,تغذية راجعة ,ملاحظات) وهوه خاص بالتطوعين...
                     
                     5- /reminder  :
                     يستخدم هذا الأمر في تذكير المتطوعين بتعبئة الفورم الاسبوعي يمكن استخدامه في اي وقت وهوه أمر خاص فقط بالمسؤولين عن المبادرة...
                     
                     6-/ai_bot :
                     يستخدم هذا الأمر في الدخول الي بوت الذكاء الإصطناعي يستطيع اتمام بعض المهم بدقة مثل كتابة نص او كتابة اسئلة للطلاب او حل الرياضيات بدقة عالية او اشياء اخرى ,,يتم ايقافه من فبل المسؤول فقط...
                     
                     7- /help  :
                     يستخدم هذا الأمر للمساعدة و إظهار التعليمات الأساسية لإستخدام البوت...
                     
                     ‼️ملاحظة :
                     
                     ارجوا من الجيمع الطِّلاع على التعليمات قبل اي شيء من خلال الأمر :
                     /help
                     
                     هاي الرسالة راح تظهر فقط لمرة واحدة او عند الضغط على أمر :
                     /start
                     
                     ارجوا استخدام البوت فقط للقيام بمهمته وشكرا....
                     ''')


############################################################################################################################################
#################################################### reminder message handler ##############################################################
############################################################################################################################################


@bot.message_handler(commands=["reminder"])
def privet(message):
    if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:
        for i in chat_id_users:
            bot.send_message(i,
                             f"{txt_prv[0]}\n\n{random.choice(message_privet)}\n\n{txt_prv[1]}\n\n{txt_prv[2]}\n\n{txt_prv[3]}\n\n{txt_prv[4]}\n\n{txt_prv[5]}")
        bot.send_message(message.chat.id, "تم تذكير المتطوعين  :)")

    else:
        bot.send_message(message.chat.id, "انت/ي كبيرة كثير بعيونا بس منعتذر منك مش مسؤول بالمبارة...")


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

send_delete = []


@bot.message_handler(commands=["send_all", "cancel_send"],
                     content_types=['document', 'photo', 'audio', 'video', 'voice', "text", "command", "chat"])
def send_to_all(message):
    if message.text == "/cancel":
        bot.send_message(message.chat.id, "تم الإلغاء...")
        send_delete.clear()

    if message.text == "/cancel_send":
        bot.send_message(message.chat.id, "تم الغاء الإرسال للجميع....\nسوف يبقى العداد يعمل حتى ينتهي من العد..")
        count = 0
        for i in chat_id_users:
            bot.delete_message(i, message_id=send_delete[count])
            count += 1
        send_delete.clear()

    if message.text == "/send_all":
        send_delete.clear()

        if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:
            bot.send_message(message.chat.id, "ارجو ادخال ما تريد ان ترسله للمتطوعين :")
            bot.register_next_step_handler(message, send_to_all2)

        else:
            bot.send_message(message.chat.id, "انت/ي كبيرة كثير بـِ عيونا بس منعتذر منك مش مسؤول بـِ المبارة...")


def send_to_all2(message):
    if message.text == "/cancel":
        send_to_all(message)

    else:

        mes = bot.reply_to(message, " حسنا سوف يتم الإرسال..\nأرجو الإنتظار لحظة 🌿😊 ")

        for i in chat_id_users:
            send_del2 = bot.forward_message(i, from_chat_id=message.chat.id, message_id=message.message_id)
            send_delete.append(send_del2.message_id)

        text0 = "تم الإرسال للجميع..."
        text1 = "بتقدر تلغي الإرسال بالضغط على :"
        text2 = "/cancel_send"
        text3 = "معك *10* ثواني للالغاء"
        sent = bot.send_message(message.chat.id, f"{text0}\n{text1}\n{text2}\n\n{text3}")
        id_c = sent.chat.id

        time.sleep(1)
        for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            text3 = f"معك *{str(i)}* ثواني للإلغاء"
            bot.edit_message_text(chat_id=id_c, text=f"{text0}\n{text1}\n{text2}\n\n{text3}",
                                  message_id=sent.message_id)
            time.sleep(1)

        time.sleep(1)
        bot.delete_message(chat_id=id_c, message_id=sent.message_id)

        send_to_all(message)
        if send_delete != []:
            bot.send_message(message.chat.id, 'تم الإرسال بنجاح 🌿🌿🌿😊')


############################################################################################################################################
############################################################################################################################################

arbic_num = '٠١٢٣٤٥٦٧٨٩'
chooes_confirm = ["نعم", "حسنا", "حسناً", "ok", "Ok", "اوك", "اوكي", "أوك", "نعماريد", "نعمأريد", "تم", "تسليم",
                  "انهاء", "إنهاء"]
chooes_cansle = ["لا", "لأ", "لاء", "no", "No", "لااريد", "لاأريد", "اعادة", "إعادة", "أعادة", "اعادةادخال",
                 "إعادةادخال", "إعادةإدخال"]

msg_delete = []
user_id_list = []

ans_dict = {}

############################################################################################################################################
########################################################## submission message handler ######################################################
############################################################################################################################################

mes = ""


@bot.message_handler(commands=["submission", "cancel_submission246"],
                     content_types=['document', 'photo', 'audio', 'video', 'voice', "text", "command",
                                    "chat"])  # list relevant content types
def forward(message):
    if message.chat.id not in chat_id_users:
        chat_id_users.append(message.chat.id)

    if message.text == "/submission":
        bot.send_message(message.chat.id, "ادخل المعرف الخاص بك رجاء :")
        bot.register_next_step_handler(message, go)

    if message.text == "/cancel_submission246":
        try:
            bot.delete_message(-1001873591057, message_id=msg_delete[0])
            bot.delete_message(-1001873591057, message_id=msg_delete[1])
            bot.delete_message(message.chat.id, message.message_id)
        except:
            bot.send_message(message.chat.id,
                             "الأمر هذا فقط بعد التسليم شكرا الك لأنك غلبت حالك وكتبت الأمر ...")
            bot.send_message(1066196464,
                             f"لقد حاول احدهم ارسال رسالة تعطي ايرور\n" + "@" + str(message.from_user.username))
        else:
            bot.send_message(message.chat.id,
                             "تم الالغاء...\n\n ملاحظة : راح يضل العداد يعمل حتى ينتهي من العد لا تقلق...😂😊❤️")

        if msg_delete != []:
            msg_delete.pop(0)
            msg_delete.pop(0)

    if message.text == "/cancel":
        bot.send_message(message.chat.id, "تم الغاء التسليم...")

    if message.text == "repetition":
        bot.send_message(message.chat.id, " ارجو التأكد من المعرف الذي ادخلته \nاعد الإدخال رجاء :")
        bot.register_next_step_handler(message, go)


def go(message):
    if message.text == "/cancel":
        forward(message)

    else:
        users_info = data_msg
        user_id = str(message.text).replace(" ", "")

        for i in user_id:
            if i in arbic_num:
                user_id = user_id.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤',
                                                                                                                  '4').replace(
                    '٥', '5')
                user_id = user_id.replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')
                break

        if msg_delete != []:
            msg_delete.pop(0)
            msg_delete.pop(0)

        if user_id in users_info.keys():
            bot.send_message(message.chat.id,
                             "ارجو ارسال الملف (فيديو ,صورة ,ملاحظة نصية, ....الخ) :\n ملاحظة اقصى حد لحجم الملف في تلجرام هوه (2GB)")
            bot.register_next_step_handler(message, go2, user_id, users_info)

        if user_id not in users_info.keys():
            if "/submission" not in user_id:
                message.text = "repetition"
                forward(message)


def go2(message, user_id, users_info):
    if message.text == "/cancel":
        forward(message)

    else:

        mes = bot.reply_to(message, "أرجو الإنتظار لحظة 🌿😊 ")
        bot.send_sticker(message.chat.id,
                         sticker="CAACAgIAAxkBAAEH0B1j8s7HXkVf8eRx7AWpoeJIA7CLNgAC3AAD9wLID1DYvAZ7vfB8LgQ")

        mes_del2 = bot.forward_message(-1001873591057, from_chat_id=message.chat.id, message_id=message.message_id)
        time.sleep(1)
        mes_del = bot.send_message(-1001873591057, users_info[str(user_id)])
        msg_delete.append(mes_del.message_id)
        msg_delete.append(mes_del2.message_id)

        text0 = "تم الاستلام..."
        text1 = "بتقدر تلغي التسليم بالضغط على :"
        text2 = "/cancel_submission246"
        text3 = "معك *10* ثواني للالغاء"
        sent = bot.send_message(message.chat.id, f"{text0}\n{text1}\n{text2}\n\n{text3}")

        id_c = sent.chat.id

        time.sleep(1)
        for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            text3 = f"معك *{str(i)}* ثواني للالغاء"
            bot.edit_message_text(chat_id=id_c, text=f"{text0}\n{text1}\n{text2}\n\n{text3}",
                                  message_id=sent.message_id)
            time.sleep(1)

        time.sleep(1)
        bot.delete_message(chat_id=id_c, message_id=sent.message_id)

        forward(message)
        if msg_delete != []:
            bot.send_message(message.chat.id, 'تم الإستلام شكراً كثيررررررر الك 🌿🌿🌿😊')


ans1 = {}


now_user = {}  ###########@@@@@@@@@########$$$$$$$$!!!      (1)


@bot.message_handler(commands=['fill_the_form', 'cancel', 'help', "clear", "nw246"])
def commands_buttons(message):
    global timee, wks, sh_num, now_user

    #################################################################
    #################################################################
    if message.chat.id not in chat_id_users:
        chat_id_users.append(message.chat.id)

    if (time.time() - start_time) > timee:
        bot.send_message(1066196464, "تذكير الاسبوع........")
        timee = 0
        timee += 60 * 60 * 24 * 7

    if message.text.lower() == "/nw246":

        id_c = message.chat.id
        sent = bot.reply_to(message,
                            'يتم رفع البيانات الرجاء الإنتظار * 5 * ثواني 🌿😊')

        for num in range(len(all_data)):

            find = all_data[num][0]
            cell = wks.find(find)

            if cell is None:
                wks.append_row(
                    [all_data[num][1], all_data[num][2], all_data[num][0], "--", "--", "--", "0", "--", "--", "مقصر",
                     "--"])

        bot.edit_message_text(chat_id=id_c, text='الرجاء الإنتظار * 4 * 🌿😊', message_id=sent.message_id)
        time.sleep(1)

        bot.edit_message_text(chat_id=id_c, text='الرجاء الإنتظار * 3 * 🌿😊', message_id=sent.message_id)
        time.sleep(1)

        bot.edit_message_text(chat_id=id_c, text='الرجاء الإنتظار * 2 * 🌿😊', message_id=sent.message_id)
        time.sleep(1)

        bot.edit_message_text(chat_id=id_c, text='الرجاء الإنتظار * 1 * 🌿😊', message_id=sent.message_id)
        time.sleep(1)

        bot.edit_message_text(chat_id=id_c,
                              text='الرجاء الإنتظار * 0 * 🌿😊\n الوقت غير دقيق (يعتمد على حجم البيانات) ',
                              message_id=sent.message_id)
        bot.send_message(message.chat.id, f"تم بنجاح الاسبوع الحالي هوه : الاسبوع رقم({str(int(wks.index) + 1)}) ")
        time.sleep(2)

        bot.delete_message(chat_id=id_c, message_id=sent.message_id)

        sheet_format()

        bot.send_message(-1001873591057, wks.url)  # @@@@@@@@@@@@@@@@@@@@

        now = datetime.now(timezone('Asia/Amman'))
        date = f"{now.day} / {now.month} / {now.year}"
        time0 = f"(H:{now.hour} :: M:{now.minute})"

        text0 = f"رقم الصفحة : {str(int(wks.index) + 1)}"
        text1 = f"التاريخ : {date}"
        text2 = f"الوقت : {time0}"

        bot.send_message(-1001873591057, f"{str(text0)}\n\n{str(text1)}\n\n{str(text2)}")  # @@@@@@@@@@@@@@

        for i in str(wks.title):
            if i.isnumeric():
                sh_num = int(i) + 1

        sh.add_worksheet(rows=200, cols=1000, title=f"الاسبوع رقم({str(sh_num)}) ")
        wks = sh.worksheet(f"الاسبوع رقم({str(sh_num)}) ")

        wks.append_row(['اسم المتطوع',
                        'اسم الطالب',
                        'المعرف (رقم الهاتف)',
                        'وقت الحصة "الساعة"',
                        'وقت الحصة "التاريخ"',
                        'ما تم شرحة خلال الاسبوع',
                        'مجموع الحصص خلال الاسبوع',
                        'اذا لم تعطي ضع الظرف هنا/هل قمت بستجيل الحصص ام لا',
                        'استجابة الطالب و الأهل وهل يوجد مشاكل',
                        'المقصرين',
                        'وقت تعبئة النموذج'])

    #################################################################
    #################################################################

    if message.text == "/clear":  ###########@@@@@@@@@########$$$$$$$$
        now_user.clear()
        bot.send_message(message.chat.id, "تمت العملية....")

    else:

        if now_user != {}:

            for i in now_user.keys():
                if (now_user[i] != message.chat.id):
                    if (time.time() - i) >= 4 * 60:
                        now_user.clear()

                    else:
                        message.text = "other users"
                break
        if now_user == {}:
            now_user[time.time()] = message.chat.id

    if message.text == "other users":  ###########@@@@@@@@@########$$$$$$$$

        te1 = "مستخدم اخر يقوم بتعبئة الفورم يرجى الانتظار :"
        for a in now_user.keys():
            seconds = 4 * 60 - (time.time() - a)
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            te2 = ("%d:%02d:%02d" % (hour, minutes, seconds)) + " او حتى ينتهي"
            bot.send_message(message.chat.id, f"{te1}\n{te2}")
            break

    if message.text == "/help":
        ans1.clear()
        now_user.clear()  ###########@@@@@@@@@########$$$$$$$$
        bot.send_message(message.chat.id,
                         '''
                         التعليمات :
                         
                         1-يرجى إتباع ما يظهر عند الإجابة على اي سؤال\n في حال عدم ظهور زر المتابعة الى السؤال-- او اعادة السؤال-- بتقدر بكل بساطة تجاوب بـ نعم للمتابعة او لا للإعادة
                         
                         
                         2-الإجابة تكون في رسالة واحدة فقط
                         
                         
                         3-اذا واجهتك اي مشكلة أثناء تعبئة النموذج اضغط على (/cancel) من القائمة سوف يتم الغاء النموذج ثم أعد تعبئته مرة أخرى بالضغط على (/fill_the_form)
                         
                         
                         4-في حال كانت هنالك مشكلة في اعطاء الحصة سواء من الطالب او من المتطوع  يستخدم الامر (/direct_question5) ويعتبر بديل لـ أمر (/fill_the_form) اي اذا تمت تعبئته لن يعتبر المتطوع مقصر
                         
                         
                         5-عند الضغط على مساعدة ( /help) او إلغاء  ( /cancel) سوف يتم حذف ما ادخلته سابقاً
                         
                         
                         6-يمكن تسليم أي شيء يخص المتطوع باستخدام أمر (/submission) بعد ما يتم التسليم بتقدر تلغي التسليم من الرسالة إلي بتظهرلك فقط بعد التسليم
                         
                         
                         @ملاحظة نقطة (5) : \n حتى الأوامر الخاصة بالبوت راح يعتبرها البوت (نص) ما عدا الأمر /cansel
                         
                         
                         7-بوت الذكاء الاصطناعي هوه فقط نسخة تجريبية للمساعدة في بعض المهام لا يستطيع تخزين المعلومات من السؤال السابق, يجب ان تكون رسالتك دقيقة ,, البوت راح يعتبر جميع الاوامر عبارة عن سؤال موجه اله ما عدا الامر ( /cancel)\n\n ‼️*لا يمكنك إرسال رسالة تتعدى 15 سطر له حاول تقسيم الرسائل الطويلة ولا يمكنك إرسال  صور او فيديوهات..  فقط نص *\n\nالروابط التي يرسلها لك اغلبها غير صحيحة,, يتم الخروج منه عن طريق أمر /cansel
                         
                         
                         *  رابط فيديو الشرح للمساعدة :   * https://vimeo.com/801261952
                         
                         
                         **في اي وقت يمكنك التواصل مع المسؤول لـ إي استفسار** \n https://wa.me/qr/O746DANK7V75A1 \n\n\n
                         
                         مواقع التواصل الاجتماعي الخاصة بالمبادرة :
                         
                         💙 Facebook :\n https://www.facebook.com/groups/549789176250199/?ref=share \n\n❤ Instagram :\n https://instagram.com/ltl20.10?igshid=YmMyMTA2M2Y=
                         
                         
                         ''', reply_markup=types.ReplyKeyboardRemove(), disable_web_page_preview=True)

        text01 = (
            '''
            في أوامر خاصة بالمسؤولين فقط وهيه كتالي :
            
            1- /add  :
            
            هذا الأمر يستخدم بعد ما يتم إضافة او حذف متطوع أو اي تعديل اخر من ملف الـ إكسل الموجود في جوجل درايف
            
            ملفاتي >> مبادرة الحسين للسراطان22-23 >> قسم الـ تقني >> الاحصائيات >> الردود >> احصائيات الفصل الثانيي >> بيانات الطلاب (خاصة بالقسم التقني)
            
            2-@admin0  :
            
            هاي رسالة تستخدم لـ إيقاف بوت الذكاء الإصطناعي بعد ما يتم تشغيل البوت من
            أمر(/ai_bot)
            ابعث هاي الرسالة بتوقف البوت عن العمل عند الجميع
            قم بنسخ ولصق الرسالة كما هيه
            
            3-@admin1  :
            
            اذا فقط استخدمت الرسالة السابقة من نقطة 2
            بتقدر ترجع تخلي البوت يشتغل بنفس الطريقة تماما
            من خلال رسالة النقطة 3 قم بنسخ ولصق الرسالة كما هيه
            **يفضل أن يتم أخبار المتطوعين قبل ايقاف او تشغيل البوت
            
            4-/send_all
            
            هذا الأمر يُتيح إرسال رسالة او فيديو او صورة او ملفات وغيرها لكل المتطوعين بتقدر تلغي ألأمر بعد الإرسال او قبل الإرسال عن طريق الأمر (/cancel)
            
            5-/nw246
            هذا الامر خاص ببدأ اسبوع جديد
            
            6-/pin 
            هذا الامر يستخدم في ارسال رسالة لجميع المتطوعين مع تثبيتها لكن لا يمكن ازالة التثبيت لهذا احذر اثناء ارسال الرسالة
            
            7-/remiss246
            هذا الامر يستخدم في جلب اسماء المقصرين يجب التأكد من المقصرين في كل اسبوع والتعديل عليهم اذا لزم قبل استخدام هذا الامر 
            
            8-/format
            يستخدم هذا الامر في حال كنت تريد عمل تنسيق لشيت اكسل للاسبوع الحالي قبل انتهاء موعده ولا يؤثر على عمل اي شيء اخر
            
            وشكرا كثير لجهودك بالمبادرة....
            ''')
        text02 = "أهلا فيك مسؤولنا محمد هاي الرسالة خاصة بس الك بتمنى ما تشاركها مع حدا.. "
        text03 = "أهلا فيكِ مشرفتنا  ميس قفيشة هاي الرسالة خاصة بس الك بتمنى ما تشاركيها مع حدا.. "
        text04 = "أهلا فيكِ مسؤولتنا ميس الصوى هاي الرسالة خاصة بس الك بتمنى ما تشاركيها مع حدا.. "

        if str(message.chat.id) in ['1066196464', "989404678", "5767317562"]:
            if str(message.chat.id) == "1066196464":
                bot.send_message(message.chat.id, f"{text02}\n\n{text01}")

            if str(message.chat.id) == "989404678":
                bot.send_message(message.chat.id, f"{text03}\n\n{text01}")

            if str(message.chat.id) == "989404678":
                bot.send_message(message.chat.id, f"{text04}\n\n{text01}")
        ans_dict.clear()



    elif message.text == "/cancel":
        bot.send_message(message.chat.id, "شكرا لأنك جزء من عيلتنا..😊❤️", reply_markup=types.ReplyKeyboardRemove())
        ans_dict.clear()
        ans1.clear()
        now_user.clear()  ###########@@@@@@@@@########$$$$$$$$

    elif message.text == "/fill_the_form":
        bot.send_message(message.chat.id, "ادخل المعرف الخاص بك رجاء :", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_info)
        ans_dict.clear()
        ans1.clear()


def get_info(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    else:
        users_info = data_msg
        user_id = str(message.text).replace(" ", "")

        for i in user_id:
            if i in arbic_num:
                user_id = user_id.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤',
                                                                                                                  '4').replace(
                    '٥', '5')
                user_id = user_id.replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')
                break

        if user_id in users_info.keys():

            n = str(users_info[str(user_id)]).split("\n")
            mmm = []
            for i in n:
                a = i.find(":") + 2
                mmm.append(i[a:])

            ans_dict["اسم المتطوع"] = [mmm[0]]
            ans_dict["اسم الطالب"] = [mmm[1]]
            ans_dict['المعرف (رقم الهاتف)'] = [user_id]
            text0 = "للمتابعة :"
            text1 = "/continue"
            text2 = "للالغاء :"
            text3 = "/cancel"
            bot.send_message(message.chat.id, users_info[str(user_id)] + f"\n\n{text0}\n{text1}\n{text2}\n{text3}")

            if str(message.text).replace(" ", "") in ["/cancel", "/help", "/fill_the_form"]:
                commands_buttons(message)

            bot.register_next_step_handler(message, question_1)


        else:
            if message.text not in ["/cancel", "/help", "/fill_the_form"]:
                bot.send_message(message.chat.id, "ارجو التأكد من المعرف الخاص بك اعد الإدخال :",
                                 reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(message, get_info)


def question_1(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)
    else:
        user_id = str(message.text)

        bot.send_message(message.chat.id, '1- ارجو ادخال وقت الحصة "الساعة" \n\nمثال: 3:00pm',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, continue_fun_1)


def continue_fun_1(message):
    ans_dict['وقت الحصة "الساعة"'] = [str(message.text)]
    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:
        func(message, ['متابعة الى السؤال الثاني', 'اعادة ادخال السؤال الاول'], question_2)

    else:
        commands_buttons(message)


def question_2(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif (message.text in ["متابعة الى السؤال الثاني"] or str(message.text).replace(" ", "").replace(".",
                                                                                                     "") in chooes_confirm):

        bot.send_message(message.chat.id, '2- ارجو ادخال وقت الحصة "التاريخ" \n\nمثال: الاثنين, 20/12/2022',
                         reply_markup=types.ReplyKeyboardRemove())

        bot.register_next_step_handler(message, continue_fun_2)

    elif (message.text in ["اعادة ادخال السؤال الاول"] or str(message.text).replace(" ", "").replace(".",
                                                                                                     "") in chooes_cansle):
        ans_dict.pop('وقت الحصة "الساعة"')
        question_1(message)


def continue_fun_2(message):
    ans_dict['وقت الحصة "التاريخ"'] = [str(message.text)]
    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:
        func(message, ['متابعة الى السؤال الثالث', 'اعادة ادخال السؤال الثاني'], question_3)


    else:
        commands_buttons(message)


def question_3(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    if (message.text in ["متابعة الى السؤال الثالث"] or str(message.text).replace(" ", "").replace(".",
                                                                                                   "") in chooes_confirm):
        bot.send_message(message.chat.id, '3- ما تم شرحة خلال الاسبوع \n\nضع عنوان الدرس واسم المادة',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, continue_fun_3)

    if (message.text in ["اعادة ادخال السؤال الثاني"] or str(message.text).replace(" ", "").replace(".",
                                                                                                    "") in chooes_cansle):
        message.text = "متابعة الى السؤال الثاني"

        ans_dict.pop('وقت الحصة "التاريخ"')
        question_2(message)


def continue_fun_3(message):
    ans_dict['ما تم شرحة خلال الاسبوع'] = [str(message.text)]
    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:
        func(message, ['متابعة الى السؤال الرابع', 'اعادة ادخال السؤال الثالث'], question_4)


    else:
        commands_buttons(message)


def question_4(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif (message.text in ["متابعة الى السؤال الرابع"] or str(message.text).replace(" ", "").replace(".",
                                                                                                     "") in chooes_confirm):
        bot.send_message(message.chat.id, '4- مجموع الحصص خلال الاسبوع \n\nضع صفر اذا لم تعطي اي حصة',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, continue_fun_4)

    elif (message.text in ["اعادة ادخال السؤال الثالث"] or str(message.text).replace(" ", "").replace(".",
                                                                                                      "") in chooes_cansle):
        message.text = "متابعة الى السؤال الثالث"

        ans_dict.pop('ما تم شرحة خلال الاسبوع')
        question_3(message)


def continue_fun_4(message):
    ans_dict['مجموع الحصص خلال الاسبوع'] = [str(message.text)]

    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:

        func(message, ['متابعة الى السؤال الخامس', 'اعادة ادخال السؤال الرابع'], question_5)  ##############@@@

    else:
        commands_buttons(message)


def question_5(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif (message.text in ['متابعة الى السؤال الخامس'] or str(message.text).replace(" ", "").replace(".",
                                                                                                     "") in chooes_confirm):
        bot.send_message(message.chat.id, '5-هل قمت بستجيل الحصص ام لا ', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, continue_fun_5)

    elif (message.text in ["اعادة ادخال السؤال الرابع"] or str(message.text).replace(" ", "").replace(".",
                                                                                                      "") in chooes_cansle):
        message.text = "متابعة الى السؤال الرابع"
        ans_dict.pop('مجموع الحصص خلال الاسبوع')
        question_4(message)


def continue_fun_5(message):
    ans_dict['اذا لم تعطي ضع الظرف هنا'] = [str(message.text)]

    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:
        func(message, ['متابعة الى السؤال السادس', 'اعادة ادخال السؤال الخامس'], question_6)  ############@@@@@@


    else:
        commands_buttons(message)


def question_6(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif (message.text in ['متابعة الى السؤال السادس'] or str(message.text).replace(" ", "").replace(".",
                                                                                                     "") in chooes_confirm):  ##################@@@@

        bot.send_message(message.chat.id, '6- كيف استجابة الطالب والأهل معك وهل لديك اي مشاكل..؟',
                         reply_markup=types.ReplyKeyboardRemove())

        bot.register_next_step_handler(message, continue_fun_6)

    elif (message.text in ["اعادة ادخال السؤال الخامس"] or str(message.text).replace(" ", "").replace(".",
                                                                                                      "") in chooes_cansle):

        message.text = "متابعة الى السؤال الخامس"
        ans_dict.pop('اذا لم تعطي ضع الظرف هنا')
        question_5(message)


def continue_fun_6(message):
    ans_dict["استجابة الطالب و الأهل وهل لديك اي مشاكل"] = [str(message.text)]
    if message.text in ["/direct_question5"]:
        commands_buttons2(message)

    elif message.text not in ["/cancel", "/help", "/fill_the_form"]:
        func(message, ['متابعة الى التسليم', 'اعادة ادخال السؤال السادس'], question_7)  ############@@@@@@


    else:
        commands_buttons(message)


def question_7(message):
    if message.text in ["/cancel", "/help", "/fill_the_form"]:
        commands_buttons(message)

    elif message.text in ["/direct_question5"]:
        commands_buttons2(message)

    if (message.text in ["متابعة الى التسليم"] or str(message.text).replace(" ", "").replace(".",
                                                                                             "") in chooes_confirm):

        bot.send_message(message.chat.id,
                         "شكراً كثير تم الإستلام بنجاح...😍🌷\n\n\n ‼️هذا ما تم استلامه منك يرجى اخبار المسؤول اذا كان به اي مشكلة رجاء...",
                         reply_markup=types.ReplyKeyboardRemove())

        try:
            list2 = ans_func()
            bot.send_message(message.chat.id,
                             str(list2[:9]).replace("[", "").replace("]", "").replace("'", ' * ').replace("\\n",
                                                                                                          "\n").replace(
                                 ",", "\n\n") + "\n\n" + str(list2[11:]).replace("[", "").replace("]", "").replace(",",
                                                                                                                   "\n\n"))
        except:

            bot.send_message(1066196464, "لقد حدث ايرور.....")
            bot.send_message(1066196464, "لقد حدث ايرور.....")

        ans_dict.clear()
    if (message.text in ['اعادة ادخال السؤال السادس'] or str(message.text).replace(" ", "").replace(".",
                                                                                                    "") in chooes_cansle):
        message.text = 'متابعة الى السؤال السادس'
        ans_dict.pop("استجابة الطالب و الأهل وهل لديك اي مشاكل")
        question_6(message)


############################################################################################################################################
########################################################## Form message handler ############################################################
############################################################################################################################################
@bot.message_handler(commands=['direct_question5'])
def commands_buttons2(message):
    if message.text == "/direct_question5":
        bot.send_message(message.chat.id, "لتسليم الظرف بشكل مباشر\n\nادخل المعرف الخاص بك رجاء :",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, user)

    elif message.text == "/cancel":
        ans1.clear()
        bot.send_message(message.chat.id, "تم الالغاء...")


def user(message):
    if message.text in ["/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/cancel"]:
        commands_buttons2(message)

    else:
        users_info = data_msg
        user_id = str(message.text).replace(" ", "")

        for i in user_id:
            if i in arbic_num:
                user_id = user_id.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤',
                                                                                                                  '4').replace(
                    '٥', '5')
                user_id = user_id.replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')
                break

        if user_id in users_info.keys():
            ans_dict['المعرف (رقم الهاتف)'] = [user_id]
            text0 = "للمتابعة :"
            text1 = "/continue"
            text2 = "للالغاء :"
            text3 = "/cancel"
            bot.send_message(message.chat.id, users_info[str(user_id)] + f"\n\n{text0}\n{text1}\n{text2}\n{text3}")
            bot.register_next_step_handler(message, user2)
        else:
            bot.send_message(message.chat.id, "ارجو التأكد من المعرف الخاص بك اعد الإدخال :",
                             reply_markup=types.ReplyKeyboardRemove())

            bot.register_next_step_handler(message, user)


def user2(message):
    if message.text in ["/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/cancel"]:
        commands_buttons2(message)


    else:
        bot.send_message(message.chat.id, "ضع الظرف هنا رجاء مع وقت الحصة:")
        bot.register_next_step_handler(message, user3)


def user3(message):
    if message.text in ["/help", "/fill_the_form"]:
        commands_buttons(message)
    elif message.text in ["/cancel"]:
        commands_buttons2(message)

    else:
        ans1["ضع الظرف هنا"] = str(message.text)
        func(message, ['متابعة الى التسليم', 'اعادة اللإدخال'], user4)


def user4(message):
    if message.text in ["/help", "/fill_the_form"]:
        commands_buttons(message)

    elif message.text in ["/cancel"]:
        commands_buttons2(message)

    else:

        if (message.text == "اعادة اللإدخال" or str(message.text).replace(" ", "").replace(".", "") in chooes_cansle):
            ans1.clear()
            message.text = ""
            user2(message)

        elif (message.text == "متابعة الى التسليم" or str(message.text).replace(" ", "").replace(".",
                                                                                                 "") in chooes_confirm):
            value = []
            student = data_msg[ans_dict['المعرف (رقم الهاتف)'][0]].replace("اسم المتطوع", "").replace("اسم الطالب",
                                                                                                      "").replace(
                "رقم الهاتف (المعررف)", "")
            student = student.replace(":", "").replace(ans_dict['المعرف (رقم الهاتف)'][0], "").split("\n")
            student = student[::-1]

            for i in student[1:]:
                value.append(i[2:])

            value = value[::-1]
            value.append(ans_dict['المعرف (رقم الهاتف)'][0])
            value.append("--", )
            value.append("--")
            value.append("--")
            value.append("--")
            value.append(ans1["ضع الظرف هنا"])
            value.append("--")
            now = datetime.now(timezone('Asia/Amman'))
            value.append("")
            value.append(f"{now.date()}\n{now.time()}\n{str(now.strftime('%A'))}\n")
            wks.append_row(value)
            bot.send_message(message.chat.id, "شكراً كثير تم الإستلام بنجاح...",
                             reply_markup=types.ReplyKeyboardRemove())
            ans1.clear()



############################################################################################################################################
################################################### any message else #######################################################################
############################################################################################################################################
@bot.message_handler(func=lambda message: True)
def random_message(message):
    if message.chat.id not in chat_id_users:
        chat_id_users.append(message.chat.id)
    if message.text not in ["/cancel", "/help", "/fill_the_form",
                            "/continue", "/submission", "/cancel_submission246", "/reminder", "/ai_bot", "/help",
                            "/start", "/direct_question5", "/nw246", "/pin"]:
        bot.send_message(message.chat.id, "‼️انت لم تختار اي أمر..للمساعدة ( /help )")


############################################################################################################################################
################################################### to append data to excel file ###########################################################
############################################################################################################################################


def ans_func():
    value = []

    for i in ans_dict.values():
        value.append(i[0])

    now = datetime.now(timezone('Asia/Amman'))
    value.append(" ")
    value.append(f"{now.date()}\n{now.time()}\n{str(now.strftime('%A'))}\n")

    wks.append_row(value)
    wks.append_row(["24620020mrasdad"])
    cell = wks.find("24620020mrasdad")
    row_num = cell.row

    a = int(row_num)

    wks.delete_rows(a, a)

    value.append(f"اسم الصفحة في ملف اكسل : الاسبوع رقم({str(int(wks.index) + 1)})")
    value.append(f"رقم الصف هوه : {row_num - 1}")
    return value


######################################### generate buttons ############################################
def generate_buttons(command, markup):
    for button in command:
        markup.add(types.KeyboardButton(button))
    return markup


######################################### follow-up function ###########################################
def func(message, text, fun):
    get_button = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    markup = generate_buttons(text, get_button)
    message = bot.reply_to(message, "هل تريد المتابعة..؟", reply_markup=markup)
    bot.register_next_step_handler(message, fun)


print("The bot is working.....")
keep_alive()
bot.infinity_polling()

wks2.delete_rows(2, 2)
wks2.append_row([(time.time() - start_time) + t, wks.title, str(chat_id_users)])