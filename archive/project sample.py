import telebot
from telebot import types
bot = telebot.TeleBot('1723075813:AAFVXryYTG_wtFUueGSY40vv-t_tGMLwIBA')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'bul bot binomal probability esepteu ushin koldanyladi, {message.from_user.first_name}. zhumys isteudi bastau yshin, salem dep zhaziniz ')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global trials
    trials = 0
    global succestrials
    succestrials = 0
    global probofsuccess
    probofsuccess = 0
    
    def get_trials(message):
        global trials
        try:
            trials = int(message.text) 
        except Exception:
            bot.send_message(message.from_user.id, 'Sandardy engiziniz')
        bot.send_message(message.from_user.id, 'satti zhasalyngan mumkindikterdi engiziniz')
        bot.register_next_step_handler(message, get_successtrials)
    def get_successtrials(message):
        global succestrials
        try:
            succestrials = int(message.text) 
        except Exception:
            bot.send_message(message.from_user.id, 'Sandardy engiziniz')
        bot.send_message(message.from_user.id,'Probability of success?')
        bot.register_next_step_handler(message, get_success)

    def get_success(message):
        failure = 0
        failurepower = 0
        global probofsuccess
        try:
            probofsuccess = float(message.text) 
        except Exception:
            bot.send_message(message.from_user.id, 'Sandardy engiziniz')
            failure = 1 - probofsuccess
            failurepower = trials - succestrials
        factorial1 = 1
        factorial2 = 1
        for i in range(2, trials+1):
            factorial1 *= i
            print(factorial1)
        for i in range(2, succestrials+1):
            factorial2 *= i
        combine = factorial1/factorial2
        gensuccess = probofsuccess**succestrials
        genfailure = failure**failurepower
        result= combine * gensuccess * genfailure
        result = str(result)
        bot.send_message(message.from_user.id, "Zhauabi"+ result)
    if message.text.lower() == "salem":
        bot.send_message(message.from_user.id, "Salem,")
        bot.send_message(message.from_user.id, "Zhasalyngan barlyk mumkindikterdi engiziniz")
        bot.register_next_step_handler(message, get_trials)
    else:
        bot.send_message(message.from_user.id, "Men sizdi tusinbei turmyn. /help dep zahzynyz")
    
    
bot.polling(none_stop=True, interval=0)
