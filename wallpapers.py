from time import sleep
from info import *
import requests
wallpapers = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text = "4K", callback_data = "4K")
btn2 = types.InlineKeyboardButton(text = "2K", callback_data = "2K")
btn3 = types.InlineKeyboardButton(text = "FHD", callback_data = "FHD")
btn4 = types.InlineKeyboardButton(text = "HD", callback_data = "HD")
wallpapers.add(btn1, btn2, btn3, btn4)
def call_result2(call_back):
    wallpaper = call_back.data
    if wallpaper == "4K":
        pic = requests.get("https://picsum.photos/3840/2160").content
        bot.send_photo(call_back.message.chat.id, pic)
        bot.delete_message(call_back.message.chat.id, call_back.message.message_id)
    elif wallpaper == "2K":
        pic = requests.get("https://picsum.photos/2560/1440").content
        bot.send_photo(call_back.message.chat.id, pic)
        bot.delete_message(call_back.message.chat.id, call_back.message.message_id)
    elif wallpaper == "FHD":
        pic = requests.get("https://picsum.photos/1920/1080").content
        bot.send_photo(call_back.message.chat.id, pic)
        bot.delete_message(call_back.message.chat.id, call_back.message.message_id)
#######################################################
@bot.callback_query_handler(func=lambda call: call.data == "HD")
def HD(call_back):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton("768P", callback_data="768P")
    itembtn2 = types.InlineKeyboardButton("720P", callback_data="720P")
    mkup.add(itembtn1, itembtn2)
    text = "أحجام الHD"
    bot.edit_message_text( text, call_back.message.chat.id, call_back.message.message_id, reply_markup=mkup)
#######################################################
@bot.callback_query_handler(func=lambda call: call.data == "768P")
def HD1(call):
    pic = requests.get("https://picsum.photos/1366/768").content
    bot.send_photo(call.message.chat.id, pic)
    bot.delete_message(call.message.chat.id, call.message.message_id)
#######################################################
@bot.callback_query_handler(func=lambda call: call.data == "720P")
def HD2(call):
    pic = requests.get("https://picsum.photos/1280/720").content
    bot.send_photo(call.message.chat.id, pic)
    bot.delete_message(call.message.chat.id, call.message.message_id)
