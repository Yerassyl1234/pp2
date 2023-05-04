import os
import psycopg2
import telebot

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',    
    password='Jjd7UU3m'
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        phone BIGINT
    );
""")
conn.commit()

bot = telebot.TeleBot("6086388443:AAGCEBIC8i2nTcqqHyszP_J_KxvWO-I5mNU")
if not bot.token:
    raise ValueError("Missing required environment variable: BOT_TOKEN")

menu_commands = [
    telebot.types.BotCommand('start', 'Start the bot'),
    telebot.types.BotCommand('show', 'Показать зарегистрированные данные'),
    telebot.types.BotCommand('change', 'Изменить зарегистрированные данные'),
    telebot.types.BotCommand('delete', 'Удалить зарегистрированные данные'),
    telebot.types.BotCommand('help', 'Показать список доступных команд'),
]
bot.set_my_commands(menu_commands)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    if row:
        bot.reply_to(message, "Вы уже зарегистрированы. Воспользуйтесь командой /help, чтобы узнать доступные команды.")
    else:
        bot.reply_to(message, "Чтобы зарегистрироваться, введите свое имя, фамилию и номер телефона через пробел.")
        @bot.message_handler(content_types=['text'])
        def register(message):
            try:
                name, surname, phone = message.text.split()
            except ValueError:
                bot.reply_to(message, "Неверный формат данных. Введите имя, фамилию и номер телефона через пробел.")
                return
            user_id = message.from_user.id
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (user_id, name, surname, phone) VALUES (%s, %s, %s, %s)", (user_id, name, surname, phone))
            conn.commit()
            cursor.close()
            bot.reply_to(message, "Вы успешно зарегистрированы.")

@bot.message_handler(commands=['change'])
def change(message):
    user_id = message.from_user.id
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    if not row:
        bot.reply_to(message, "Вы не зарегистрированы.")
        return
    bot.reply_to(message, "Введите новое имя, фамилию и номер телефона через пробел.")
    bot.register_next_step_handler(message, change_name, user_id)

def change_name(message, user_id):
    try:
        name, surname, phone = message.text.split()
    except ValueError:
        bot.reply_to(message, "Неверный формат данных. Введите имя, фамилию и номер телефона через пробел.")
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, surname = %s, phone = %s WHERE user_id = %s", (name, surname, phone, user_id))
    conn.commit()
    cursor.close()
    bot.reply_to(message, "Ваши данные успешно изменены.")

@bot.message_handler(commands=['show'])
def show(message):
    user_id = message.from_user.id
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    if not row:
        bot.reply_to(message, "Вы не зарегистрированы.")
        return
    name, surname, phone = row[1], row[2], row[3]
    message_text = f"Ваши данные:\n\nИмя: {name}\nФамилия: {surname}\nНомер телефона: {phone}"
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['delete'])
def delete(message):
    user_id = message.from_user.id
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    if not row:
        bot.reply_to(message, "Вы не зарегистрированы.")
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    cursor.close()
    bot.reply_to(message, "Ваши данные успешно удалены.")

@bot.message_handler(commands=['help'])
def help(message):
    commands = [
        ("/start", "Начать регистрацию"),
        ("/show", "Показать зарегистрированные данные"),
        ("/change", "Изменить зарегистрированные данные"),
        ("/delete", "Удалить зарегистрированные данные"),
        ("/help", "Показать список доступных команд")
    ]
    message_text = "Доступные команды:\n\n"
    for command, description in commands:
        message_text += f"{command} - {description}\n"
    bot.reply_to(message, message_text)


bot.polling()

