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
msg_id = 999990
msgR_id = 9999990
msgX_id1 = 999999
msgX_id2 = 999999
msg_id_parametro = 99999999
msg_id_cliente_BOT = 9999999
msg_id_Veces_x_dia_BOT = 99999999
msg_mostrar = 99999999
texto = ""
configuraciones = {  }
lineas_enviar_mensajes = []
cx = 0
TOKEN1 =''
mi_chat_id = ''
mi_chad_id_canal = ''
TOKEN1 = os.environ['TOKEN']
mi_chat_id = os.environ['mi_chat_id']
mi_chad_id_canal =  os.environ['mi_chad_id_canal']
path1 = os.path.abspath(os.getcwd()) + '/'
bot = telebot.TeleBot(TOKEN1)
#este es otro canal

##t.me/promoorge



@bot.message_handler(content_types=["text"])
def cmd_texto1(message):
#    if message.text == '/test':
#        #if message.text == "1":
#        if w.hour > 9:
#            horaa = str(w.hour)
#        else:
#            horaa = "0" + str(w.hour)
#        clave0 = str(time.strftime('%d-%m-%Y', time.localtime())) + " " + horaa
#        print(clave0)
#        clave1 = "05-06-2022 11" 
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

        
        
        
        
        
        
    if message.text == '/reset':
        with open(path1 + 'configuraciones.txt','w') as f:
            f.write("")
        f.close
        with open(path1 + 'mensaje.txt','w') as f:
            f.write("")
        f.close
        with open(path1 + 'schedule.txt','w') as f:
            f.write("")
        f.close
        with open(path1 + 'schedule_temp.txt','w') as f:
            f.write("")
        f.close
        with open(path1 + 'Pruebas.txt','w') as f:
            f.write("")
        f.close
        with open(path1 + "schedule_schedule.txt", 'w') as f1:
            f1.write("")
        f1.close
        bot.send_message(mi_chat_id, "Envie el comndo /start 0 /alta para crer configuración nueva.")
                           
    if message.text == '/alta':
        estado = "alta"
        guardar_estado(estado)
        Correr_def = cmd_alta(message)
    else:
        if message.text == '/start':
            estado = "start"
            guardar_estado(estado)
            Correr_def = cmd_start(message)
        else:
            if message.text == '/help':
                estado = "help"
                guardar_estado(estado)
                #Correr_def = cmd_start(message)
                texto = "Datos de ayuda:\n"
                texto+= "/start : Inicia el Bot\n"
                texto+= "/alta : Para crear nueva configuración\n"
                texto+= "/publicar : Para incluir las publicaciones en la configuracion\n"
                texto+= "/finalizar : Para terminar y guardar publicaciones en la configuración\n"
                texto+= "/reset : Borra o elimina las configuraciones y publicaciones\n"
                texto+= "/agregarcanal : Agrega persona, grupo o canal a la lista de difusión\n"
                texto+= "/eliminarcanal : Elimina persona, grupo o canal de la lista de difusión\n"
                texto+= "/mostrarcanal : Muestra la lista de persona, grupo o canal para difusión\n"
                texto+= "/ayuda : La presente ayuda\n"
                texto+= "/help : La presente ayuda\n"
                mensaje = bot.send_message(mi_chat_id, texto, parse_mode="HTML")
            else:
                if message.text == '/ayuda':
                    estado = "ayuda"
                    guardar_estado(estado)
                    texto = "Datos de ayuda:\n"
                    texto+= "/start : Inicia el Bot\n"
                    texto+= "/alta : Para crear nueva configuración\n"
                    texto+= "/publicar : Para incluir las publicaciones en la configuracion\n"
                    texto+= "/finalizar : Para terminar y guardar publicaciones en la configuración\n"
                    texto+= "/reset : Borra o elimina las configuraciones y publicaciones\n"
                    texto+= "/agregarcanal : Agrega persona, grupo o canal a la lista de difusión\n"
                    texto+= "/eliminarcanal : Elimina persona, grupo o canal de la lista de difusión\n"
                    texto+= "/mostrarcanal : Muestra la lista de persona, grupo o canal para difusión\n"
                    texto+= "/ayuda : La presente ayuda\n"
                    texto+= "/help : La presente ayuda\n"
                    mensaje = bot.send_message(mi_chat_id, texto, parse_mode="HTML")
                else:
                    if message.text == '/finalizar':
                        estado = "finlizar"
                        guardar_estado(estado)
                        #Correr_def = cmd_finlizar(message)
                        # verificar que existe  mensajes 
                        if leer_mensaje(message):
                            if MostrarUltimaConfiguracionDesde_txt(message):
                                # leer las configuraciones guardaa y gurdarlos en schedule en formato de lista que luego leere con eval
                                with open(path1 + "configuraciones.txt", 'r', encoding="utf8") as f1:
                                    lines = f1.readlines()
                                    lines = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines]
                                f1.close
                                with open(path1 + "schedule.txt", 'a', encoding="utf8") as f1:
                                    f1.write(str(lines) + '\n')
                                f1.close
                                # leer los mensajes guardados y gurdarlos en schedule en formato de lista que luego leere con eval
                                with open(path1 + "mensaje.txt", 'r', encoding="utf8") as f1:
                                    lines2 = f1.readlines()
                                    lines2 = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines2]
                                f1.close
                                # guardar mensajes en schedule
                                with open(path1 + "schedule.txt", 'a', encoding="utf8") as f1:
                                    f1.write(str(lines2) + '\n')
                                f1.close
                                asfd = crear_y_guardar_schedule_temp(message)
                                # leer configuracion y generar schedule en formato de lista que luego leere con eval
                                with open(path1 + "schedule_temp.txt", 'r', encoding="utf8") as f1:
                                    lines3 = f1.readlines()
                                    lines3 = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines3]
                                f1.close
                                with open(path1 + "schedule.txt", 'a', encoding="utf8") as f1:
                                    f1.write(str(lines3) + '\n')
                                f1.close
                                with open(path1 + "schedule_schedule.txt", 'a', encoding="utf8") as f1:
                                    f1.write(str(lines3) + ']\n') # guardar solo la clave
                                f1.close
                                
                                ##########################################
                                ###########    abrir lo guardado   #######
                                # # # # with open(path1 + "schedule.txt", 'r', encoding="utf8") as f4:
                                    # # # # listasXX =  f4.readlines()
                                    # # # # #print(listasXX)
                                    # # # # #listasXX = list(listasXX)
                                    # # # # listas0 = eval(listasXX[0])
                                    # # # # listas1 = eval(listasXX[1])
                                    # # # # listas2 = eval(listasXX[2])
                                    # # # # listasR0 = ""
                                    # # # # ## leer configuraciones
                                    # # # # i = 0
                                    # # # # listasR0 = ""
                                    # # # # for i in listas0:
                                        # # # # listasR0+= str(i)
                                        # # # # print("conf: " + i)
                                # # # # with open(path1 + "Pruebas.txt", 'w', encoding="utf8") as f3:
                                    # # # # print(listasR0)
                                    # # # # f3.write(listasR0)
                                    # # # # f3.close
                                    # # # # ## leer mensajes
                                    # # # # i = 0
                                    # # # # listasR1 = ""
                                    # # # # for i in listas1:
                                        # # # # listasR1+= str(i)
                                        # # # # #print("msg: " + i)
                                # # # # with open(path1 + "Pruebas.txt", 'a', encoding="utf8") as f4:
                                    # # # # print(listasR1)
                                    # # # # f4.write(listasR1)                           
                                    # # # # f4.close
                                    # # # # ## leer schedule
                                    # # # # i = 0
                                    # # # # listasR2 = ""
                                    # # # # for i in listas2:
                                        # # # # listasR2+= str(i)
                                        # # # # #print("msg: " + i)
                                # # # # with open(path1 + "Pruebas.txt", 'a', encoding="utf8") as f4:
                                    # # # # print(listasR2)
                                    # # # # f4.write(listasR2)                           
                                # # # # f4.close                            
                            else:
                                bot.send_message(message.chat.id, "Envie el comndo /alta para crer configuración y luego /publicar para asociarlo a la configuración.")
                                # limpir mensajes
                                # limpiar estado
                                # limpiar configuraciones
                                # ....
                        else:
                            if MostrarUltimaConfiguracionDesde_txt(message):
                                bot.send_message(message.chat.id, "Envie el comndo /publicar para asociarlo a la configuración anterior.")
                            else:
                                bot.send_message(message.chat.id, "Envie el comndo /alta para crer configuración y luego /publicar para asociarlo a la configuración.")
                    else:
                        if message.text == '/publicar':
                            estado = "publicar"
                            guardar_estado(estado)         
                            ##Correr_def = cmd_start(message)
                            xxx = MostrarUltimaConfiguracionDesde_txt(message)
                            bot.send_message(message.chat.id, "Envie el mensaje para asociarlo a la configuración anterior.")
                            ##Correr_def = cmd_publicar(message) ##pass ##bot.send_message(message.chat.id, "publicaciones")
                        else:
                            Correr_def = cmd_publicar(message)

