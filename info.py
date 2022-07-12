import telebot
import time
from telebot import types
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
tok = '5216980167:AAGJ7y5qXW8VxVej9s0X7kuHty2qtJbGAN4'
state_storage = StateMemoryStorage()
bot = telebot.TeleBot(tok, state_storage=state_storage)