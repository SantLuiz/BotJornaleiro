import telebot, os
from dotenv import load_dotenv

load_dotenv(".env") 
ChaveApi = os.getenv("TOKEN_TELEBOT")

if not ChaveApi:
    raise ValueError("A chave da API não foi encontrada no .env")

print(f"Chave API carregada: {ChaveApi}")


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



def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def BoasVindas(msg):
    textoMsg = f"""
Olá,{msg.from_user.first_name}, 
Seja Bem-Vindo ao Bot Jornaleiro

Escolha uma das opções abaixo:
(Clique no item)

->  /ConfigurarGeral
->  /ConfigurarFontes
->  /ConfigurarAssuntos
"""
    bot.send_message(msg.chat.id, textoMsg)










bot.polling()