# ListaDinamicaConfiguraciones.txt
        #else:
            #clave1 = message.text
        #LineasDeF4 = []
        #LineasDeF4 = 0
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




def report():
    #w = datetime.now()
    #if message.text == "1":
    now = datetime.now()
    today = date.today()
    
    #print(horaC)
    #print(time.strftime('%d-%m-%Y', datetime.now()))
    horaC = int(now.hour)
    if horaC > 9:
        horaa = str(horaC)
    else:
        horaa = "0" + str(horaC)
    DIAC = int(today.day)
    if DIAC > 9:
        DIA = str(DIAC)
    else:
        DIA = "0" + str(DIAC)
    MESC = int(today.month)
    if MESC > 9:
        MES = str(MESC)
    else:
        MES = "0" + str(MESC)
    clave1 = str(DIA) + "-" + str(MES) + "-" + str(today.year) + " " + str(horaa)
    #    clave0 = str(time.strftime('%d-%m-%Y', datetime.now())) + " " + horaa
	#    clave0 = str(time.strftime('%d-%m-%Y', time.localtime())) + " " + horaa
    #print(Clave1)
    #clave1 = clave0 
    #clave1 = "05-06-2022 11" 
    linea = 0
    cx = 0
    with open(path1 + "schedule.txt", 'r', encoding="utf8") as f4:
        LineasDeF4 = f4.readlines()
        f4.seek(0)
        lineas_enviar_mensajes = f4.readlines()
    f4.close
    Fin = len(LineasDeF4)
    #print("  len(LineasDeF4): " + str(len(LineasDeF4)))
    sss = "no"
    for linea in range(Fin):
        listasXX = ""
        #f4.seek(0)
        listasXX =  LineasDeF4[linea] #f4.readlines(linea)

        if clave1 in listasXX:

            #print("index: " + str(c) +", linea: "+str(linea))
            lineas_enviar_mensajes[cx] = str(linea-1)
            if linea == Fin:
                pass
            else:    
                cx+= 1
                

                
            sss = "si"
        else:
            sss = "no"
            #lineas_enviar_mensajes[cx] = "999999999999"
            #lineas_mensajes
            #if linea == 0:
                #vfe = 34
            #else:
                #print("   cant msg: " + str(c))
                #lineas_enviar_mensajes[c] = str(linea-1)
                #print("   linea: " + str(linea))
                #print("   cant msg: " + str(c))

        #print("index: " + str(cx))# +", linea: " + str(linea) + " ddd:" + str(lineas_enviar_mensajes[cx]) + " enontro: " + sss)
        #print("   linea: " + str(linea) + " text:" + listasXX)    


    ### recorrer la lista de mensajes y enviarlos.
    linea_mensajes = []
    #linea_mensajes = 0
    list_mensajes = []
    #list_mensajes = 0
    #lineaX = []
    lineaX = 0
    i = 0
    iii = 0
    with open(path1 + "schedule.txt", 'r', encoding="utf8") as f4:
        lineas_leidas = f4.readlines()
        for iii in range(cx):
            #print("   leer msg temp: " + str(len(lineas_enviar_mensajes)))
            #f4.seek(0)
            LineaEspecifica = int(lineas_enviar_mensajes[iii])
            f4.seek(0)
            #lineas_leidas[LineaEspecifica] = f4.read()
            linea_mensajes = lineas_leidas[LineaEspecifica]
            #print("   int(lineas_enviar_mensajes[iii]):" + str(int(lineas_enviar_mensajes[iii])))
            #print("   lineas_leidas[LineaEspecifica] :" + str(lineas_leidas[LineaEspecifica]))
            #print("  LineaEspecifica " + str(LineaEspecifica))
            #linea_mensajes = f4.readline(int(lineas_enviar_mensajes[iii]))

            with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as fcanal:
                
                canal_send = fcanal.readlines()
                fcanal.close
            list_mensajes = eval(linea_mensajes)
            listasR = ""
            for ii in list_mensajes:
                listasR+= str(ii)
            with open(path1 + "mensaje_temp.txt", 'w', encoding="utf8") as fa:
                fa.write(listasR) 
            fa.close
            with open(path1 + "mensaje_temp.txt", 'r', encoding="utf8") as fc:
                #print("   leer msg temp: " + "4")
                msg_send = fc.readlines()
                i = 0
                for i in range(len(msg_send)):
                    for canalx in range(len(canal_send)):
                    	bot.copy_message(canal_send[canalx], mi_chat_id, int(msg_send[i])) 
                    	bot.send_message(mi_chat_id, "Mensage #: " + str(int(msg_send[i])) + " enviado al canal:" + str(canal_send[canalx]))
            fc.close
    f4.close
        
        
        
        
