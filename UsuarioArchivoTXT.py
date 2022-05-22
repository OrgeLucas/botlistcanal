## pip install pyTelegramBotAPI
## Estudiar esto:
## https://core.telegram.org/bots/api
## https://core.telegram.org/bots/api#html-style
# -*- coding: utf-8 -*-

# Importamos el m�dulo de pyTelegramBotAPI
import telebot

from telebot import *

# Creamos el bot. Sustituir <TOKEN> con el token de nuestro bot
bot = telebot.TeleBot('5376172259:AAHCy9TODVEBN7CqyqacbduSrdiwdnEky8s')

# Declaramos una funci�n que har� de listener. Todos los mensajes
# recibidos por el bot pasar�n por esta funci�n.
def listener(messages):
	for m in messages:
	# Comprobamos que el mensaje recibido sea de texto
		if m.content_type == 'text':
			# Y le respondemos con el texto propio del mensaje recibido.
			bot.reply_to(m, m.text)
			# Una vez creado el listener, debemos asign�rselo al bot.
			bot.set_update_listener(listener)
			# As� le indicamos c�mo manejar el comando '/start'
@bot.message_handler(commands=['start'])
def command_start(m):
	# En primer lugar, guardaremos en una variable el id de la
	# conversaci�n a la que debe dirigirse
	cid = m.chat.id
	# Con from_user obtenemos informaci�n del usuario
	# y con first_name, su nombre.
	nombre = m.from_user.first_name
	# A continuaci�n indicamos qu� debe decir el bot.
	## bot.send_message(cid, "Bievenido a este bot de pruebas<i>" + nombre + "</i>!", parse_mode="HTML")
	# Para almacenar los usuarios dentro de nuestro programa,
	# usaremos una lista
	LISTusuarios = list()
	# Despu�s, abriremos el fichero y por cada linea, iremos
	# insertando en nuestra lista el ID
	for linea in open('usuarios.txt','r'):
		# El fichero contiene texto, pero nosotros queremos n�meros
		# por lo que transformaremos cada l�nea a un n�mero entero.
		id = int(linea)
		# Y lo insertaremos en nuestra lista de usuarios
		LISTusuarios.append(id)
		# Comprobamos que el ID no est� en nuestros usuarios:
	if cid not in LISTusuarios:
		# Con from_user obtenemos informaci�n del usuario
		# y con first_name, su nombre.
		nombre = m.from_user.first_name
		# A continuaci�n indicamos qu� debe decir el bot.
		bot.send_message(cid, "Bievenido a este bot de pruebas <i>" + nombre + "</i>!", parse_mode="HTML")
		# Y lo guardamos como usuario tan to en la variable
		# como en el fichero
		LISTusuarios.append(cid)
		with open('usuarios.txt','a') as f:
			f.write(str(cid)+'\n')
			# Si ya es usuario, le avisamos
	else:
		bot.send_message(cid, "Ya eras usuario!")
		# Por �tlimo, hacemos el long-poll, es decir, le decimos al bot que# empiece a leer los mensajes que el bot reciba.
bot.polling(True)