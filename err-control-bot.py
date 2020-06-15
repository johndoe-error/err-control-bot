import telebot

bot = telebot.TeleBot('token')
admins = [930416869, 993368774, 1098481550, 774618861]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет, меня зовут ERROR ControlBot и я слежу за выполнением правил в этом чате!\nПосмотреть их можно командой /rules!\nПриятного общения!")

@bot.message_handler(func=lambda message: message.entities is not None )
def delete_links(message):
	if (str(message.from_user.id) not in admins):
		j = 0
		for entity in message.entities:  
			j = j + 1
			if (j == 1):
				if (entity.type in ["text_link", "url"]):
					bot.reply_to(message,"@Mieri_1 @LegendaryShadow @J_doe\n================================\n@" + str(message.from_user.username) + ", кажется, ты нарушил 1️⃣ или 2️⃣ правило...\nНажми /rules, чтобы посмотреть остальные правила этого чата!")
					bot.forward_message(1098481550, message.chat.id, message.message_id)
					bot.delete_message(message.chat.id, message.message_id)
					bot.send_message(1098481550, "Я удалил это сообщение из чата " + str(message.chat.title) + " по причине " + entity.type)
				if entity.type in ["hashtag"]:
					bot.reply_to(message,"Хэй, @" + message.from_user.username + ", в этом чате не разрешено кидать хэштеги! Впредь будь аккуратней!)\nНажми /rules, чтобы посмотреть остальные правила этого чата!")
					bot.delete_message(message.chat.id, message.message_id)
				if entity.type in ["bot_command"]:
					bot.delete_message(message.chat.id, message.message_id)

#				if (entity.type in ["pre"]):					
#					body			
#				if entity.type in ["email"]:
#					body
#				if entity.type in ["bold"]:
#					body
#				if entity.type in ["mention"]:
#					body
#				if (entity.type in ["italic"]):
#					body
#               if entity.type in ["code"]:
#					body

bot.polling()