@bot.message_handler(content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "pinned_message"])
def cmd_otro1(message):
    Correr_def = cmd_publicar(message)
# @bot.message_handler(content_types=["video"])
# def cmd_videoo1(message):
    # Correr_def = cmd_publicar(message)
# @bot.message_handler(content_types=["audio"])
# def cmd_audio1(message):
    # Correr_def = cmd_publicar(message)







# @bot.message_handler(commands=['publicar'])#, 'help', 'ayuda']) /publicar
def cmd_publicar(message):
    
    # ggg = 133
    # estado = leer_estado(ggg) 
    
    # if estado == "publicar":
    	# estado = "indefinido"
    	# guardar_estado(estado)
    gggg = 133
    estado = leer_estado(gggg) 
    #print(estado)
    if estado == "publicar":
        #print("entro")
        estado = "ninguno"
        guardar_estado(estado)
        #Correr_def = cmd_publicaciones(message)
        #def cmd_publicaciones(message):
        DDDD = guardar_mensaje(str(message.message_id))
        textx = message.message_id
        bot.send_message(message.chat.id, "Mensge #: " + str(message.message_id) + " !Registrado!")
        bot.copy_message(mi_chad_id_canal, mi_chat_id, int(textx))
        #gggg = 133
#        mensaje = leer_mensaje(gggg)
#        bot.send_message(message.chat.id, "Mensges #: " + str(mensaje) + " !Registrados!")
        bot.send_message(message.chat.id, "comando /publicar o /finalizar para guardar schedule.")
        
        # cccc programar finalizar
    else:
        bot.send_message(message.chat.id, "Use los comandos /start , /publicar , /alta , /reset , /ayuda o /help ")    	
    	
#@bot.message_handler(commands=['publicar'])
#def cmd_publicar(message):
    #bot.send_message(message.chat.id, "enviaste el comando /publicar")
    #bot.send_message(message.chat.id, "Envie las publicaciones que desea tengan la configuracin anterior luego de enviar el comando /publicar . Para una nueva configuracin envie el comando /nueva.")

    
    
