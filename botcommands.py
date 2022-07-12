from time import sleep
from info import *
import requests
from wallpapers import wallpapers
def my_comd(m):
    if m.text == "/ban":
        try:
            status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
            status1 = bot.get_chat_member(m.chat.id,m.from_user.id).status
            if status == 'administrator' and m.reply_to_message.from_user.id != 5216980167 or status == 'creator' and m.reply_to_message.from_user.id != 5216980167:
                bot.send_message(m.chat.id, "لا أستطيع حظره لأن صلاحياته أعلى مني")
            elif m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لِمَ العبث؟")
            elif status1 == "member":
                bot.send_message(m.chat.id, "صلاحياتك لا تسمح لك بحظر أحد")
            else:
                Ban = bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
                if Ban:
                    bot.send_message(m.chat.id,"احترم نفسك" + " @"+ m.reply_to_message.from_user.username)
        except AttributeError:
            status1 = bot.get_chat_member(m.chat.id,m.from_user.id).status
            if status1 == "member":
                bot.send_message(m.chat.id, "___\nأنت عضو ولا تستطيع حظر أحد\nأضف إلى ذلك أنك لم تعطني رسالة لأتعامل معها\nهههه\n___")
            else:
                bot.send_message(m.chat.id,"أعطني رسالةً لأحظر صاحبها!")

    if m.text == "/start":
        bot.reply_to(m, "مرحباً")
    if m.text == "/pic":
        try:
            upp = bot.get_user_profile_photos(m.from_user.id).photos
            photo = upp[0][0].file_id
            bot.send_photo(m.chat.id, photo)
        except:
            bot.send_message(m.chat.id,"ليس لديك صورةٌ أصلاً")
        
    if m.text == "/unban":
        try:
            status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
            status1 = bot.get_chat_member(m.chat.id, m.from_user.id).status
            if m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لِمَ العبث؟")
            elif status1 == "member":
                bot.send_message(m.chat.id, "أنت عضو وصلاحياتك لا تسمح لك بهذا")
            else:
                if status == "kicked":
                    unban = bot.unban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
                    if unban:
                        bot.send_message(m.chat.id,"لا تشاغب مرةً أخرى" + " @"+ m.reply_to_message.from_user.username)
                else:
                    bot.send_message(m.chat.id, "إنه ليس محظوراً أصلاً")
        except AttributeError:
            status1 = bot.get_chat_member(m.chat.id, m.from_user.id).status
            if status1 == "member":
                bot.send_message(m.chat.id, "___\nأنت عضو و صلاحياتك لا تسمح لك باستعمال هذا الأمر\nأضف إلى ذلك أنك لم تعطني رسالة لأتعامل معها\nهههه\n___")
            else:
                bot.send_message(m.chat.id, "أعطني رسالة لألغي حظر صاحبها")
    if m.text == "/info":
        try:
            info = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).user
            id = info.id
            first_name = info.first_name
            bio = bot.get_chat(m.reply_to_message.from_user.id).bio
            last_name = info.last_name
            user_name = info.username
            if last_name != None and user_name != None and bio != None:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n التعريف: {bio}\n_____")
            if last_name != None and user_name != None and bio == None:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n لا يوجد تعريف\n_____")
            if last_name != None and user_name == None and bio != None:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n التعريف: {bio}\n_____")
            if last_name != None and user_name == None and bio == None:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n لا يوجد تعريف\n_____")
            if last_name == None and user_name != None and bio != None:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n التعريف: {bio}\n_____")
            if last_name == None and user_name != None and bio == None:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n لا  يوجد تعريف\n_____")
            if last_name == None and user_name == None and bio != None:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n التعريف: {bio}\n_____")
            if last_name == None and user_name == None and bio == None:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n لا يوجد تعريف")
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأعرض معلومات صاحبها")
    if m.text == "/intel":
            info = bot.get_chat(m.from_user.id)
            if info.bio != None and info.username != None:
                try:
                    bio = "التعريف: "+ info.bio
                    user = "اسم المستخدم: @"+ info.username
                    full_info =  f"_____\n{user}\n{bio}\n_____"
                    upp = bot.get_user_profile_photos(m.from_user.id)
                    photos = upp.photos
                    photo = photos[0][0].file_id
                    bot.send_photo(m.chat.id, photo, caption=full_info)
                except IndexError:
                    bot.send_message(m.chat.id, "ليس لديك صورة مستخدم")
                    bio = "التعريف: "+ info.bio
                    user = "اسم المستخدم: @"+ info.username
                    full_info =  f"{user}\n{bio}"
                    bot.reply_to(m, full_info)
            if info.bio != None and info.username == None:
                try:
                    bio = "التعريف: "+ info.bio
                    user = "ليس لديك اسم مستخدم"
                    full_info =  f"{user}\n{bio}"
                    bot.reply_to(m, full_info)
                    upp = bot.get_user_profile_photos(m.from_user.id)
                    photos = upp.photos
                    photo = photos[0][0].file_id
                    bot.send_photo(m.chat.id, photo)
                except IndexError:
                    bot.send_message(m.chat.id, "ليس لديك صورة مستخدم")
                    bio = "التعريف: "+ info.bio
                    user = "ليس لديك اسم مستخدم"
                    full_info =  f"{user}\n{bio}"
            if info.bio == None and info.username != None:
                bio = "ليس لديك تعريف"
                user = "اسم المستخدم: @"+ info.username
                full_info =  f"{user}\n{bio}\nصورة المستخدم:"
                bot.reply_to(m, full_info)
                upp = bot.get_user_profile_photos(m.from_user.id)
                photos = upp.photos
                try:
                    photo = photos[0][0].file_id
                    bot.send_photo(m.chat.id, photo)
                except IndexError:
                    bot.send_message(m.chat.id, "ليس لديك صورة مستخدم")
            if info.bio == None and info.username == None:
                upp = bot.get_user_profile_photos(m.from_user.id)
                photos = upp.photos
                try:
                    photo = photos[0][0].file_id
                    bot.send_photo(m.chat.id, photo)
                except:
                    bot.send_message(m.chat.id, "ليست لديك المعلومات الكافية لأستطيع العمل")
    if m.text == "/up":
        try:
            status2 = bot.get_chat_member(m.chat.id, m.from_user.id).status
            if m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لا أستطيع تعديل صلاحيات نفسي")
            if status2 == "member":
                bot.send_message(m.chat.id, "أنت عضو ولا تستطيع ترقية أحد (:")
            else:
                status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id)
                status1 = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
                if status.can_invite_users and status.can_manage_chat and status.can_promote_members and status.can_restrict_members and not status.can_delete_messages or status1 == 'member':
                    bot.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, is_anonymous=False, can_manage_chat=True, can_delete_messages=True, can_restrict_members=True, can_promote_members=True, can_manage_voice_chats=True, can_invite_users=True, can_pin_messages=True)
                    bot.send_message(m.chat.id, "رُفع مديراً بنجاح")
                elif status1 == "kicked":
                    bot.send_message(m.chat.id, "هذا الشخص محظور")
                else:
                    bot.send_message(m.chat.id, "هذا الشخص مدير أصلاً")
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأرفع صاحبها مديراً")
    if m.text == "/sp":
        try:
            if m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لا أستطيع تعديل صلاحيات نفسي")
            else:
                status1 = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
                if status1 == 'member':
                    bot.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, can_invite_users=True,can_manage_chat=True,can_promote_members=True,can_restrict_members=True)
                    bot.send_message(m.chat.id, "تم رفعهُ مشرفاً بنجاح")
                if not status.is_anonymous and status.can_manage_chat and status.can_delete_messages and status.can_restrict_members and status.can_promote_members and status.can_manage_voice_chats and status.can_invite_users and status.can_pin_messages:
                    bot.send_message(m.chat.id, "هذا الشخص مدير ولا يمكن رفع المدير الى مشرف\nهههه")               
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأرفع صاحبها مشرفاً")
    if m.text == "/admin":
        admin = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        bot.send_message(m.chat.id, admin)
    if m.text == "/down":
        try:
            if m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لا أستطيع تعديل صلاحيات نفسي")
            else:
                status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id)
                status1 = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
                if not status.is_anonymous and status.can_manage_chat and status.can_delete_messages and status.can_restrict_members and status.can_promote_members and status.can_manage_voice_chats and status.can_invite_users and status.can_pin_messages:
                    bot.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, can_invite_users=True,can_manage_chat=True,can_promote_members=True,can_restrict_members=True)
                    bot.send_message(m.chat.id, "تم خفض رتبته من مدير إلى مشرف")
                if status.can_invite_users and status.can_manage_chat and status.can_promote_members and status.can_restrict_members and not status.can_delete_messages:
                    bot.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, can_invite_users=False,can_manage_chat=False,can_promote_members=False,can_restrict_members=False)
                    bot.send_message(m.chat.id, "تم خفض رتبته من مشرف إلى عضو")
                if status1 == "member":
                    bot.send_message(m.chat.id, "إنه ليس مديراً أو مشرفاً أصلاً")
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأخفض رتبة صاحبها")
    if m.text == "/photo":
            bot.set_chat_photo(m.chat.id, "https://picsum.photos/1000/1000")
    if m.text == "/admins":
        admin = bot.get_chat_administrators(m.chat.id)
        bot.send_message(m.chat.id, admin)
    if m.text == "/mcount":
        mcount = bot.get_chat_member_count(m.chat.id)
        bot.send_message(m.chat.id, mcount)
    if m.text == "/pin":
        try:
            status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
            if status == "administrator":
                pin = bot.pin_chat_message(m.chat.id, m.reply_to_message.message_id)
                if pin:
                    bot.send_message(m.chat.id, "تم تثبيت الرسالة")
            if status == "member":
                bot.send_message(m.chat.id, "أنت عضو ولا تستطيع تثبيت الرسائل")
        except AttributeError:
            try:
                status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
                if status == "member":
                    bot.send_message(m.chat.id, "لن أثبت الرسالة لسببين:")
                    bot.send_message(m.chat.id, "1- أنت لم تعطني رسالة")
                    bot.send_message(m.chat.id, "2- أنت عضو ولا تستطيع تثبيت الرسائل أصلاً")
            except AttributeError:
                bot.send_message(m.chat.id, "___\nأعطني رسالة لأثبتها يا صديقي\n بدون الرسالة لا أستطيع العمل\n___")
    if m.text == "/image":
        pic = requests.get("https://picsum.photos/500").content
        bot.send_photo(m.chat.id, pic)
    if m.text == "/wallpaper":
        bot.send_message(m.chat.id,"Choose an image size: ", reply_markup=wallpapers)
    if m.text == "/face":
        pic = requests.get("http://thispersondoesnotexist.com/image").content
        bot.send_photo(m.chat.id, pic)
    #states are planned to be PUT somewhere around here(BRUH)
    