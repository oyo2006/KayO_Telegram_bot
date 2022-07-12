from info import *
from time import sleep
import random

choices = ["حجر","ورقة","مقص"]
player = None
#----------------------------------
#----------------------------------
list_btn1=types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text = "حجر", callback_data = "حجر")
btn2 = types.InlineKeyboardButton(text = "ورقة", callback_data = "ورقة")
btn3 = types.InlineKeyboardButton(text = "مقص", callback_data = "مقص")
list_btn1.add(btn1)
list_btn1.add(btn2)
list_btn1.add(btn3)
def call_result1(call):
    computer = random.choice(choices)
    print("computer: " + computer)
    player = call.data
    print(player)
    user = call.from_user.first_name
    computer_choice = call.message.from_user.first_name
    if player != None:
        bot.delete_message(call.message.chat.id, call.message.id)
        if player == computer:
            bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
            sleep(.5)
            bot.send_message(call.message.chat.id, "تعادل")
            
        elif player == "حجر":
            
            if computer == "ورقة":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {computer_choice}")
                
            if computer == "مقص":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {user}")
                
        elif player == "مقص":
            if computer == "حجر":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {computer_choice}")
                
            if computer == "ورقة":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {user}")
                
        elif player == "ورقة":
            if computer == "مقص":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {computer_choice}")
                
            if computer == "حجر":
                bot.send_message(call.message.chat.id, f"{user} اختار {player}\n{computer_choice} اختار {computer}")
                sleep(.5)
                bot.send_message(call.message.chat.id, f"الفائز: {user}")     
        
# def rock(m):
#     while True:
#         bot.send_message(m.chat.id, "أنا اشتغلت")
#         choices = ["rock","paper","scissors"]

#         computer = random.choice(choices)
#         player = None

#         while player not in choices:
#             player = input("rock, paper, or scissors?: ").lower()

#         if player == computer:
#             bot.send_message(m.chat.id, "تعادل")

        # elif player == "rock":
        #     if computer == "paper":
        #         bot.send_message(m.chat.id, "لقد خسرت")
        #     if computer == "scissors":
        #         bot.send_message(m.chat.id, "لقد فزت")

        # elif player == "scissors":
        #     if computer == "rock":
        #         bot.send_message(m.chat.id, "لقد خسرت")
        #     if computer == "paper":
        #         bot.send_message(m.chat.id, "لقد فزت")

        # elif player == "paper":
        #     if computer == "scissors":
        #         bot.send_message(m.chat.id, "لقد خسرت")
        #     if computer == "rock":
        #         bot.send_message(m.chat.id, "لقد فزت")

#         play_again = input("Play again? (yes/no): ").lower()

#         if play_again != "yes":
#             break