def cmd_ayuda(message):
	textoAyuda = 'Auda:\n'
	textoAyuda+= f'Usa comando /nueva para introducir tus datos\n'
	textoAyuda+= f'Usa comando /ayuda o /help para obtener ayuda\n'
	textoAyuda+= f'Usa comando /start para iniciar el bot\n'
	bot.send_message(message.chat.id, textoAyuda, parse_mode="HTML")
def cmd_start(message):
	##print(tipoMSG)
	# muestra los comandos disponibles
	#markup = telebot.types.ReplyKeyboardRemove()
	#bot.send_message(message.chat.id, "Usa comando /nueva para introducir tus datos", reply_markup=markup )
    xxx = MostrarUltimaConfiguracionDesde_txt(message)
    bot.send_message(message.chat.id, "Envie las publicaciones que desea tengan la última configuracin mostrada anteriormente. Para una nueva configuracin envie el comando /alta.")
# Responde al comando /nueva
##@bot.message_handler(commands=['nueva'])
def cmd_alta(message):
	# preguntar el por nombre Cliente del due�o de la publicaci�n
    ##      PEDIR CLIENTE ESTADO = COMPLETADO   ######################################################################
	markup = telebot.types.ForceReply()
	msgP = bot.send_message(message.chat.id, "Nombre del Cliente dueño de la publicación", reply_markup=markup )
	##msg_id_cliente_BOT = msgP.message_id
	## se obtiene nombre del cliente y se pregunta por el proximo dato
	bot.register_next_step_handler(msgP, preguntar_Gestor_Cliente)
	##msgX_id1 = msgR.message_id
def preguntar_Gestor_Cliente(message):
	configuraciones[message.chat.id] = {  }
	configuraciones[message.chat.id]["nombreCliente"] = ""
	configuraciones[message.chat.id]["nombreCliente"] = message.text
	configuraciones[message.chat.id]["nombreGestorCliente"] = ""
	configuraciones[message.chat.id]["VecesXdia"] = ""
	configuraciones[message.chat.id]["HoraInicio"] = ""
	configuraciones[message.chat.id]["FechaInicio"] = ""
	configuraciones[message.chat.id]["FechaFin"] = ""
	##Delete_msg_send(msg_mostrar)
	mmm = mostrar_datos(message)
	##Delete_msg_send(msg_id_cliente_BOT )
	# preguntar el por nombre del Gestor del este Cliente
    ##      PEDIR "GESTOR" ESTADO = "CONFIGURACIONES CLIENTE"   ######################################################################
	markup = telebot.types.ForceReply()
	msgP = bot.send_message(message.chat.id, "Nombre del Gestor de este Cliente", reply_markup=markup )
	##msg_id_Gestor_BOT = msgP.message_id
	bot.register_next_step_handler(msgP, preguntar_veces_x_dia)
	##print(msgR)
	#msgX_id2 = msgP.message_id
def preguntar_veces_x_dia(message):
    ##configuraciones[message.chat.id] = {  }
    configuraciones[message.chat.id]["nombreGestorCliente"] = message.text
    ##nombreCliente = message.text
    ##      PEDIR "VECES_X_DIA" ESTADO = "CONFIGURACIONES GESTOR"   ######################################################################
    mmm = mostrar_datos(message)
    markup = telebot.types.ForceReply()
    msgP = bot.send_message(message.chat.id, "¿Cuantas veces por día desea repetir la publicación?", reply_markup=markup)
    ##msg_id_Veces_x_dia_BOT = msgP.message_id
    ##Delete_msg_send(msg_mostrar)
    ##Delete_msg_send(msgX_id1 )
    ##Delete_msg_send(msg_id_Gestor_BOT)
    bot.register_next_step_handler(msgP, preguntar_hora_inicio)
def preguntar_hora_inicio(message):
	# preguntar 
	# si la hora inicio introducida no es un numero
    if not message.text.isdigit(): ## es verdadero si es un n�mero
		# informamos del error y volvemos a preguntar
        #mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, 'ERROR: Debes indicar un número. \n¿Cuantas veces por día desea repetir la publicación?')
		##msg_id_Veces_x_dia_BOT = msgP.message_id
		# volver a ejecutar la funci�n
        bot.register_next_step_handler(msgP, preguntar_veces_x_dia)
		##msgX_id3 = msgR.message_id
    else: #  si se introdujo el numero correcto veces_x_dia
        configuraciones[message.chat.id]["VecesXdia"] = int(message.text)
        ##      PEDIR "HORA_INICIO" ESTADO = "CONFIGURACIONES VECES_X_DIA"   ######################################################################
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la hora a la que desea se inicien las repeticiones?", reply_markup=markup)
        msg_id_Hora_BOT = msgP.message_id
        bot.register_next_step_handler(msgP, preguntar_fecha_inicio)
        ##msgX_id3 = msgR.message_id
        ##Delete_msg_send(msg_mostrar)
        #mmm = mostrar_datos(message)
