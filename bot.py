from decouple import config
from models import User
import telebot

BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am an Educationa Assistance Bot. I will hold a conversation with to gather your learning profile. 
What is your first name?
""")
    bot.register_next_step_handler(msg, process_firstname_step)
    
def process_firstname_step(message):
    try:
        chat_id = messgae.chat.id
        first_name = message.text
        user = User(first_name)
        user_data[chat_id] = user
        msg = bot.reply_to(message, 'What is your last name?')
        bot.reply_to_next_step_handler(msg, process_lastname_step)
        
    except Exception as e:
        bot.reply_to(message, 'oooops')
        
def process_lastname_step(message):
    try:
        chat_id = message.chat.id
        user.last_name = message.text
        msg = bot.reply_to(message, 'What are your goals?')
        bot.register_next_step_handler(msg, process_goals_step)
        
    except Exception as e:
        bot.reply_to(message, 'oooops')
        
        
bot.infinite_polling()