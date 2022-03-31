import telebot;
from telebot import types
bot = telebot.TeleBot('1733893572:AAEdtX3PIvl5CD60LUWRtddYNNDDeik643A');
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Hello{message.from_user.first_name}! Welcome to bot which can calculate the circular permutation')
    bot.reply_to(message, f'To begin type \'help\'command')
@bot.message_handler(commands=['help'])
def send_instr(message):
    bot.reply_to(message, f' If you need to solve problem choose which type of problem i must to solve')
    bot.send_message(message.from_user.id, 'Simple(type simple); \nwith condition like\"must sit together\"(type condition);  ');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global amount
    amount = 0;
    global genamount
    genamount = 0;

    def moregroups(message):
        try:
            global amount; 
            amount = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Error8');
        sumofgengroup = 1
        bot.send_message(message.from_user.id, 'Enter the number of people of '+str(list(range(1, amount+1)))+" group");
        for i in range (1, amount+1):
            def polygroup(message):
                try:
                     global doki; 
                     doki = int(message.text)
                     return doki
                except Exception:
                     bot.send_message(message.from_user.id, 'Error8');
           
            bot.register_next_step_handler(message, polygroup);
            sumofgengroup = sumofgengroup * polygroup(message)
        print(sumofgengroup)
    
    def simple(message):
        try:
            global amount; 
            amount = int(message.text)
            amount = amount - 1 
            def simplesolution(amount):
                if amount == 0:
                    return 1
                return simplesolution(amount-1) * amount
            bot.send_message(message.from_user.id, "Result is "+ str(simplesolution(amount)))
        except Exception:
            bot.send_message(message.from_user.id, 'Error');
    def condition(message):
        try:
            global amount; 
            amount = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Error1');
        bot.send_message(message.from_user.id,'Enter the number of people (alert! You need to enter \"must sit together\" as one member. )');
        bot.register_next_step_handler(message, solcondition);
    def solcondition(message):
        try:
            global genamount; 
            genamount = int(message.text)
            genamount = genamount - 1
        except Exception:
            bot.send_message(message.from_user.id, 'Error2');
            
        def amountsquare(amount):
            if amount == 0:
                return 1
            return amountsquare(amount-1) * amount
        
        def conditionalfacto(genamount):
            if genamount == 0:
                return 1
            return conditionalfacto(genamount-1) * genamount
        
        result = conditionalfacto(genamount)* amountsquare(amount)
        print(result)
        bot.send_message(message.from_user.id, "Result is "+ str(result)+" ways")
    def bagit(message):
        try:
            global bit; 
            bit = str(message.text)
        except:
            bot.send_message(message.from_user.id, "Error")
        if bit == "1 group":
            bot.send_message(message.from_user.id, "enter the amount of people that must sit together")
            bot.register_next_step_handler(message, condition);
        elif bit == "more groups":
            bot.send_message(message.from_user.id, "how much group there are?")
            bot.register_next_step_handler(message, moregroups);
        else:
            bot.send_message(message.from_user.id, "Error")
    if message.text.lower() == "simple":
        bot.send_message(message.from_user.id, "You choose simple problems")
        bot.send_message(message.from_user.id, "enter the amount")
        bot.register_next_step_handler(message, simple);
    elif message.text.lower() == "condition":
        bot.send_message(message.from_user.id, "You choose with condition problems")
        bot.send_message(message.from_user.id, "There are two way: \n1) 1 group(enter \' 1 group\') \n2) more than one group(enter\'more groups\')")
        bot.register_next_step_handler(message, bagit);    
    else:
        bot.send_message(message.from_user.id, "Error")
    
    
bot.polling(none_stop=True, interval=0)