def preguntar_fecha_inicio(message):
    # preguntar por 
    # si la hora inicio introducida no es un numero
    if not message.text.isdigit(): ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        ##      PEDIR "HORA_INICIO" ESTADO = "CONFIGURACIONES VECES_X_DIA"   ###############
        #mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿REPITA: Cual es la hora a la que desea se inicien las repeticiones?", reply_markup=markup)
        ##msg_id_Hora_BOT = msgP.message_id
        # volver a ejecutar la funci�n
        bot.register_next_step_handler(msgP, preguntar_fecha_inicio)
        msgX_id3 = msgR.message_id
    else: #  si se introdujo el numero correcto veces_x_dia
        configuraciones[message.chat.id]["HoraInicio"] = int(message.text)
        ##Delete_msg_send(msg_mostrar)
        mmm = mostrar_datos(message)
        ##Delete_msg_send(msg_id_Hora_BOT)
        ##Delete_msg_send(msgX_id1 )
        ##nombreCliente = message.text
        ##      PEDIR "FECHA_INICIO" ESTADO = "CONFIGURACIONES HORA_INICIO"   ###############
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha (dia/mes/año) en que iniciar las repeticiones?", reply_markup=markup)
        ##msg_id_fecha_inicial_BOT = msg.message_id
        bot.register_next_step_handler(msgP, preguntar_fecha_fin)
def preguntar_fecha_fin(message):
    # preguntar por 
    # si la fecha inicio introducida no es valida
    FechaValida = "NO"
    ##while True:
    ##except ValueError:FechaValida = "NO" ##print("Fecha inv�lida")
    try:
        fecha = message.text
        ##fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
        #print("ok")
        datetime.strptime(fecha, '%d-%m-%Y')
        FechaValida = "SI" ##print("Fecha v�lida")###while True:
    except:
        FechaValida = "NO"
        ##print("Fecha inválida")
    ##print("salio")					
    if FechaValida == "NO": ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        ##print("if not")
        ##      PEDIR "FECHA_INICIO" ESTADO = "CONFIGURACIONES HORA_INICIO"   ###############
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿REPITA: ¿Cual es la fecha (dia/mes/año 31/12/2022) en que iniciar las repeticiones?", reply_markup=markup)
        ##msg_id_fecha_inicial_BOT = msgP.message_id
        # volver a ejecutar la función
        bot.register_next_step_handler(msgP, preguntar_fecha_inicio)
        ##msgX_id3 = msgR.message_id
        
    else: #  si se introdujo la fecha valida 
        configuraciones[message.chat.id]["FechaInicio"] = message.text
        ##nombreCliente = message.text
        ##      PEDIR "FECHA_FIN" ESTADO = "CONFIGURACIONES FECHA_INICIO"   ###############
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha en que terminan las repeticiones?", reply_markup=markup)
        ##msg_id_fecha_Fin_BOT = msg.message_id
        bot.register_next_step_handler(msgP, Validar_datos_de_publicaciones)
        ##msgX_id3 = msgR.message_id
        ##Delete_msg_send(msg_mostrar)
        ##Delete_msg_send(msg_id_fecha_inicial_BOT)
def Validar_datos_de_publicaciones(message):
    # preguntar por 
    # si la fecha inicio introducida no es valida
    FechaValida = "NO"
    #FechaValida = "NO"
    ##while True:
    ##except ValueError:FechaValida = "NO" ##print("Fecha inv�lida")
    try:
        fecha = message.text
        ##fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
        datetime.strptime(fecha, '%d-%m-%Y')
        FechaValida = "SI" ##print("Fecha v�lida")###while True:
    except:
        FechaValida = "NO"
        ##print("Fecha inv�lida")
    if FechaValida == "NO": ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha en que terminan las repeticiones?", reply_markup=markup)
        ##msg_id_fecha_Fin_BOT = msg.message_id
        # volver a ejecutar la funci�n
        bot.register_next_step_handler(msgP, Validar_datos_de_publicaciones)
        ##msgX_id3 = msgR.message_id
    else: #  si se introdujo la fecha valida 
        configuraciones[message.chat.id]["FechaFin"] = message.text
        ##nombreCliente = message.text
        ##Delete_msg_send(msg_mostrar)
        # texto = f'<code>NombreCliente:</code> {configuraciones[message.chat.id]["nombreCliente"]}\n'
        # texto+= f'<code>NombreGestor.:</code> {configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
        # texto+= f'<code>Veces x día..:</code> {configuraciones[message.chat.id]["VecesXdia"]}\n'
        # texto+= f'<code>Hora Inicio..:</code> {configuraciones[message.chat.id]["HoraInicio"]}\n'
        # texto+= f'<code>FechaInicio..:</code> {configuraciones[message.chat.id]["FechaInicio"]}\n'
        # texto+= f'<code>FechaFin.....:</code> {configuraciones[message.chat.id]["FechaFin"]}\n'
        
        texto = f'{configuraciones[message.chat.id]["nombreCliente"]}\n'
        texto+= f'{configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
        texto+= f'{configuraciones[message.chat.id]["VecesXdia"]}\n'
        texto+= f'{configuraciones[message.chat.id]["HoraInicio"]}\n'
        texto+= f'{configuraciones[message.chat.id]["FechaInicio"]}\n'
        texto+= f'{configuraciones[message.chat.id]["FechaFin"]}\n'
        with open(path1 + 'configuraciones.txt','w') as f:
            f.write(texto)
        f.close
        xxx = MostrarUltimaConfiguracionDesde_txt(message)
        xxx1 = guardar_mensaje_nuevo("")
        bot.send_message(message.chat.id, "Se guardó correctamente la configuración. Utilice el comando /publicar para asociar publicaciones a esta configuración.")                    
        
        #mmm = mostrar_datos(message)
        ##markup = telebot.types.ForceReply()
        ##msgPublicaciones = bot.send_message(message.chat.id, "Envie las publicaciones que desea tengan la configuracin anterior. Para una nueva configuracin envie el comando /alta.", reply_markup=markup)
        
        ##bot.register_next_step_handler(msgPublicaciones, publicaciones)
        ##      PEDIR "PUBLICACIONES" ESTADO = "CONFIGURACIONES PUBLICACIONES"   ############### RECIBIR PUBLICACIONES
        ## ojoooooo
        ################################################ gtg = Guardar_txt_Conf(message)	##Delete_msg_send(msg_id_fecha_Fin_BOT)

