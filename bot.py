import telebot

TOKEN = '7384331973:AAHtjjNtG5p6hQbnZRoi9eyyja_nB43QLgE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я — AI-бот агентства Kenny AI Services.

Выберите опцию:
1. Заказать услугу
2. Посмотреть услуги
3. Связаться с Kenny")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "1" in message.text:
        bot.reply_to(message, "🧠 Заказать услугу:
Напишите, что вам нужно, и Kenny ответит лично.")
    elif "2" in message.text:
        bot.reply_to(message, "📋 Доступные услуги:
• Резюме / CV
• Сценарий и озвучка видео
• Чат-бот Telegram
• Тексты для бизнеса
• AI-презентации")
    elif "3" in message.text:
        bot.reply_to(message, "Связь с Kenny: @Kenny_Corleone")
    else:
        bot.reply_to(message, "Выберите 1, 2 или 3 для продолжения.")

bot.polling()
