import telebot, os, emoji
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv(".env") 
ChaveApi = os.getenv("TOKEN_TELEBOT")

if not ChaveApi:
    raise ValueError("A chave da API não foi encontrada no .env")

bot = telebot.TeleBot(ChaveApi)

#https://core.telegram.org/bots/api -> Documentação API
#https://core.telegram.org/bots -> Documentação Bots em geral do Telegram



@bot.message_handler(commands=["ConfigurarGeral"])
def ConfigGeral(msg):
    bot.send_message(msg.chat.id, "Configurações Gerais")


@bot.message_handler(commands=["ConfigurarFontes"])
def ConfigGeral(msg):
    bot.send_message(msg.chat.id, "Configurações de Fontes")


@bot.message_handler(commands=["ConfigurarAssuntos"])
def ConfigGeral(msg):
    bot.send_message(msg.chat.id, "Configuração de Assuntos")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "noticias":
        bot.answer_callback_query(call.id, "Aqui estão as suas noticias")
    elif call.data == "concursos":
        bot.answer_callback_query(call.id, "Aqui estão os concursos publicados recentemente")


def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def BoasVindas(msg):

    markup = InlineKeyboardMarkup()

    #btn1 = InlineKeyboardButton(emoji.emojize(":gear:"), url="https://www.google.com")
    #btn2 = InlineKeyboardButton(emoji.emojize(":newspaper:"), callback_data="botao_clicado")
     #markup.add(btn1, btn2)

    markup.row(InlineKeyboardButton(emoji.emojize(":newspaper:"), callback_data="noticias"),
               InlineKeyboardButton(emoji.emojize(":receipt:"), callback_data="concursos"),
               InlineKeyboardButton(emoji.emojize(":gear:"), url="https://www.google.com"),)

   


    textoMsg = f"""
Olá,{msg.from_user.first_name}, 
Seja Bem-Vindo ao Bot Jornaleiro

Escolha uma das opções abaixo:
(Clique no item)
"""
    bot.send_message(msg.chat.id, textoMsg, reply_markup=markup)










bot.polling()
