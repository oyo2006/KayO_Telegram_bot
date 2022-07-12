from btns import *
from datetime import *
from insert_reply import *
from rock import *
from read_reply import *
from wallpapers import *
def rm(m):
    if m.text in ('مرحبا', 'مرحباً', 'اهلا', 'هلا', 'شلون', 'هاي'):
       bot.reply_to(m, "مرحباً!")
    if m.text == ('السلام عليكم'):
       bot.reply_to(m, "وعليكم السلام ورحمة الله وبركاته")
    if m.text in ('time' , 'time?' ,'كم الساعة؟', 'الساعة كم؟', 'الساعة كم', 'كم الساعة', 'الوقت', 'الساعة', 'كم الوقت'):
        now = datetime.now()
        dt_hours = now.strftime("%H")
        dt_minutes = now.strftime("%M")
        # this is added because of the local time heroku uses
        hours = int(dt_hours)
        Makkah_hours = hours + 3
        Libya_hours  = hours + 2
        Jerusalem_hours = hours + 3
        Makkah_time = f"{Makkah_hours}:{dt_minutes}"
        Jerusalem_time = f"{Jerusalem_hours}:{dt_minutes}"
        Libya_time = f"{Libya_hours}:{dt_minutes}"
        bot.send_message(m.chat.id, str(Makkah_time) + " بتوقيت مكة")
        bot.send_message(m.chat.id, str(Jerusalem_time) + " بتوقيت القدس، حررها الله")
        bot.send_message(m.chat.id, str(Libya_time) + " بتوقيت طرابلس الغرب")
    if m.text == "طرد" or m.text == "حظر":
        try:
            Ban = bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
            if Ban:
                bot.send_message(m.chat.id,"احترم نفسك" + " @"+ m.reply_to_message.from_user.username)
        except AttributeError:
            bot.send_message(m.chat.id,"أعطني رسالةً لأحظر صاحبها!")
        except:
            bot.send_message(m.chat.id,"لا أستطيع حظره لأن صلاحياته أعلى مني")
    # if m.text in ('تحبني', 'تحبني؟'):
    #     bot.reply_to(m, "تحبه؟" ,reply_markup=list_btn)
    if m.text == "معلوماتي":
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
                    bot.send_message(m.chat.id, "ليست لديك صورة مستخدم")
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
                    bot.send_message(m.chat.id, "ليست لديك صورة مستخدم")
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
                    bot.send_message(m.chat.id, "ليست لديك صورة مستخدم")
            if info.bio == None and info.username == None:
                upp = bot.get_user_profile_photos(m.from_user.id)
                photos = upp.photos
                try:
                    photo = photos[0][0].file_id
                    bot.send_photo(m.chat.id, photo)
                except:
                    bot.send_message(m.chat.id, "ليست لديك المعلومات الكافية لأستطيع العمل")
    if m.text == "معلوماته":
        try:
            info = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).user
            is_Bot = info.is_bot
            id = info.id
            first_name = info.first_name
            bio = bot.get_chat(m.reply_to_message.from_user.id).bio
            last_name = info.last_name
            user_name = info.username
            if last_name != None and user_name != None and bio != None and is_Bot == False:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n التعريف: {bio}\n_____")
            if last_name != None and user_name != None and bio != None and is_Bot == True:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n التعريف: {bio}\nوهو بوت\n_____")
            if last_name != None and user_name != None and bio == None and is_Bot == False:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n لا يوجد تعريف\n_____")
            if last_name != None and user_name != None and bio == None and is_Bot == True:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n اسم المستخدم: @{user_name}\n لا يوجد تعريف\nوهو بوت\n_____")
            if last_name != None and user_name == None and bio != None and is_Bot == False:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n التعريف: {bio}\n_____")
            if last_name != None and user_name == None and bio != None and is_Bot == True:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n التعريف: {bio}\nوهو بوت\n_____")
            if last_name != None and user_name == None and bio == None and is_Bot == False:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n لا يوجد تعريف\n_____")
            if last_name != None and user_name == None and bio == None and is_Bot == True:
                bot.send_message(m.chat.id,f"_____\nالمعرف: {id}\n الاسم الاول: {first_name}\n الاسم الاخير: {last_name}\n لا يوجد اسم مستخدم\n لا يوجد تعريف\nوهو بوت\n_____")
            if last_name == None and user_name != None and bio != None and is_Bot == False:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n التعريف: {bio}\n_____")
            if last_name == None and user_name != None and bio != None and is_Bot == True:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n التعريف: {bio}\nوهو بوت\n_____")
            if last_name == None and user_name != None and bio == None and is_Bot == False:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n لا  يوجد تعريف\n_____")
            if last_name == None and user_name != None and bio == None and is_Bot == True:
               bot.send_message(m.chat.id, f"_____\n الاسم الأول: {first_name}\n المعرف: {id}\n لا يوجد اسم أخير\n اسم المستخدم: @{user_name}\n لا  يوجد تعريف\nوهو بوت\n_____")
            if last_name == None and user_name == None and bio != None and is_Bot == False:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n التعريف: {bio}\n_____")
            if last_name == None and user_name == None and bio != None and is_Bot == True:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n التعريف: {bio}\nوهو بوت\n_____")
            if last_name == None and user_name == None and bio == None and is_Bot == False:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n لا يوجد تعريف\n_____")
            if last_name == None and user_name == None and bio == None and is_Bot == True:
                bot.send_message(m.chat.id, f"_____\nالاسم الأول: {first_name}\n المعرف: {id}\n لا بوجد اسم أخير\n لا يوجد اسم مستخدم\n لا يوجد تعريف\nوهو بوت\n_____")
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأعرض معلومات صاحبها")
    if m.text == "من أنت":
        bot.send_message(m.chat.id, f"_____\nأنا بوت إدارة مجموعات يتحدث باللغة العربية\nتمت برمجتي بواسطة: @A2HX21\n_____")
    if m.text == "حكم":
        with open("hekam.txt","r",encoding="utf-8") as hk:
            for i in hk.readlines():
                bot.send_message(m.chat.id, i)
    if m.text == "رفع مدير":
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
    if m.text == "رفع مشرف":
        try:
            if m.reply_to_message.from_user.id == 5216980167:
                bot.send_message(m.chat.id, "لا أستطيع تعديل صلاحيات نفسي")
            else:
                status1 = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id).status
                if status1 == 'member':
                    bot.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id, can_invite_users=True,can_manage_chat=True,can_promote_members=True,can_restrict_members=True)
                    bot.send_message(m.chat.id, "تم رفعهُ مشرفاً بنجاح")
                status = bot.get_chat_member(m.chat.id,m.reply_to_message.from_user.id)
                if not status.is_anonymous and status.can_manage_chat and status.can_delete_messages and status.can_restrict_members and status.can_promote_members and status.can_manage_voice_chats and status.can_invite_users and status.can_pin_messages:
                    bot.send_message(m.chat.id, "هذا الشخص مدير ولا يمكن رفع المدير الى مشرف\nهههه")               
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة لأرفع صاحبها مشرفاً")
    if m.text == "كيفية الترقية":
        bot.send_message(m.chat.id, "'رفع مشرف' يرفع لصلاحيات المشرف")
        bot.send_message(m.chat.id, "'رفع مدير' يرفع لصلاحيات المدير")
    if m.text == "رتبتي":
        try:
            status1 = bot.get_chat_member(m.chat.id, m.from_user.id).status
            if status1 == "member":
                bot.send_message(m.chat.id, "أنت عضو")
            status = bot.get_chat_member(m.chat.id, m.from_user.id)
            if not status.is_anonymous and status.can_manage_chat and status.can_delete_messages and status.can_restrict_members and status.can_promote_members and status.can_manage_voice_chats and status.can_invite_users and status.can_pin_messages:
                bot.send_message(m.chat.id, "أنت مدير")
            if status.can_invite_users and status.can_manage_chat and status.can_promote_members and status.can_restrict_members and not status.can_delete_messages:
                bot.send_message(m.chat.id, "أنت مشرف")
        except AttributeError:
            bot.send_message(m.chat.id, "أعطني رسالة")
    if m.text == "تثبيت":
        pin = bot.pin_chat_message(m.chat.id, m.reply_to_message.from_user.id)
        if pin:
            bot.send_message(m.chat.id, "تم تثبيت الرسالة")
    if m.text == "Kay/o":
        bot.send_message(m.chat.id, "نعم؟")
    if m.text == "فوندا":
        bot.send_message(m.chat.id, "لماذا تكلمون بوت آخر وأنا هنا؟")
        bot.send_message(m.chat.id, "ألست كافياً؟")
    if m.text == "الغي الصورة":
        bot.delete_chat_photo(m.chat.id)
    if m.text == "شخشير":
        bot.send_message(m.chat.id, "ليس لدي جورب لأعطيه لك")
    if m.text == "تفاعل":
        count = bot.get_chat_member_count(m.chat.id)
        bot.send_message(m.chat.id, f"عندك {count} عضو وليس هناك تفاعل؟")
        bot.send_message(m.chat.id, "مجموعة كسلاء")
    if m.text == "حجر":
        bot.send_message(m.chat.id, "حجر،ورقة،مقص", reply_markup=list_btn1)
    if m.text == "صور حائطية":
        bot.send_message(m.chat.id,"اختر حجماً للصورة:", reply_markup=wallpapers)