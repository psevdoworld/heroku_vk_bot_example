import telebot
bot = telebot.TeleBot("5932201689:AAFjlqCGOu_pUL8d0eiIwrhumjIP6QcWfdU",
                     parse_mode=None) 

bot.send_message(65353297,
                 'i am alive')
def is_privet(message):
    return 'привет' in message.text

@bot.message_handler(commands=['whoami',])
def say_privet(message):
	bot.reply_to(message,
                     (str(message.chat.id)
                      + '\n' +
                      message.chat.username
                      )
                     )
@bot.message_handler(func=is_privet)
def say_privet(message):
	bot.reply_to(message,
                     "Здравствуй")

def yes(message):
    return True
@bot.message_handler(func=yes)
def echo_all(message):        
        bot.reply_to(message, message.text)
bot.infinity_polling()