def mostrar_datos(message):
    try:
        ##bot.delete_message(message.chat.id, msg_mostrar)
        markup = telebot.types.ForceReply()
        texto = 'Datos introducios:\n'
        texto+= f'<code>NombreCliente:</code> {configuraciones[message.chat.id]["nombreCliente"]}\n'
        texto+= f'<code>NombreGestor.:</code> {configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
        texto+= f'<code>Veces x día..:</code> {configuraciones[message.chat.id]["VecesXdia"]}\n'
        texto+= f'<code>Hora Inicio..:</code> {configuraciones[message.chat.id]["HoraInicio"]}\n'
        texto+= f'<code>FechaInicio..:</code> {configuraciones[message.chat.id]["FechaInicio"]}\n'
        texto+= f'<code>FechaFin.....:</code> {configuraciones[message.chat.id]["FechaFin"]}\n'
        markup = telebot.types.ReplyKeyboardRemove()
        msg_mostrarX = bot.send_message(message.chat.id, texto, parse_mode="HTML",  reply_markup=markup )
        ##def guardar_estado(estado):
        msg_mostrar =  msg_mostrarX.message_id
        ##print(configuraciones)
    except:
        pq = 1
################################################################################################################################
## eliminar mensajes
def MostrarUltimaConfiguracionDesde_txt(mensaje):
    with open(path1 + 'configuraciones.txt','r') as f:
        texto = f.readlines()
    f.close
    ##return texto
    configuraciones = {  }
    configuraciones[mensaje.chat.id] = {  }
    configuraciones[mensaje.chat.id]["nombreCliente"] = texto[0] #"Orge"
    configuraciones[mensaje.chat.id]["nombreGestorCliente"] =  texto[1] #"Orge G"
    configuraciones[mensaje.chat.id]["VecesXdia"] =  texto[2] #"6"
    configuraciones[mensaje.chat.id]["HoraInicio"] =  texto[3] #"7"
    configuraciones[mensaje.chat.id]["FechaInicio"] =  texto[4] #"06-06-2022"
    configuraciones[mensaje.chat.id]["FechaFin"] =  texto[5] #"07-06-2022"
    texto = 'Datos introducios:\n'
    texto+= f'<code>NombreCliente:</code> {configuraciones[mensaje.chat.id]["nombreCliente"]}'
    texto+= f'<code>NombreGestor.:</code> {configuraciones[mensaje.chat.id]["nombreGestorCliente"]}'
    texto+= f'<code>Veces x día..:</code> {configuraciones[mensaje.chat.id]["VecesXdia"]}'
    texto+= f'<code>Hora Inicio..:</code> {configuraciones[mensaje.chat.id]["HoraInicio"]}'
    texto+= f'<code>FechaInicio..:</code> {configuraciones[mensaje.chat.id]["FechaInicio"]}'
    texto+= f'<code>FechaFin.....:</code> {configuraciones[mensaje.chat.id]["FechaFin"]}'
    ##bot.send_message(mensaje.chat.id, "hola 2")
    ##markup = telebot.types.ReplyKeyboardRemove()
    ##markup = telebot.types.ForceReply()
    mensaje = bot.send_message(mensaje.chat.id, texto, parse_mode="HTML")
    return mensaje
      
    ###msgPublicaciones = bot.send_message(message.chat.id, "Envie las publicaciones que desea tengan la última configuracin mostrada anteriormente. Para una nueva configuracin envie el comando /alta.")
   
def Delete_msg_send(msg_id_parametro):
	try:
		bot.delete_message(message.chat.id, msg_id_parametro)
	except:
		pq = 1
##//////////////////////----------'zzzz///////////////////////////////////'
##/nueva
#def Guardar_txt_Conf(message):

