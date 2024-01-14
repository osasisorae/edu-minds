from decouple import config
from models import User
from tools import Brain
import telebot
import pandas as pd
import os

import mindsdb_sdk
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

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
        chat_id = message.chat.id
        first_name = message.text
        user = User(first_name)
        user_data[chat_id] = user
        msg = bot.reply_to(message, 'What is your last name?')
        bot.register_next_step_handler(msg, process_lastname_step)
        
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')
        
def process_lastname_step(message):
    try:
        chat_id = message.chat.id
        user = user_data[chat_id]
        user.last_name = message.text
        msg = bot.reply_to(message, 'What are your goals?')
        bot.register_next_step_handler(msg, process_goals_step)
        
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')
        
def process_goals_step(message):
    try:
        chat_id = message.chat.id
        user = user_data[chat_id]
        user.goals = message.text
        msg = bot.reply_to(message, 'What are your learning styles?')
        bot.register_next_step_handler(msg, process_learning_styles_step)
        
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')

def process_learning_styles_step(message):
    try:
        chat_id = message.chat.id
        user = user_data[chat_id]
        user.learning_styles = message.text
        msg = bot.reply_to(message, 'What are your subjects of interest?')
        bot.register_next_step_handler(msg, process_subjects_of_interest_step)
        
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')
        
def process_subjects_of_interest_step(message):
    try:
        chat_id = message.chat.id
        user = user_data[chat_id]
        user.subjects_of_interest = message.text
        bot.reply_to(message, 'Thanks. Your profile has been saved.')
        print(user_data)
        # # Save data on MindDB 

        # Create dataframe from user data
        df = pd.DataFrame([vars(user) for user in user_data.values()])
        
        files_db = server.get_database('files')
        files_db.create_table(f'profile_{str(chat_id)}', df)
        
        # Save to CSV file
        df.to_csv(f'user_data_{chat_id}.csv', index=False)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')
        
@bot.message_handler(commands=['learning_path'])
def send_learning_path(message):
    try:
        chat_id = message.chat.id

        # Load data from minds DB
        rs = server.get_database('files').query(f'SELECT * FROM profile_{chat_id}')
        df = pd.DataFrame(rs.fetch())

        prompt = f"With all the data in this database, can you create a learning path for this user. The learning path should fit to the users goals which are {df['goals'].iloc[0]} and information on the pandas dataframe. It should have links to resources and a max of 5 resources. The user's subjects of interest are {df['subjects_of_interest'].iloc[0]}."
        print(prompt)
        learning_path = Brain().create_learning_path(prompt)
        
        # Send the learning path to the user
        bot.reply_to(message, learning_path)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops')

bot.infinity_polling()