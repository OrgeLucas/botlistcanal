##from config import *
import telebot
from telebot.types import *
import json
import pytz
import time
import datetime
from datetime import *
from datetime import datetime
from datetime import date
from datetime import timedelta
from time import perf_counter
from time import strptime
import io
from io import open
import os
import re
import schedule
from schedule import every
import threading
import requests

HORA_SCHEDULE = "20:23"
##import timedelta

msg_id = 999990
msgR_id = 9999990
msgX_id1 = 999999
msgX_id2 = 999999
msg_id_parametro = 99999999
msg_id_cliente_BOT = 9999999
msg_id_Veces_x_dia_BOT = 99999999
msg_mostrar = 99999999
texto = ""
lineas_enviar_mensajes = []
#lineas_enviar_mensajes = 0

#TOKEN1 = os.environ['TOKEN']
TOKEN1 = os.getenv('TOKEN')
path1 = os.path.abspath(os.getcwd()) + '/'
#mi_chat_id = 1188860009
#mi_chad_id_canal = -1001759781255
#bot = telebot.TeleBot('5376172259:AAHCy9TODVEBN7CqyqacbduSrdiwdnEky8s')
bot = telebot.TeleBot(TOKEN)
mi_chat_id = os.getenv('mi_chat_id')
#mi_chat_id = os.environ['mi_chat_id']
mi_chad_id_canal =  os.getenv('mi_chat_id')
#mi_chad_id_canal =  os.environ['mi_chat_id']
cx = 0
@bot.message_handler(content_types=["text"])

def cmd_texto1(message):
    if message.text == '/mostrarcanal':
    	 #PersonaGrupoCanal.txt
    	 vgvg = mostrarcanal(message)

    if message.text == '/agregarcanal': #PersonaGrupoCanal.txt
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(mi_chat_id, "Envie el número de persona, Grupo o Canal para agregarlo.", reply_markup=markup )
        bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_agregar)
    if message.text == '/eliminarcanal': #PersonaGrupoCanal.txt
        #PersonaGrupoCanal.txt
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(mi_chat_id, "Envie el número de persona, Grupo o Canal para eliminarlo.", reply_markup=markup )
        bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_eliminar)
def mostrarcanal(message):
	        with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
	        	LineasDeF4 = f4.read()
        		f4.close
        		bot.send_message(mi_chat_id, "Lista de Personas Grupos o Canales: " + str(LineasDeF4))
def preguntar_persona_Grupo_Canal_eliminar(message):
    linea = 0
    with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
        LineasDeF4 = f4.read()
        f4.close
        s = str(LineasDeF4)
        clave1 = message.text
        #s = "Naze
        new_s = s.replace(clave1+ '\n', '')
        with open(path1 + "PersonaGrupoCanal.txt", 'w', encoding="utf8") as f:
        	f.write(new_s)
        	f.close
        	with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
        		LineasDeF41 = f4.read()
        	f4.close
        	vgvg = mostrarcanal(message)
        	#bot.send_message(mi_chat_id, "Lista de Personas Grupos o Canales: " + str(LineasDeF41))

def preguntar_persona_Grupo_Canal_agregar(message):
    persona_grupo_canal = message.text
    if persona_grupo_canal[0:0] == "-":
        canal = -1 * int(persona_grupo_canal)
        Agregarlo = canal
    else:
        persona_grupo = int(persona_grupo_canal)
        Agregarlo = persona_grupo
    with open(path1 + "PersonaGrupoCanal.txt", 'a', encoding="utf8") as f:
        f.write(str(Agregarlo) + '\n')
    f.close
    with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f:
        canales = f.read()
    f.close
    bot.send_message(mi_chat_id, "Se agregó a la lista de Personas Grupos o Canales: " + str(canales))
print("	 Llegó al final...")        
def recibir_mensajes():
	##bucle infinito que comproeba si hay nuevos mensajes
    bot.infinity_polling()

# Main ####################################
if __name__ == '__main__':
	print('    Iniciando el BOT')
	##bot.infinity_polling()
	hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
	hilo_bot.start()
	#hilo_bot = threading.Thread(name="hilo_bot", target=activar_schedule)
	#hilo_bot.start()
	print('   fin')