def crear_y_guardar_schedule_temp(message):
    lines = ["yuy", "234", "2343"]
    with open(path1 + "configuraciones.txt", 'r', encoding="utf8") as f1:
        lines = f1.readlines()
        #lines = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines]
    f1.close
    # with open(path1 + "abre_borra_escribe_lee.txt", 'w', encoding="utf8") as f1:
        # #lines = f1.read()
        # #lines = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines]
        # f1.write(str(lines))
    # f1.close
    # with open(path1 + "abre_borra_escribe_lee.txt", 'r', encoding="utf8") as f4:
            # listasXX =  f4.read()
            # listasC = eval(listasXX)
            # listasR = ""
            #for i in listasC:
                	#listasR+= str(i)
                	#print("   " + i)

            ## leer configuraciones
    i = 0
    listasR0 = ""
    nombreCliente = ""
    nombreGestorCliente = ""		
    VecesXdia = 0
    HoraInicio = ""
    FechaInicio  = ""
    FechaFin  = ""
    # for i in listasC:
        # if i == 0:
    nombreCliente = lines[0] #str(i)
        # if i == 1:
    nombreGestorCliente = lines[1] #str(i)
        # if i == 2:
    VecesXdia = int(lines[2]) #str(i)   
        # if i == 3:
    HoraInicio = int(lines[3]) #str(i)
        # if i == 4:
    FechaInicio1 = lines[4] #str(i)
        # if i == 5:
    FechaFin1 = lines[5]#str(i)
    #f4.close
    #texto = 'Datos introducios:\n'
    #texto+= f'<code>NombreCliente:</code> {configuraciones[message.chat.id]["nombreCliente"]}\n'
    #texto+= f'<code>NombreGestor.:</code> {configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
    #texto+= f'<code>Veces x día..:</code> {configuraciones[message.chat.id]["VecesXdia"]}\n'
    #texto+= f'<code>Hora Inicio..:</code> {configuraciones[message.chat.id]["HoraInicio"]}\n'
    #texto+= f'<code>FechaInicio..:</code> {configuraciones[message.chat.id]["FechaInicio"]}\n'
    #texto+= f'<code>FechaFin.....:</code> {configuraciones[message.chat.id]["FechaFin"]}\n'
    ##cdi = 23
    ##usuarios.append(cid)

    ##FechaInicio = ""
    ##FechaFin = ""
    RecibirPublicaciones = 0
    #textoV = f' {configuraciones[message.chat.id]["nombreCliente"]}'
    ##if configuraciones[message.chat.id]["nombreCliente"]:
    textoV0 = nombreCliente
    textoV1 = nombreGestorCliente		
    textoV2 = VecesXdia
    textoV3 = HoraInicio
    textoV4 = FechaInicio1
    textoV5 = FechaFin1
    if textoV0:
        #nombreCliente = configuraciones[message.chat.id]["nombreCliente"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["nombreGestorCliente"]}'
    if textoV1:
        #nombreGestorCliente = configuraciones[message.chat.id]["nombreGestorCliente"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["VecesXdia"]}'
    if textoV2:
        #VecesXdia = configuraciones[message.chat.id]["VecesXdia"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["HoraInicio"]}'
    if textoV3:
        #HoraInicio = configuraciones[message.chat.id]["HoraInicio"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["FechaInicio"]}'
    if textoV4:
        # Convertimos un string con formato <d�a>/<mes>/<a�o> en datetime
        ## una_fecha = '20/04/2019'
        demo = FechaInicio1
        
        una_fecha = re.sub(r"^\s+|\s+$", "", demo) #demo # FechaInicio1.strip(' ') #FechaInicio1 #configuraciones[message.chat.id]["FechaInicio"]
        #print("  " + FechaInicio)
        
        FechaInicio= datetime.strptime(una_fecha, '%d-%m-%Y')
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["FechaFin"]}'
    if textoV5:
        # Convertimos un string con formato <d�a>/<mes>/<a�o> en datetime
        ## una_fecha = '20/04/2019'
        #string = FechaFin1
        demo = FechaFin1
       
        una_fecha =  re.sub(r"^\s+|\s+$", "", demo) #demo # 
        #una_fecha = FechaFin1.strip(' ') #FechaFin1 #configuraciones[message.chat.id]["FechaFin"]
        FechaFin = datetime.strptime(una_fecha, '%d-%m-%Y')
        RecibirPublicaciones += 1
        Fecha = FechaInicio
        
        
    if RecibirPublicaciones == 6:
        if int(VecesXdia) > 0:
            Cada_x_Hora = 24/VecesXdia 
            Cada_x_Hora = round(Cada_x_Hora, 0)
        else:
            Cada_x_Hora = 0
        DiasT = (FechaFin - FechaInicio).days + 1
        Continue = "no"
        with open(path1 + 'schedule_temp.txt','a') as f:
            try:
                DD = 0
                for DD in range(DiasT):
                    if DD == 0:
                        Fecha = FechaInicio
                        Continue = "si"
                    else:
                        if (Fecha +  timedelta(days=DD)) <= FechaFin:
                            Fecha = FechaInicio + timedelta(days=DD)
                            Continue = "si"
                        else:
                            Continue = "no"
                    
                    if Fecha.day > 9:
                        fechaRepet = str(Fecha.day)
                    else:
                        fechaRepet = "0" + str(Fecha.day)
                    if Fecha.month > 9:
                        fechaRepet = fechaRepet + "-" + str(Fecha.month) + "-" + str(Fecha.year)
                    else:
                        fechaRepet = fechaRepet + "-" + "0" + str(Fecha.month) + "-" + str(Fecha.year) 
                    ##datetime.datetime(datetime.strptime(Fecha, '%Y'), datetime.strptime(Fecha, '%m'), datetime.strptime(Fecha, '%d')) ##datetime.strptime(Fecha, '%d-%m-%Y')
                    horaRepet = 0
                    vc = 0
                    for vc in range(VecesXdia-1):
                        if Continue == "si" and horaRepet < 23:
                            if vc == 0:
                                horaRepet = HoraInicio
                            else:
                                horaRepet = HoraInicio + Cada_x_Hora*vc
                            ##"FECHA      H Cli Gest iDMSG"
                            if horaRepet > 9:
                                HotaTXT = str('{:.0f}'.format(horaRepet))
                            else:
                                HotaTXT = "0" + str('{:.0f}'.format(horaRepet)) 
                            cadena = fechaRepet + " " + HotaTXT + " " + nombreCliente + " " + nombreGestorCliente # + " " + str(message.message_id)##str(msg.message_id
                            if message.content_type == 'text':
                                bot.send_message(message.chat.id, "Config:" + cadena) #"Mensaje_TEXTO_Registrado_Número:"+str(message.message_id) + " Config:" + cadena)
                            if message.content_type == 'photo':
                                bot.send_message(message.chat.id, "Config:" + cadena) # "Mensaje_PHOTO_Registrado_N�mero:"+str(message.message_id) + " Config:" + cadena)
                            if message.content_type == 'audio':
                                bot.send_message(message.chat.id, "Config:" + cadena) # "Mensaje_AUDIO_Registrado_N�mero:"+str(message.message_id) + " Config:" + cadena)
                            if message.content_type == 'video':
                                bot.send_message(message.chat.id, "Config:" + cadena) # "Mensaje_VIDEO_Registrado_N�mero:"+str(message.message_id) + " Config:" + cadena)
                            f.write(cadena)
                #bot.send_message(message.chat.id, "Envie el comndo /alta para crer configuración y luego /publicar para asociarlo a la configuración.")
                bot.send_message(message.chat.id, "Se guardó correctamente la configuración con las publicaciones, se desea iniciar una nueva configuración use comando /alta")                    
                ## main ########################################################################################################################
            except:
                bot.send_message(message.chat.id, "No guardó!! Por favor repita desde el inicio con el comando /alta ")
        f.close()
    else:
        bot.send_message(message.chat.id, "Configuración vacia!, Por favor inicie una nueva configuración de publicaciones mediante el comando /alta")

