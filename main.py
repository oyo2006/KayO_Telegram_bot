from botcommands import *
from reply import *
from rock import *
from telebot import util
from wallpapers import *
@bot.message_handler(content_types=util.content_type_service)
def delall(m: types.Message):
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        bot.send_message(m.chat.id, "لا أستطيع حذف الرسالة")

@bot.message_handler(commands=['start','ban','pic','unban','info','intel', 'up', 'admin','sp','down', 'photo', 'admins', 'mcount', 'pin', 'file', 'face', 'state','image','wallpaper'])
def myc(m):
    my_comd(m)

@bot.chat_member_handler()
def chat_m(m: types.ChatMemberUpdated):
    old = m.old_chat_member
    new = m.new_chat_member
    first_name = m.from_user.first_name
    name = new.user.first_name
    if new.status == "member":
        bot.send_message(m.chat.id, f"مرحباً {name}")
        if name == first_name:
            bot.send_message(m.chat.id, f"{name} انضم إلينا عن طريق رابط دعوة")
        else:
            bot.send_message(m.chat.id, f"{first_name} هو من أضاف {name} إلى المجموعة")
    if new.status == "administrator":
        bot.send_message(m.chat.id, "استمتع بمنصبك الجديد (:", reply_to_message_id=m.reply_to_message.from_user.id)
    else:
        bot.send_message(m.chat.id, f"وداعاً {name}")


@bot.message_handler(func=lambda m: True)
def reply_message(m):
    rm(m)


@bot.callback_query_handler(func=lambda call: call.data == "4K" or "2K" or "FHD")
def wallpaper_callback(call_back):
    call_result2(call_back)

@bot.callback_query_handler(func=lambda call :True)
def calling(call):
    call_result1(call)



telebot.apihelper.RETRY_ON_ERROR = True
bot.infinity_polling()