@bot.message_handler(commands=['publicarRRRRRRRRRRRRRRRR'])   
def guardar_mensaje_nuevo(mensaje):
	with open(path1 + 'mensaje.txt','w') as f:
		f.write("")
	f.close
    
def guardar_mensaje(mensaje):
	with open(path1 + 'mensaje.txt','a') as f:
		f.write(str(mensaje) + '\n')
		f.close
def leer_mensaje(mensaje):
	with open(path1 + 'mensaje.txt','r') as f:
		mensaje = f.readline()
		return mensaje
	f.close	    

	
def leer_estado(estado):
	with open(path1 + 'estado.txt','r') as f:
	    	estado = f.readline()
	    	return estado
	f.close
    
    
    

def guardar_estado(estado):
	with open(path1 + 'estado.txt','w') as f:
		f.write(estado)
		f.close
	
	
def leer_estado(estado):
	with open(path1 + 'estado.txt','r') as f:
	    	estado = f.readline()
	    	return estado
	    	f.close

def guardar_schedule(schedule):
	with open(path1 + 'schedule.txt','w') as f:
		f.write(schedule)
		f.close

#if __name__ == '__main__':
    
def activar_schedule():
    print("     SCHEDULE INICIADO...")
    schedule.every().day.at("00:00").do(report)
    schedule.every().day.at("01:00").do(report)
    schedule.every().day.at("02:00").do(report)
    schedule.every().day.at("03:00").do(report)
    schedule.every().day.at("04:00").do(report)
    schedule.every().day.at("05:00").do(report)
    schedule.every().day.at("06:00").do(report)
    schedule.every().day.at("07:34").do(report)
    schedule.every().day.at("08:00").do(report)
    schedule.every().day.at("09:00").do(report)
    schedule.every().day.at("10:00").do(report)
    schedule.every().day.at("11:00").do(report)
    schedule.every().day.at("12:00").do(report)
    schedule.every().day.at("13:00").do(report)
    schedule.every().day.at("14:00").do(report)
    schedule.every().day.at("15:00").do(report)
    schedule.every().day.at("16:00").do(report)
    schedule.every().day.at("17:00").do(report)
    schedule.every().day.at("18:00").do(report)
    schedule.every().day.at("19:00").do(report)
    schedule.every().day.at("20:00").do(report)
    schedule.every().day.at("21:00").do(report)
    schedule.every().day.at("22:00").do(report)
    schedule.every().day.at("23:28").do(report)
    while True:
        schedule.run_pending()
        #print("	 Schedule runing...")
        ## bucle infinito en la que se comprueba si hay nuevos mensajes
        #bot.infinity_polling()
## responde a los mens


def recibir_mensajes():
	##bucle infinito que comproeba si hay nuevos mensajes
		bot.infinity_polling()

# Main ####################################
if __name__ == '__main__':
	print('    Iniciando el BOT')
	##bot.infinity_polling()
	hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
	hilo_bot.start()
	hilo_bot = threading.Thread(name="hilo_bot", target=activar_schedule)
	hilo_bot.start()
	print('   fin')
