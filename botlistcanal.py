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
from time import *
from time import sleep
import io
from io import open
import os
import re
import schedule
from schedule import every
import threading
HORA_UNICA = "00:00"
SLEEP_VAR = 0
msg_id = 999990
msgR_id = 9999990
msgX_id1 = 999999
msgX_id2 = 999999
msg_id_parametro = 99999999
msg_id_cliente_BOT = 9999999
msg_id_Veces_x_dia_BOT = 99999999
msg_mostrar = 99999999
textom = []
configuraciones = {  }
lineas_enviar_mensajes = []
cx = 0
bhtvgrr=567
TOKEN1 = ''
mi_chat_id = ''
mi_chad_id_canal = ''
ghtyygt = 10
# TOKEN1 = os.environ['TOKEN']
# mi_chat_id = os.environ['mi_chat_id']
# mi_chad_id_canal =  os.environ['mi_chad_id_canal']
mi_chat_id = 1188860009
mi_chad_id_canal = -1001759781255
TOKEN1 = '2011870885:AAEKWSIAq5MSj7tIzApZwsQADHRaBwcjGMM'


path1 = os.path.abspath(os.getcwd()) + '/'
bot = telebot.TeleBot(TOKEN1)
#este es otro canal
##t.me/promoorge
Agregarlo = ""

@bot.message_handler(content_types=["text"])
def cmd_texto1(message):
    if message.text == '/publicarboton': # Reenvia mensaje existente en nustro chat_id a ti mismo nuevamente.
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Envie los botones en el siguiente formato:\n Nombre * https://www.google.com \n \n Si desea un boton al lado del otro utilice el separador && \n Nombre1 - http://www.google.com && Nombre2 - http://www.yahoo.com \n \nSi desea un boton debajo del otro use la tecla entre \n Nombre1 - http://www.google.com \n Nombre2 - http://www.yahoo.com \n Luego enviar.", reply_markup=markup)
        bot.register_next_step_handler(msgP, Send_botones) 
    if message.text[0:6] == '/idmsg': # Reenvia mensaje existente en nustro chat_id a ti mismo nuevamente.
        #venceconfig
        Id_MSG_numero(message)
    if message.text == '/venceconfig':
        #venceconfig
        report_fecha_vence(message)
    if message.text == '/verconfig':
        #verconfig
        verconfiguraciones(message)
    if message.text == '/sendahora':
        bot.send_message(mi_chat_id, "/sendahora recibido.")
        sendahora = ""
        HORA_UNICA = "99:99"
        sendahora = report1(HORA_UNICA)
        vnce1 = ""
        ####vnce1 = report_fecha_vence()
        
        ##HORA_UNICA = "00:00"
        #markup = telebot.types.ForceReply()
        #msgP = bot.send_message(mi_chat_id, "Envie la hora y minutos a los que desea se envien las publicaciones, ejemplo: 01:00.", reply_markup=markup )
        #bot.register_next_step_handler(msgP, preguntar_hora_unica)
        #para cancelar las configuraciones iniciadas antes de guardar.
    if message.text == '/sendfechahora':
        Send_lo_de_esta_fecha_horaF0(message)
    if message.text == '/cancelconfig':
        with open(path1 + 'configuraciones.txt','w') as f:
        	f.write("")
        f.close
        bot.send_message(mi_chat_id, "Envie el comndo /start 0 /alta para crer configuración nueva.")
        #cambiar estado 
        #limpiar configuraciones
        
    # si se envia /bajartxt se envian los txt relacionados al chat que lo solicita
    if message.text == '/bajartxt':
        bajartxtF0(message)
    
    if message.text == '/mostrarcanal':
    	 #PersonaGrupoCanal.txt
    	 vgvg = mostrarcanal(message)

    if message.text == '/agregarcanal': #PersonaGrupoCanal.txt
        # markup = telebot.types.ForceReply()
        # msgP = bot.send_message(mi_chat_id, "Envie el número de persona, Grupo o Canal para agregarlo.", reply_markup=markup )
        # bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_agregar)
        vgvg1 = preguntar_persona_Grupo_Canal_agregar(message)
        
        
    if message.text == '/eliminarcanal': #PersonaGrupoCanal.txt
        eliminarcanalF0(message)

    if message.text == '/eliminarconfig':
        eliminarconfiguracionF0(message)
        
    if message.text == '/sendpuplicaciones':
        preguntar_hora_de_envioPaso1(message)

        
    if message.text == '/reset':
        resetF0(message)
                           
    if message.text == '/alta':
        estado = "alta"
        guardar_estado(estado)
        Correr_def = cmd_alta(message)
        
        
    if message.text == '/start':
        estado = "start"
        guardar_estado(estado)
        Correr_def = cmd_start(message)
        
        #ayuda1 = 0
    if message.text == '/help':
        ayuda1(message) # = "1"
    if message.text == '/ayuda':
        ayuda1(message) # = "1"

    if message.text == '/finalizar':
        estado = "finlizar"
        guardar_estado(estado)
        now = datetime.now()
        today = date.today()
        #Correr_def = cmd_finlizar(message)
        # verificar que existe  mensajes 
        if leer_mensaje(message):
            if MostrarUltimaConfiguracionDesde_txt(message):
                # leer las configuraciones guardaa y gurdarlos en schedule en formato de lista que luego leere con eval
                with open(path1 + "configuraciones.txt", 'a', encoding="utf8") as fnumero:
                    today = date.today()
                    fnumero.write(str(today.day) + "." + str(today.month) + "." + str(today.year) + "." + str(now.hour) + "." + str(now.second) + '\n')
                fnumero.close
                ################configuraciones[message.chat.id]["Numero"] = 
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
                                
            else:
                bot.send_message(message.chat.id, "Envie el comando /alta para crer configuración y luego /publicar para asociarlo a la configuración.")
                # limpir mensajes
                # limpiar estado
                # limpiar configuraciones
                # ....
        else:
            if MostrarUltimaConfiguracionDesde_txt(message):
                bot.send_message(message.chat.id, "Envie el comndo /publicar para asociarlo a la configuración anterior.")
            else:
                bot.send_message(message.chat.id, "Envie el comndo /alta para crer configuración y luego /publicar para asociarlo a la configuración.")
    if message.text == '/publicar':
        xxx = MostrarUltimaConfiguracionDesde_txt(message)
        if xxx:
            estado = "publicar"
            guardar_estado(estado)         
            ##Correr_def = cmd_start(message)
            bot.send_message(message.chat.id, "Envie el mensaje para asociarlo a la configuración anterior.")
            ##Correr_def = cmd_publicar(message) ##pass ##bot.send_message(message.chat.id, "publicaciones")
    else:
        Correr_def = cmd_publicar(message)

def Send_botones(message):
    clave = {  } 
    idboton = 0
    capboton = {  } 
    link = {  } 
    nombreboton = ""
    urllink = ""
    #claveboton = ""
    fila = 0
    inicio_capboton = 0
    inicio_link = 0
    fin_capboton = 0
    fin_link = 0
    duo = ""
    trio = ""
    cuarteto = ""
    cadena = ""
    nuevo_boton = "no"
    total_fila = 0
    total_idboton = 0
    total_cadena = 0
    #clave[fila]["claveboton"] = ""
    filaboton = []
    link[fila] = {  } 
    capboton[fila] = {  } 
    #link_arr = [[][]]# [[fila][idboton]]= {  } 
    capboton_arr = []#[[fila][idboton]] = {  } 
    #link = [[fila][idboton]["urllink"] = ""
    #capboton[fila][idboton]["nombreboton"] = ""
    cadena = message.text
    ##print(message.text)
    ##print(".......................")
    # if "\n" in cadena:
        # ##print(" tiene" + )

    i = 0
    total_cadena = len(cadena)
    markup = InlineKeyboardMarkup()
    for i in range(total_cadena+1):
        if i == 0:
            inicio_capboton = 0
        duo = cadena[i:i+2] #duo == "\n":
        trio = cadena[i:i+3] #if trio == " * ":
        cuarteto = cadena[i:i+4] #cuarteto == " ** ":
        ##print("  duo:" + duo + "[")
        ##print("  trio:" + trio + "[") 
        ##print("  cuarteto:" + cuarteto + "[") 

        if trio == " * ":
            fin_capboton = i
            inicio_link = i + 3

            nombreboton = cadena[inicio_capboton:fin_capboton]

        if duo.find("\n") > 0: # == "\n":
            #link[fila][idboton]["urllink"] = cadena[inicio_link:i+1]
            urllink = cadena[inicio_link:i]
            capboton = [fila, idboton, nombreboton, urllink]
            #filaboton = [fila, idboton] 
            #capboton_arr.append(filaboton)
            capboton_arr.append(capboton)
           
            ##print("  fila: " + str(fila) + " idboton: " + str(idboton) + " urllink : " + str(capboton_arr))#[fila][idboton]["urllink"]))
            ##print("\n  arr :\n " + str(capboton_arr))
            inicio_capboton = i + 2
            fin_link = i - 1
            fila+= 1
            idboton+= 1
            #clave[fila]["claveboton"]+= "\n"
        if cuarteto == " ** ":
            #link[fila][idboton]["urllink"]= cadena[inicio_link:i]
            urllink = cadena[inicio_link:i-1]
            #filaboton = [fila, idboton]
            capboton = [fila, idboton, nombreboton, urllink]
            #capboton_arr.append(filaboton)
            capboton_arr.append(capboton)
            inicio_capboton = i + 4
            fin_link = i - 1
            #fila+= 1
            idboton+= 1
            #clave[fila]["claveboton"]+= " ** "
        ##print("  i-1:" + str(i) + "[") 
        ##print("  total_cadena:" + str(total_cadena) + "[") 
        if (total_cadena-1) == i-1:
            ##print("  entro")
            if duo == "\n" or cuarteto == " ** ":
                pass
            else:
                ##print("  entro222")
                #link[fila][idboton]["urllink"] = cadena[inicio_link:i]
                urllink = cadena[inicio_link:i]
                #filaboton = [fila, idboton]
                capboton = [fila, idboton, nombreboton, urllink]
                #capboton_arr.append(filaboton)
                capboton_arr.append(capboton)

                ##print("  fila: " + str(fila) + " idboton: " + str(idboton) + " urllink : " + str(capboton_arr))#link[fila][idboton]["urllink"]))
                fin_link = i - 1

    i_fila = 0
    i_idboton = 0
    fila_boton = []
    contar_botones_por_fila = {  }
    contar_botones_por_fila[i_fila] = {  }
    #contar_botones_por_fila[0] = 0
    total_fila_arr = len(capboton_arr)
    #step = 2
    #contar_botones_por_fila.append(0) 
    var = 0
    cont_boton = 0
    filax1 = 0
    for i_fila_arr in range(total_fila_arr):#, step):
        
        if capboton_arr[i_fila_arr][0] == var:
            cont_boton+= 1
            contar_botones_por_fila[filax1] = cont_boton
        	
        else:
            filax1+= 1
            cont_boton = 1
            contar_botones_por_fila[filax1] = cont_boton
            var = capboton_arr[i_fila_arr][0]
    #print("  botones fila: " + str(contar_botones_por_fila))        

    ##print("   fgffgg")
    ##print("  botones fila: " + str(0) + " cant boton: " + str(contar_botones_por_fila[0]))
    ##print("  botones fila: " + str(1) + " cant boton: " + str(contar_botones_por_fila[1]))
    i_fila = 1
    ttt = len(contar_botones_por_fila)
    fx = 0
    for i_fila in range(ttt):
        if i_fila == 0:
            fx = 0
        ##print("  botones fila: " + str(i_fila) + " cant boton: " + str(contar_botones_por_fila[i_fila]))
        if contar_botones_por_fila[i_fila] == 1:
            
            
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            markup.add(button1)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
                
        if contar_botones_por_fila[i_fila] == 2:
            ##print("  botones fila: " + str(i_fila) + " cant boton: " + str(contar_botones_por_fila[fx]))
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            markup.add(button1, button2)       
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
                
        if contar_botones_por_fila[i_fila]== 3:
            
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
            markup.add(button1, button2, button3)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""
                
        if contar_botones_por_fila[i_fila] == 4:

            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
            fx+= 1

            nombre4 = capboton_arr[fx][2]
            Url4 = capboton_arr[fx][3]
            button4 = InlineKeyboardButton(nombre4,url=f'{Url4}')
            markup.add(button1, button2, button3, button4)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""                   
            nombre4 = ""
            Url4 = ""
            button4 = "" 
                
        if contar_botones_por_fila[i_fila] == 5:
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
            fx+= 1

            nombre4 = capboton_arr[fx][2]
            Url4 = capboton_arr[fx][3]
            button4 = InlineKeyboardButton(nombre4,url=f'{Url4}')
            fx+= 1

            nombre5 = capboton_arr[fx][2]
            Url5 = capboton_arr[fx][3]
            button5 = InlineKeyboardButton(nombre5,url=f'{Url5}')
            markup.add(button1, button2, button3, button4, button5)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""                   
            nombre4 = ""
            Url4 = ""
            button4 = "" 
            nombre5 = ""
            Url5 = ""
            button5 = "" 
                
        if contar_botones_por_fila[i_fila] == 6:
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
            fx+= 1

            nombre4 = capboton_arr[fx][2]
            Url4 = capboton_arr[fx][3]
            button4 = InlineKeyboardButton(nombre4,url=f'{Url4}')
            fx+= 1

            nombre5 = capboton_arr[fx][2]
            Url5 = capboton_arr[fx][3]
            button5 = InlineKeyboardButton(nombre5,url=f'{Url5}')
            fx+= 1

            nombre6 = capboton_arr[fx][2]
            Url6 = capboton_arr[fx][3]
            button6 = InlineKeyboardButton(nombre6,url=f'{Url6}')
            markup.add(button1, button2, button3, button4, button5, button6)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""                   
            nombre4 = ""
            Url4 = ""
            button4 = "" 
            nombre5 = ""
            Url5 = ""
            button5 = ""                     
            nombre6 = ""
            Url6 = ""
            button6 = ""   
                
        if contar_botones_por_fila[i_fila] == 7:
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
             
            fx+= 1
            nombre4 = capboton_arr[fx][2]
            Url4 = capboton_arr[fx][3]
            button4 = InlineKeyboardButton(nombre4,url=f'{Url4}')
            
            fx+= 1
            nombre5 = capboton_arr[fx][2]
            Url5 = capboton_arr[fx][3]
            button5 = InlineKeyboardButton(nombre5,url=f'{Url5}')
            
            fx+= 1
            nombre6 = capboton_arr[fx][2]
            Url6 = capboton_arr[fx][3]
            button6 = InlineKeyboardButton(nombre6,url=f'{Url6}')
            
            fx+= 1
            nombre7 = capboton_arr[fx][2]
            Url7 = capboton_arr[fx][3]
            button7 = InlineKeyboardButton(nombre7,url=f'{Url7}')
            markup.add(button1, button2, button3, button4, button5, button6, button7)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""                   
            nombre4 = ""
            Url4 = ""
            button4 = "" 
            nombre5 = ""
            Url5 = ""
            button5 = ""                     
            nombre6 = ""
            Url6 = ""
            button6 = ""                       
            nombre7 = ""
            Url7 = ""
            button7 = ""    
                
        if contar_botones_por_fila[i_fila] == 8:
            nombre1 = capboton_arr[fx][2]
            Url1 = capboton_arr[fx][3]
            button1 = InlineKeyboardButton(nombre1,url=f'{Url1}')
            fx+= 1
            nombre2 = capboton_arr[fx][2]
            Url2 = capboton_arr[fx][3]
            button2 = InlineKeyboardButton(nombre2,url=f'{Url2}')
            fx+= 1
            nombre3 = capboton_arr[fx][2]
            Url3 = capboton_arr[fx][3]
            button3 = InlineKeyboardButton(nombre3,url=f'{Url3}')
              
            fx+= 1
            nombre4 = capboton_arr[fx][2]
            Url4 = capboton_arr[fx][3]
            button4 = InlineKeyboardButton(nombre4,url=f'{Url4}')
            
            fx+= 1
            nombre5 = capboton_arr[fx][2]
            Url5 = capboton_arr[fx][3]
            button5 = InlineKeyboardButton(nombre5,url=f'{Url5}')
            fx+= 1

            nombre6 = capboton_arr[fx][2]
            Url6 = capboton_arr[fx][3]
            button6 = InlineKeyboardButton(nombre6,url=f'{Url6}')
            fx+= 1

            nombre7 = capboton_arr[fx][2]
            Url7 = capboton_arr[fx][3]
            button7 = InlineKeyboardButton(nombre7,url=f'{Url7}')
            fx+= 1

            nombre8 = capboton_arr[fx][2]
            Url8 = capboton_arr[fx][3]
            button8 = InlineKeyboardButton(nombre8,url=f'{Url8}')
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
            fx+= 1
            nombre1 = ""
            Url1 = ""
            button1 = ""
            nombre2 = ""
            Url2 = ""
            button2 = ""
            nombre3 = ""
            Url3 = ""
            button3 = ""                   
            nombre4 = ""
            Url4 = ""
            button4 = "" 
            nombre5 = ""
            Url5 = ""
            button5 = ""                     
            nombre6 = ""
            Url6 = ""
            button6 = ""                       
            nombre7 = ""
            Url7 = ""
            button7 = ""                       
            nombre8 = ""
            Url8 = ""
            button8 = ""     
                
        if contar_botones_por_fila[i_fila] > 8:
            pass
    bot.send_message(message.chat.id,'Clic en el boton para contactarme..',reply_markup=markup)



def Send_lo_de_esta_fecha_horaF0(message):
    markup = telebot.types.ForceReply()
    msgP = bot.send_message(message.chat.id, "Envíe la fecha y la hora (Ejemplo1: 05-05-2022 02 Ejemplo2: 30-12-2022 13) para enviar ahora las publicaciones que cumplan con esa configuración.", reply_markup=markup)
    bot.register_next_step_handler(msgP, Send_lo_de_esta_fecha_horaF1)


def Send_lo_de_esta_fecha_horaF1(message): #ejemplo1: 05-05-2022 02 ejemplo2: 30-12-2022 13
    Cadenap = message.text
    DIA_t = Cadenap[0:2]
    MES_t = Cadenap[3:5]
    ANO_t = Cadenap[6:10]
    HORA_t = Cadenap[11:13]
    fecha_t = Cadenap[0:10]
    try:
        #print("   dia mes año y hora" + fechahora[0:2] + "-" + fechahora[3:5] + "-" + fechahora[6:9] + " " + Cadenap[11:13])
        DIA_vallido = int(DIA_t)
        MES_vallido = int(MES_t)
        ANO_vallido = int(ANO_t)
        HORA_vallido = int(HORA_t)
        format = "%d-%m-%Y"
        #test_str = fecha_t
        res = True
        # try:
        res = bool(datetime.strptime(fecha_t, format))
        # except ValueError:
            # res = False
        #demo = fecha_t
        #una_fecha = re.sub(r"^\s+|\s+$", "", demo) 
        #datetime.strptime(una_fecha, '%d-%m-%Y')
        FECHA_vallida = fecha_t
        #Cadenap = message.text
        fechahora = Cadenap[0:10] #str(FECHA_HORA)
        #print("   fecha " + Cadenap[0:10])
        #print("   hra: " + Cadenap[11:13])
        #hora = 
        #print(hora)
        #print("   dia mes año y hora" + fechahora[0:2] + "-" + fechahora[3:5] + "-" + fechahora[6:9] + " " + Cadenap[11:13])
        
        
        #demo = message.text
        #una_fecha = re.sub(r"^\s+|\s+$", "", demo) 
        FechaEnvio= FECHA_vallida #datetime.strptime(una_fecha, '%d-%m-%Y')
        #datetime.strptime(FechaEnvio, '%d-%m-%Y')
        FechaValida = "SI" ##print("Fecha v�lida")###while True:
        #horaxx = Cadenap[11:13]
        #hora = int(horaxx)
        #if HORA_vallido.isdigit:
        if HORA_vallido == 0: 
            HoraValida = "SI"
        else:
            if HORA_vallido < 24: 
                if HORA_vallido > 0: 
                    HoraValida = "SI"
                else:  
                    HoraValida = "NO"
                    markup = telebot.types.ForceReply()
                    msgP = bot.send_message(message.chat.id, " ¿ERROR debe ser una hora válida entre 0 y 23 : \n¿Cual es la fecha (dia-mes-año 31-12-2022), un espacio y luego la hora para enviar ahora las publicaciones que cumplan con esa configuración.", reply_markup=markup)
                    bot.register_next_step_handler(msgP, Send_lo_de_esta_fecha_horaF0)  

        hora = HORA_vallido #Cadenap[11:13]

        if hora > 9:
            HORAS = str(hora)
        else:
            HORAS = "0" + str(hora)
        if FechaValida == "SI":
            #if 
            clave1 = fechahora[0:2] + "-" + fechahora[3:5] + "-" + fechahora[6:10] + " " + HORAS
            linea = 0
            cx = 0
            Recorerlist_mensajes = []
            Lista_mensaje = []
            
            if HORA_UNICA == "00:00":
                with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
                    with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as fcanal:
                        canal_send = fcanal.readlines()
                        fcanal.seek(0)
                        ipgc = 0
                        for ipgc in range(len(canal_send)):
                            #Id_Canal_Send = canal_send[ipgc]
                            Linea_Canal_Send = canal_send[ipgc]
                            largo_Linea_Canal_Send = len(canal_send[ipgc])
                            provincia_send = Linea_Canal_Send[largo_Linea_Canal_Send-3:largo_Linea_Canal_Send]
                            Id_Canal_Send = Linea_Canal_Send[0:largo_Linea_Canal_Send-3]
                            LineasDefsched = fsched.readlines()
                            fsched.seek(0)
                            ik = 0
                            for ik in range(len(LineasDefsched)):
                                if clave1 in LineasDefsched[ik]:
                                    Lista_mensaje = LineasDefsched[ik-1]
                                    Tomar_Provincia = str(Recorerlist_SCHEDULE_x[2])
                                    Recorerlist_mensajes = eval(Lista_mensaje)
                                    iimsg = 0
                                    if Tomar_Provincia == "Tod" or Tomar_Provincia == provincia_send:
                                        for iimsg in Recorerlist_mensajes:
                                            #print(" " + iimsg)
                                            idCanal = int(Id_Canal_Send)
                                            Idmsg = int(iimsg)
                                            #print("   " + str(int(Id_Canal_Send)) + "  " + str(mi_chat_id) + " " + str(int(iimsg)))
                                            try:
                                                #msgP = bot.send_message(mi_chat_id, "  Mensajes: " + str(iimsg) + " Canal: " + str(Id_Canal_Send))
                                                msgP = bot.forward_message(idCanal, mi_chat_id, Idmsg)
                                                msgP = bot.send_message(mi_chat_id, "Mensage #: " + str(iimsg) + " enviado al canal:" + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
                                            except:
                                                msgP = bot.send_message(mi_chat_id, "ERROR: Mensage #: " + str(iimsg) + " NO enviado al canal:" + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
                    fcanal.close
                fsched.close
    except:
        #print("   dia mes año y hora" + fechahora[0:2] + "-" + fechahora[3:5] + "-" + fechahora[6:9] + " " + Cadenap[11:13])
        FechaValida = "NO"
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, " ¿ERROR debe ser una fecha válida, " + fecha_t + " DIA = " + Cadenap[0:2] + " MES = " + Cadenap[3:5] + " ANO = " + Cadenap[6:10] + " HORA = " + Cadenap[11:13] + ": \n¿Cual es la fecha (dia-mes-año 31-12-2022), un espacio y luego la hora para enviar ahora las publicaciones que cumplan con esa configuración.", reply_markup=markup)
        bot.register_next_step_handler(msgP, Send_lo_de_esta_fecha_horaF0)  


def eliminarconfiguracionF0(message):
    if message.text == "/abortar":
        ayuda1(message)
    else:
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Envíe su código para configuracion.", reply_markup=markup )
        bot.register_next_step_handler(msgP, eliminarconfiguracionF1)
def eliminarconfiguracionF1(message):
    if not message.text == "Tosim": 
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un código correcto. Inténtelo nuevamente, o /abortar para terminar.")
        bot.register_next_step_handler(msgP, eliminarconfiguracionF0) #si no es un número preguntar vecesXdias
    else:
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(mi_chat_id, "Envie el número de configuración que desea eliminar.", reply_markup=markup )
        bot.register_next_step_handler(msgP, preguntar_numero_configuracion_eliminar)
        
def preguntar_numero_configuracion_eliminar(message):
    ### poner aqui el codigo para eliminar publicaciones
    ## buscar en schedule la configuración según numero enviado·
    # eliminar fila donde esta, la siguiente con los mensajes, y la siguiente con el schedule
    # buscar como eliminar una fila en un txt que sería eliminar un elemento de una lista  
    linea = 0
    Encontrado = "No"
    try:
        clave4 = message.text
        Recorerlist_mensajes = []
        Lista_mensaje = []
        with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
            LineasDefsched = fsched.readlines()
            fsched.seek(0)
            LineasDefsched_fijo = fsched.readlines()
        fsched.close
        ik = 0
        for ik in range(len(LineasDefsched)):
            procede = "no"
            ListaDeMensajesAsociados = ""
            msgx = 0
            if ik == 0:
                procede = "si"
            if ik % 3 == 0:
                procede = "si"
            if procede == "si":  
                
                #for clave4 in LineasDefsched:
                if clave4 in LineasDefsched_fijo[ik]:
                    Encontrado = "Si"
                    #print("Si esta")
                    pos1 = str(LineasDefsched[ik])
                    pos2 = str(LineasDefsched[ik+1])
                    pos3 = str(LineasDefsched[ik+2])
                    
                    linea1 = LineasDefsched[ik]
                    linea2 = LineasDefsched[ik+1]
                    linea3 = LineasDefsched[ik+2]
                    
                    LineasDefsched.remove(linea1)
                    LineasDefsched.remove(linea2)
                    LineasDefsched.remove(linea3)
                    with open(path1 + "schedule.txt", 'w', encoding="utf8") as fsched:
                        #LineasDefsched = fsched.readlines()
                        #fsched.seek(0)
                        #print(str(LineasDefsched))
                        for lineaRestante in LineasDefsched:
                            fsched.write(lineaRestante) 
                    fsched.close    
                    bot.send_message(mi_chat_id, "El número de configuración: " + clave4 + " fue eliminado!, Envie el comndo /start 0 /alta para crer configuración nueva.")
                    
                    # clave4 = str(LineasDefsched[ik+1])
                    # s = str(LineasDefsched[ik])
                    # new_s = s.replace(clave4+ '\n', '')
                    # clave5 = str(LineasDefsched[ik+1])
                    # s = str(LineasDefsched[ik+1])
                    # new_s = s.replace(clave5+ '\n', '')
                    # clave6 = str(LineasDefsched[ik+2])
                    # s = str(LineasDefsched[ik+2])
                    # new_s = s.replace(clave6+ '\n', '')
                    # with open(path1 + "schedule.txt", 'w', encoding="utf8") as f:
                        # f.write(new_s)
                    # f.close
                #else:
                #print("No procede")
                #bot.send_message(mi_chat_id, "El número de configuración: " + clave4 + " fue eliminado!, Envie el comndo /start 0 /alta para crer configuración nueva.")
    except:
        bot.send_message(mi_chat_id, "El número de configuración: " + clave4 + " NO fue eliminado!, Envie el comndo /start 0 /alta para crer configuración nueva.")
    if Encontrado == "No":
        bot.send_message(mi_chat_id, "El número de configuración: " + clave4 + " NO fue encontrado!.")
# def borrarUnaLineaEnTXT():
    # with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
        # LineasDefsched = fsched.readlines()
        # fsched.seek(0)
    # fsched.close

    # pos = int(ik)
    # LineasDefsched = LineasDefsched[pos]
    # LineasDefsched.remove(LineasDefsched)
    # pos = int(ik+1)
    # LineasDefsched = LineasDefsched[pos]
    # LineasDefsched.remove(LineasDefsched)
    # pos = int(ik+1)
    # LineasDefsched = LineasDefsched[pos]
    # LineasDefsched.remove(LineasDefsched)
    # with open(path1 + "schedule.txt", 'w', encoding="utf8") as fsched:
        # LineasDefsched = fsched.readlines()
        # fsched.seek(0)
        # for linea in lineas:
           # fsched.write(linea) 
    # fsched.close    
 
 
  
        
def eliminarcanalF0(message):
    if message.text == "/abortar":
        ayuda1(message)
    else:
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Envíe su código para eliminarcanal.", reply_markup=markup )
        bot.register_next_step_handler(msgP, eliminarcanalF1)
def eliminarcanalF1(message):
    if not message.text == "Tosim": 
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un código correcto. Inténtelo nuevamente, o /abortar para terminar")
        bot.register_next_step_handler(msgP, eliminarcanalF0) #si no es un número preguntar vecesXdias
    else:
        #PersonaGrupoCanal.txt
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(mi_chat_id, "Envie el número de persona, Grupo o Canal para eliminarlo.", reply_markup=markup )
        bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_eliminar)          

def preguntar_persona_Grupo_Canal_eliminar(message):
    linea = 0
    try:
        with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
            LineasDeF4 = f4.read()
            f4.close
            s = str(LineasDeF4)
            clave1 = message.text
            print("   clave:" + clave1 + ":")
            #s = "Naze
            new_s = s.replace(clave1+ '\n', '')
            with open(path1 + "PersonaGrupoCanal.txt", 'w', encoding="utf8") as f:
                f.write(new_s)
                f.close
                with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
                    LineasDeF41 = f4.read()
                f4.close
                vgvg = mostrarcanal(message)
        bot.send_message(mi_chat_id, "El número de persona, Grupo o Canal: " + clave1 + " fue eliminado!, Envie el comndo /start 0 /alta para crer configuración nueva.")
    except:
        bot.send_message(mi_chat_id, "El número de persona, Grupo o Canal: " + clave1 + " NO fue eliminado!, Envie el comndo /start 0 /alta para crer configuración nueva.")

        
def bajartxtF0(message):
    if message.text == "/abortar":
        ayuda1(message)
    else:
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Envíe su código de bajartxt.", reply_markup=markup )
        bot.register_next_step_handler(msgP, bajartxtF1)
def bajartxtF1(message):
    if not message.text == "Tosim": 
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un código correcto. Inténtelo nuevamente, o /abortar para terminar")
        bot.register_next_step_handler(msgP, bajartxtF0) #si no es un número preguntar vecesXdias
    else:
        files1 = ['mensaje.txt', 'configuraciones.txt','schedule.txt', 'schedule_temp.txt', 'schedule_schedule.txt', 'PersonaGrupoCanal.txt', 'botlistcanal.py']
        for file1 in files1:
            try:
                if open(path1 + file1 , 'rb'):
                    file11 = open(path1 + file1, 'rb')
                    bot.send_document(mi_chat_id, file11)
                    file11.close
                else:
                    NoAbre = 0
                    bot.send_message(mi_chat_id, "Archivos no abre!."  + file1)
            except:
                bot.send_message(mi_chat_id, "Archivos no descargado."  + file1)
        bot.send_message(mi_chat_id, "Archivos descargados, Envie el comndo /start ó /alta para crer configuración nueva.")
        
def resetF0(message):
    if message.text == "/abortar":
        ayuda1(message)
    else:
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Envíe su código de RESET.", reply_markup=markup )
        bot.register_next_step_handler(msgP, resetF1)
def resetF1(message):
    if not message.text == "Tosim": 
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un código correcto. Inténtelo nuevamente, o /abortar para terminar.")
        bot.register_next_step_handler(msgP, resetF0) #si no es un número preguntar vecesXdias
    else:
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
        bot.send_message(mi_chat_id, "Sistema reseteado, Envie el comndo /start 0 /alta para crer configuración nueva.")   
        
        
        
def preguntar_hora_de_envioPaso1(message): 
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(mi_chat_id, "Envie la hora y los minutos a los que desea se envien por unica vez las publicaciones.", reply_markup=markup )
        bot.register_next_step_handler(msgP, preguntar_hora_de_envioPaso2)
def preguntar_hora_de_envioPaso2(message):
    cde = 0
        # si el dato enviado tiene en los dos primeros digitos un numero entre 0-23
        # si el dato enviado tiene en los dos ultimos digitos un numero entre 0-59
        # validar el formato, si no preguntar nuevamente
        # luego activar schedule con la nueva hora, se debe estudiar esto
       
        
        
        

        
def mostrarcanal(message):
    with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f4:
        LineasDeF4 = f4.read()
        f4.close
    bot.send_message(mi_chat_id, "Lista de Personas Grupos o Canales: " + str(LineasDeF4))


def preguntar_persona_Grupo_Canal_agregar(message):
    markup = telebot.types.ForceReply()
    msgP = bot.send_message(mi_chat_id, "Envie el número de persona, Grupo o Canal, luego spacio y la sigla de la provinca (Hol, Pri, Art, Hab, May, Mat, Cif, Isl, Vic, Ssp, Cav, Cam, Ltu, Grm, Gut, Scu, Tod) para agregarlo.", reply_markup=markup )
    bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_agregar_PROVINCIA)

# def preguntar_persona_Grupo_Canal_agregar_CANAL(message):
    # Agregarlo = message.text
    # # persona_grupo_canal = message.text
    # # if persona_grupo_canal[0:0] == "-":
        # # canal = -1 * int(persona_grupo_canal)
        # # Agregarlo = canal
    # # else:
        # # persona_grupo = int(persona_grupo_canal)
        # # Agregarlo = persona_grupo
    # markup = telebot.types.ForceReply()
    # msgP = bot.send_message(mi_chat_id, "Envie la sigla (Hol, Pri, Art, Hab, May, Mat, Cif, Isl, Vic, Ssp, Cav, Cam, Ltu, Grm, Gut, Scu, Tod) de la PROVINCIA a que pertenece el Grupo, canal o persona.", reply_markup=markup )
    # bot.register_next_step_handler(msgP, preguntar_persona_Grupo_Canal_agregar_PROVINCIA)        

        
def preguntar_persona_Grupo_Canal_agregar_PROVINCIA(message):        
    Linea_Canal_provincia = message.text
    largo_Linea_Canal_provincia = len(Linea_Canal_provincia)
    provinc = Linea_Canal_provincia[largo_Linea_Canal_provincia-3:largo_Linea_Canal_provincia]
    Id_Canal = Linea_Canal_provincia[0:largo_Linea_Canal_provincia-3]
 
    okkk = "no"
    if provinc in ["Hol", "Pri", "Art", "Hab", "May", "Mat", "Cif", "Isl", "Vic", "Ssp", "Cav", "Cam", "Ltu", "Grm", "Gut", "Scu", "Tod"]:
        okkk = "si"
    if okkk == "no":  
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Envie el número de persona, Grupo o Canal, luego spacio y la sigla de la provinca (Hol, Pri, Art, Hab, May, Mat, Cif, Isl, Vic, Ssp, Cav, Cam, Ltu, Grm, Gut, Scu, Tod) para agregarlo.\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)  
    else:    
        with open(path1 + "PersonaGrupoCanal.txt", 'a', encoding="utf8") as f:
            f.write(str(Id_Canal) + ' ' + str(provinc) + '\n')
        f.close
        with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as f:
            canales = f.read()
        f.close
        bot.send_message(mi_chat_id, "Se agregó a la lista de Personas Grupos o Canales: " + str(canales))




def report():
    wwwww = ""
    HORA_UNICA = "00:00"
    wwwww = report1(HORA_UNICA)
    
def report1(HORA_UNICA):    
    #w = datetime.now()
    #if message.text == "1":
    now = datetime.now()
    today = date.today()
    #print("  hora unica ok" + HORA_UNICA)
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
    
    linea = 0
    cx = 0
    
    Recorerlist_mensajes = []
    Lista_mensaje = []
    if HORA_UNICA == "00:00":
        with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
            with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as fcanal:
                canal_send = fcanal.readlines()
                #Lista_canal_provincia_send = eval(canal_send)
                fcanal.seek(0)
                ipgc = 0
                for ipgc in range(len(canal_send)):
                    Linea_Canal_Send = canal_send[ipgc]
                    largo_Linea_Canal_Send = len(canal_send[ipgc])
                    provincia_send = Linea_Canal_Send[largo_Linea_Canal_Send-3:largo_Linea_Canal_Send]
                    Id_Canal_Send = Linea_Canal_Send[0:largo_Linea_Canal_Send-3]
                    LineasDefsched = fsched.readlines()
                    fsched.seek(0)
                    ik = 0
                    for ik in range(len(LineasDefsched)):
                        if clave1 in LineasDefsched[ik]:
                            Recorerlist_SCHEDULE = LineasDefsched[ik-2]
                            Recorerlist_SCHEDULE_x = eval(Recorerlist_SCHEDULE)
                            Tomar_Provincia = str(Recorerlist_SCHEDULE_x[2])
                            Tomar_Sleep = str(Recorerlist_SCHEDULE_x[4])
                            Tomar_SleepX = int(Tomar_Sleep)
                            Lista_mensaje = LineasDefsched[ik-1]
                            Recorerlist_mensajes = eval(Lista_mensaje)
                            iimsg = 0
                            if Tomar_Provincia == "Tod" or Tomar_Provincia == provincia_send:
                                for iimsg in Recorerlist_mensajes:
                                    #print(" " + iimsg)
                                    idCanal = int(Id_Canal_Send)
                                    Idmsg = int(iimsg)
                                    #print("   " + str(int(Id_Canal_Send)) + "  " + str(mi_chat_id) + " " + str(int(iimsg)))
                                    try:
                                        #msgP = bot.send_message(mi_chat_id, "  Mensajes: " + str(iimsg) + " Canal: " + str(Id_Canal_Send))
                                        msgP = bot.forward_message(idCanal, mi_chat_id, Idmsg)
                                        msgP = bot.send_message(mi_chat_id, "Mensage #: " + str(iimsg) + " enviado al canal:" + str(Id_Canal_Send)  + " Provincia:" + str(provincia_send))
                                        sleep(Tomar_SleepX)
                                    except:
                                        msgP = bot.send_message(mi_chat_id, "ERROR: Mensage #: " + str(iimsg) + " NO enviado al canal:" + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
                                   
            fcanal.close
        fsched.close
    if HORA_UNICA == "99:99":
        with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
            with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as fcanal:
                canal_send = fcanal.readlines()
                fcanal.seek(0)
                ipgc = 0
                for ipgc in range(len(canal_send)):
                    #Id_Canal_Send = canal_send[ipgc]
                    Linea_Canal_Send = canal_send[ipgc]
                    largo_Linea_Canal_Send = len(canal_send[ipgc])
                    provincia_send = Linea_Canal_Send[largo_Linea_Canal_Send-3:largo_Linea_Canal_Send]
                    Id_Canal_Send = Linea_Canal_Send[0:largo_Linea_Canal_Send-3]
                    
                    LineasDefsched = fsched.readlines()
                    fsched.seek(0)
                    ik = 0
                    #for ik in range(len(LineasDefsched)):
                    #if clave1 in LineasDefsched[ik]:
                    # Lista_mensaje = LineasDefsched[0]
                    # Recorerlist_mensajes = eval(Lista_mensaje)
                    Recorerlist_SCHEDULE = LineasDefsched[0]
                    Recorerlist_SCHEDULE_x = eval(Recorerlist_SCHEDULE)
                    Tomar_Provincia = str(Recorerlist_SCHEDULE_x[2])
                    Tomar_Sleep = str(Recorerlist_SCHEDULE_x[4])
                    Tomar_SleepX = int(Tomar_Sleep)
                    Tomar_Provincia = str(Recorerlist_SCHEDULE_x[2])

                    Lista_mensaje = LineasDefsched[1]
                    Recorerlist_mensajes = eval(Lista_mensaje)
                    iimsg = 0
                    if Tomar_Provincia == "Tod" or Tomar_Provincia == provincia_send:
                        for iimsg in Recorerlist_mensajes:
                            #print(" " + iimsg)
                            idCanal = int(Id_Canal_Send)
                            Idmsg = int(iimsg)
                            #print("   " + str(int(Id_Canal_Send)) + "  " + str(mi_chat_id) + " " + str(int(iimsg)))
                            try:
                                msgP = bot.send_message(mi_chat_id, "  Mensajes: " + str(iimsg) + " Canal: " + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
                                msgP = bot.forward_message(idCanal, mi_chat_id, Idmsg)
                                msgP = bot.send_message(mi_chat_id, "Mensage #: " + str(iimsg) + " enviado al canal:" + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
                                sleep(Tomar_SleepX)
                            except:
                                msgP = bot.send_message(mi_chat_id, "ERROR: Mensage #: " + str(iimsg) + " NO enviado al canal:" + str(Id_Canal_Send) + " Provincia:" + str(provincia_send))
            fcanal.close
        fsched.close
def verconfiguraciones(message):
    msg_mostrarX = bot.send_message(mi_chat_id, "Pediste entrar a /verconfig .")
    Recorerlist_mensajes = []
    Lista_mensaje = []
    ListaDeMensajesAsociados = ""
    with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
        LineasDefsched = fsched.readlines()
        fsched.seek(0)
        configuraciones = {  }
        configuraciones[mi_chat_id] = {  } 
        ik = 0
        for ik in range(len(LineasDefsched)):
            procede = "no"
            ListaDeMensajesAsociados = ""
            Lista_mensajeM = []
            Recorerlist_mensajesM = []
            msgx = 0
            if ik == 0:
                procede = "si"
            if ik % 3 == 0:
                procede = "si"
            if procede == "si":
                Lista_mensajeM = LineasDefsched[ik+1] 
                Recorerlist_mensajesM = eval(Lista_mensajeM)
                for msgx in range(len(Recorerlist_mensajesM)):
                    if msgx == 0:
                        ListaDeMensajesAsociados+= '\n /idmsg' + str(Recorerlist_mensajesM[msgx] + ' ')
                        #bot.send_message(mi_chat_id, str(ListaDeMensajesAsociados) + '\n' + str(Recorerlist_mensajesM), parse_mode="HTML")
                    else: 
                        ListaDeMensajesAsociados+=  '/idmsg' +str(Recorerlist_mensajesM[msgx] + ' ')
                        #bot.send_message(mi_chat_id, str(ListaDeMensajesAsociados) + '\n' + str(Recorerlist_mensajesM), parse_mode="HTML")
                Lista_mensaje = LineasDefsched[ik]
                Recorerlist_mensajes = eval(Lista_mensaje)
                ##print("  lista leida:" + str(Recorerlist_mensajes))
                configuraciones[mi_chat_id]["nombreCliente"] = Recorerlist_mensajes[0]
                configuraciones[mi_chat_id]["nombreGestorCliente"] = Recorerlist_mensajes[1]
                configuraciones[mi_chat_id]["provincia"] = Recorerlist_mensajes[2]
                configuraciones[mi_chat_id]["VecesXdia"] = Recorerlist_mensajes[3]
                configuraciones[mi_chat_id]["TiempoEntreMensajes"] = Recorerlist_mensajes[4]
                configuraciones[mi_chat_id]["HoraInicio"] = Recorerlist_mensajes[5]
                configuraciones[mi_chat_id]["FechaInicio"] = Recorerlist_mensajes[6]
                configuraciones[mi_chat_id]["FechaFin"] = Recorerlist_mensajes[7]
                configuraciones[mi_chat_id]["Numero"] = Recorerlist_mensajes[8]
                configuraciones[mi_chat_id]["IDMensaje"] = ListaDeMensajesAsociados
                texto = 'Configuración:\n'
                texto+= f'<code>NombreCliente:</code> {configuraciones[mi_chat_id]["nombreCliente"]}'
                texto+= f'<code>NombreGestor.:</code> {configuraciones[mi_chat_id]["nombreGestorCliente"]}'
                texto+= f'<code>Provincia....:</code> {configuraciones[mi_chat_id]["provincia"]}'
                texto+= f'<code>Veces x día..:</code> {configuraciones[mi_chat_id]["VecesXdia"]}'
                texto+= f'<code>Tiempo/Mensje:</code> {configuraciones[mi_chat_id]["TiempoEntreMensajes"]}'
                texto+= f'<code>Hora Inicio..:</code> {configuraciones[mi_chat_id]["HoraInicio"]}'
                texto+= f'<code>FechaInicio..:</code> {configuraciones[mi_chat_id]["FechaInicio"]}'
                texto+= f'<code>FechaFin.....:</code> {configuraciones[mi_chat_id]["FechaFin"]}'
                texto+= f'<code>NumeroCong...:</code> {configuraciones[mi_chat_id]["Numero"]}'
                texto+= f'<code>ID Mensajes..:</code> {configuraciones[mi_chat_id]["IDMensaje"]}'
                
                msg_mostrarX = bot.send_message(mi_chat_id, texto, parse_mode="HTML")
                ListaDeMensajesAsociados = ""
    fsched.close


def Id_MSG_numero(message):
    Idmsg = 1
    try: #idmsg
        Idmsg = int(message.text[6:])
        msgP = bot.forward_message(mi_chat_id, mi_chat_id, Idmsg)
        # encontrado1 = "SI"
    except:
        msgP = bot.send_message(mi_chat_id, "Mensaje número: " + message.text[6:] + ", NO encontrado!")
def report_fecha_vence(message):
    msg_mostrarX = bot.send_message(mi_chat_id, "Pediste entrar a /venceconfig.. ")
    current1 = datetime.now()
    tomorrow1 = timedelta(4) #######################################
    vence1 = current1 + tomorrow1
    DIA_v = str(vence1.day)
    # if vence1.day > 9:
        # DIA_v = str(vence1.day)
    # else:
        # DIA_v = "0" + str(vence1.day)
    #MESC = int(today.month)
    MES_v = str(vence1.month)
    # if vence1.month > 9:
        # MES_v = str(vence1.month)
    # else:
        # MES_v = "0" + str(vence1.month)
    clave_vencimiento = str(DIA_v) + "-" + str(MES_v) + "-" + str(vence1.year) #+ " " + str(horaa)  
    Recorerlist_mensajes = []
    Lista_mensaje = []
    #if HORA_UNICA == "00:00":
    with open(path1 + "schedule.txt", 'r', encoding="utf8") as fsched:
        LineasDefsched = fsched.readlines()
        fsched.seek(0)
        #with open(path1 + "PersonaGrupoCanal.txt", 'r', encoding="utf8") as fcanal:
        configuraciones = {  }
        configuraciones[mi_chat_id] = {  } 
        # for h24 in range(23):
            # HH = " " + str(h24)
            # # if h24 < 10:
                # # HH = " 0" + str(h24)
            # # else:
                # # HH = " " + str(h24)
            # clave_vencimientoH = clave_vencimiento + HH
            # ik = 0
        for ik in range(len(LineasDefsched)):
            procede = "no"
            if ik == 0:
                procede = "si"
            if ik % 3 == 0:
                procede = "si"
            if procede == "si":
                Lista_mensaje = LineasDefsched[ik]
                Recorerlist_mensajes = eval(Lista_mensaje)
                #print(Recorerlist_mensajes)
                #for ip in range(7):
                #print("  ik: " + str(ik) + "  dato: " + str(Recorerlist_mensajes[ik]))
                #
                #print("   creado: " + clave_vencimiento + " guardado: " + str(Recorerlist_mensajes[6]))
                if clave_vencimiento in str(Recorerlist_mensajes[7]):
                    #print("############   creado: " + clave_vencimiento + " guardado: " + str(Recorerlist_mensajes[6]))
                    configuraciones[mi_chat_id]["nombreCliente"] = Recorerlist_mensajes[0]
                    configuraciones[mi_chat_id]["nombreGestorCliente"] = Recorerlist_mensajes[1]
                    configuraciones[mi_chat_id]["provincia"] = Recorerlist_mensajes[2]
                    configuraciones[mi_chat_id]["VecesXdia"] = Recorerlist_mensajes[3]
                    configuraciones[mi_chat_id]["TiempoEntreMensajes"] = Recorerlist_mensajes[4]
                    configuraciones[mi_chat_id]["HoraInicio"] = Recorerlist_mensajes[5]
                    configuraciones[mi_chat_id]["FechaInicio"] = Recorerlist_mensajes[6]
                    configuraciones[mi_chat_id]["FechaFin"] = Recorerlist_mensajes[7]
                    configuraciones[mi_chat_id]["Numero"] = Recorerlist_mensajes[8]
                    texto = 'Esta Configuración vence en tres días:\n'
                    texto+= f'<code>NombreCliente:</code> {configuraciones[mi_chat_id]["nombreCliente"]}'
                    texto+= f'<code>NombreGestor.:</code> {configuraciones[mi_chat_id]["nombreGestorCliente"]}'
                    texto+= f'<code>Provincia....:</code> {configuraciones[mi_chat_id]["provincia"]}'
                    texto+= f'<code>Veces x día..:</code> {configuraciones[mi_chat_id]["VecesXdia"]}'
                    texto+= f'<code>Tiempo/Mensje:</code> {configuraciones[mi_chat_id]["TiempoEntreMensajes"]}'
                    texto+= f'<code>Hora Inicio..:</code> {configuraciones[mi_chat_id]["HoraInicio"]}'
                    texto+= f'<code>FechaInicio..:</code> {configuraciones[mi_chat_id]["FechaInicio"]}'
                    texto+= f'<code>FechaFin.....:</code> {configuraciones[mi_chat_id]["FechaFin"]}'
                    texto+= f'<code>FechaFin.....:</code> {configuraciones[mi_chat_id]["Numero"]}'
                    msg_mostrarX = bot.send_message(mi_chat_id, texto, parse_mode="HTML")
                    msg_mostrarX = bot.send_message(mi_chat_id, Recorerlist_mensajes[8])
                #ik+= 2
    fsched.close

        
#####################################################################################################################################         
#####################################################################################################################################            
##################################################################################################################################### 
     
@bot.message_handler(content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "pinned_message"])
def cmd_otro1(message):
    Correr_def = cmd_publicar(message)

    
#####################################################################################################################################         
#####################################################################################################################################            
##################################################################################################################################### 

# @bot.message_handler(commands=['publicar'])#, 'help', 'ayuda']) /publicar
def cmd_publicar(message):
    #if message.text == '/publicar':
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
        bot.send_message(message.chat.id, "Use comandos\n /publicar o /finalizar para guardar schedule.")
        
        # cccc programar finalizar
    else:
        bot.send_message(message.chat.id, "Publicar: Use los comandos\n /start , /publicar , /alta , /reset , /ayuda o /help ")    	

def cmd_ayuda(message):
	textoAyuda = 'Auda:\n'
	textoAyuda+= f'Usa comando /alta para introducir tus datos\n'
	textoAyuda+= f'Usa comando /ayuda o /help para obtener ayuda\n'
	textoAyuda+= f'Usa comando /start para iniciar el bot\n'
	bot.send_message(message.chat.id, textoAyuda, parse_mode="HTML")
def cmd_start(message):

    xxx = MostrarUltimaConfiguracionDesde_txt(message)
    bot.send_message(message.chat.id, "Envie las publicaciones que desea tengan la última configuracin mostrada anteriormente. \nPara una nueva configuracin envie el comando /alta .")
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
    #entro en el mensaje el nombre del cliente
    configuraciones[message.chat.id] = {  }
    configuraciones[message.chat.id]["nombreCliente"] = ""
    configuraciones[message.chat.id]["nombreCliente"] = message.text
    configuraciones[message.chat.id]["nombreGestorCliente"] = ""
    configuraciones[message.chat.id]["provincia"] = ""
    configuraciones[message.chat.id]["VecesXdia"] = ""
    configuraciones[message.chat.id]["TiempoEntreMensajes"] = ""
    configuraciones[message.chat.id]["HoraInicio"] = ""
    configuraciones[message.chat.id]["FechaInicio"] = ""
    configuraciones[message.chat.id]["FechaFin"] = ""
    mmm = mostrar_datos(message)
    # preguntar el por nombre del Gestor del este Cliente
    ##      PEDIR "GESTOR" ESTADO = "CONFIGURACIONES CLIENTE"   ######################################################################
    markup = telebot.types.ForceReply()
    msgP = bot.send_message(message.chat.id, "Nombre del Gestor de este Cliente.\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup )
    bot.register_next_step_handler(msgP, preguntar_Provincia)
def preguntar_Provincia(message):
    #entro en el mensaje el nombre del cliente
	# configuraciones[message.chat.id] = {  }
	# configuraciones[message.chat.id]["nombreCliente"] = ""
	# configuraciones[message.chat.id]["nombreCliente"] = ""
	configuraciones[message.chat.id]["nombreGestorCliente"] = message.text
    # configuraciones[message.chat.id]["provincia"] = ""
	# configuraciones[message.chat.id]["VecesXdia"] = ""
	# configuraciones[message.chat.id]["TiempoEntreMensajes"] = ""
	# configuraciones[message.chat.id]["HoraInicio"] = ""
	# configuraciones[message.chat.id]["FechaInicio"] = ""
	# configuraciones[message.chat.id]["FechaFin"] = ""
	mmm = mostrar_datos(message)
	# preguntar el por nombre del Gestor del este Cliente
    ##      PEDIR "GESTOR" ESTADO = "CONFIGURACIONES CLIENTE"   ######################################################################
	markup = telebot.types.ForceReply()
	msgP = bot.send_message(message.chat.id, "Siglas de la provincia (Hol, Pri, Art, Hab, May, Mat, Cif, Isl, Vic, Ssp, Cav, Cam, Ltu, Grm, Gut, Scu, Tod).\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup )
	bot.register_next_step_handler(msgP, preguntar_veces_x_dia)    
def preguntar_veces_x_dia(message):
    #entro nombre del Gestor
    #o: Holguin, p: Pinar del Rio, a: artemisa, h: Habana, my: Mayabeque, mt: Matanzas, cf: Cien Fuegos, i: Isla de la #Juventud, v: Villa Clara, ss: Santis Spiritus, cv: Ciego de Avila, cm: Camaguey, lt: Las Tunas, grm: Gramna, gu: #Guantanamo, sc: Santiago de Cuba
    provinc = message.text
    okkk = "no"
    if provinc in ["Hol", "Pri", "Art", "Hab", "May", "Mat", "Cif", "Isl", "Vic", "Ssp", "Cav", "Cam", "Ltu", "Grm", "Gut", "Scu", "Tod"]:
        okkk = "si"
    if okkk == "no":  
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "Siglas de la provincia (Hol, Pri, Art, Hab, May, Mat, Cif, Isl, Vic, Ssp, Cav, Cam, Ltu, Grm, Gut, Scu, Tod).\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_veces_x_dia)
    else:
        configuraciones[message.chat.id]["provincia"] = message.text
        print("  prov: " + provinc)
        ##      PEDIR "VECES_X_DIA" ESTADO = "CONFIGURACIONES GESTOR"   ######################################################################
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cuantas veces por día desea repetir la publicación?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_tiempo_entre_cada_mensajes)
    
def preguntar_tiempo_entre_cada_mensajes(message):
    #entro vecesXdias
	# preguntar si vecesXdias introducida no es un numero
    if not message.text.isdigit(): ## es verdadero si es un numero
		# informamos del error y volvemos a preguntar
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un número. \n¿Cuantas veces por día desea repetir la publicación?\nPara cancela Conf. actual envie /cancelconfig ")
        bot.register_next_step_handler(msgP, preguntar_tiempo_entre_cada_mensajes) #si no es un número preguntar vecesXdias
    else: #  si se introdujo el numero correcto tomo veces_x_dia
        configuraciones[message.chat.id]["VecesXdia"] = int(message.text)
        ##      PEDIR "HORA_INICIO" ESTADO = "CONFIGURACIONES VECES_X_DIA"   ######################################################################
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Que intervalo de tiempo desea entre publicacioes consecutivas?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_hora_inicio) # al  ser un numero pregunto    
    
def preguntar_hora_inicio(message):
    #entro vecesXdias
	# preguntar si vecesXdias introducida no es un numero
    if not message.text.isdigit(): ## es verdadero si es un numero
		# informamos del error y volvemos a preguntar
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un número. \n¿Que intervalo de tiempo (en segundos) desea entre publicacioes consecutivas?\nPara cancela Conf. actual envie /cancelconfig ")
        bot.register_next_step_handler(msgP, preguntar_hora_inicio) #si no es un número preguntar vecesXdias
    else: #  si se introdujo el numero correcto tomo veces_x_dia
        configuraciones[message.chat.id]["TiempoEntreMensajes"] = int(message.text)
        ##      PEDIR "HORA_INICIO" ESTADO = "CONFIGURACIONES VECES_X_DIA"   ######################################################################
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la hora a la que desea se inicien las repeticiones?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_fecha_inicio) # al  ser un numero pregunto 

def preguntar_fecha_inicio(message):
    # preguntar por si la hora inicio introducida no es un numero
    if not message.text.isdigit(): ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        ##      PEDIR "HORA_INICIO" ESTADO = "CONFIGURACIONES VECES_X_DIA"   ###############
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "ERROR: Debes indicar un número. \n¿Cual es la hora a la que desea se inicien las repeticiones?", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_fecha_inicio)
        msgX_id3 = msgP.message_id
    else: #  si se introdujo el numero correcto veces_x_dia
        configuraciones[message.chat.id]["HoraInicio"] = int(message.text)
        mmm = mostrar_datos(message)
        ##      PEDIR "FECHA_INICIO" ESTADO = "CONFIGURACIONES HORA_INICIO"   ###############
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha (dia-mes-año) en que iniciar las repeticiones?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, preguntar_fecha_fin)
        
def preguntar_fecha_fin(message):
    #entro la fecha de inicio
    # preguntar por si la fecha inicio introducida no es valida
    FechaValida = "NO"
    try:
        fecha = message.text
        datetime.strptime(fecha, '%d-%m-%Y')
        FechaValida = "SI" ##print("Fecha v�lida")###while True:
    except:
        FechaValida = "NO"
    if FechaValida == "NO": ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        ##      PEDIR "FECHA_INICIO" ESTADO = "CONFIGURACIONES HORA_INICIO"   ###############
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿ERROR debe ser una fecha válida: \n¿Cual es la fecha (dia-mes-año 31-12-2022) en que iniciar las repeticiones?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        # volver a ejecutar la función
        bot.register_next_step_handler(msgP, preguntar_fecha_fin)
    else: #  si se introdujo la fecha valida 
        configuraciones[message.chat.id]["FechaInicio"] = message.text
        ##nombreCliente = message.text
        ##      PEDIR "FECHA_FIN" ESTADO = "CONFIGURACIONES FECHA_INICIO"   ###############
        mmm = mostrar_datos(message)
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha en que terminan las repeticiones?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        bot.register_next_step_handler(msgP, Validar_datos_de_publicaciones)

def Validar_datos_de_publicaciones(message):
    #entró la fecha de FechaInicio
    # preguntar por si la fecha inicio introducida no es valida
    FechaValida = "NO"
    try:
        fecha = message.text
        datetime.strptime(fecha, '%d-%m-%Y')
        FechaValida = "SI" 
    except:
        FechaValida = "NO"

    if FechaValida == "NO": ## es verdadero si es un n�mero
        # informamos del error y volvemos a preguntar
        markup = telebot.types.ForceReply()
        msgP = bot.send_message(message.chat.id, "¿Cual es la fecha en que terminan las repeticiones?\nPara cancela Conf. actual envie /cancelconfig ", reply_markup=markup)
        # volver a ejecutar la funci�n
        bot.register_next_step_handler(msgP, Validar_datos_de_publicaciones)
    else: #  si se introdujo la fecha valida 
        
        configuraciones[message.chat.id]["FechaFin"] = message.text
        texto = f'{configuraciones[message.chat.id]["nombreCliente"]}\n'
        texto+= f'{configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
        texto+= f'{configuraciones[message.chat.id]["provincia"]}\n'
        texto+= f'{configuraciones[message.chat.id]["VecesXdia"]}\n'
        texto+= f'{configuraciones[message.chat.id]["TiempoEntreMensajes"]}\n'
        texto+= f'{configuraciones[message.chat.id]["HoraInicio"]}\n'
        texto+= f'{configuraciones[message.chat.id]["FechaInicio"]}\n'
        texto+= f'{configuraciones[message.chat.id]["FechaFin"]}\n'
        #texto+= f'{configuraciones[message.chat.id]["Numero"]}\n'
        with open('configuraciones.txt','w') as f:
            f.write(texto)
        f.close
        xxx = MostrarUltimaConfiguracionDesde_txt(message)
        xxx1 = guardar_mensaje_nuevo("")
        bot.send_message(message.chat.id, "Se guardó correctamente la configuración. Utilice el comando /publicar para asociar publicaciones a esta configuración.\nPara cancela Conf. actual envie /cancelconfig ")                    


def mostrar_datos(message):
    try:
        ##bot.delete_message(message.chat.id, msg_mostrar)
        markup = telebot.types.ForceReply()
        texto = 'Datos introducios:\n'
        texto+= f'<code>NombreCliente:</code> {configuraciones[message.chat.id]["nombreCliente"]}\n'
        texto+= f'<code>NombreGestor.:</code> {configuraciones[message.chat.id]["nombreGestorCliente"]}\n'
        texto+= f'<code>Provincia....:</code> {configuraciones[message.chat.id]["provincia"]}\n'
        texto+= f'<code>Veces x día..:</code> {configuraciones[message.chat.id]["VecesXdia"]}\n'
        texto+= f'<code>Tiempo/Mensje:</code> {configuraciones[message.chat.id]["TiempoEntreMensajes"]}\n'
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
    Cerrores = 0
    with open(path1 + 'configuraciones.txt','r') as f:
        textom = f.readlines()
    f.close
    #return texto
    configuraciones = {  }
    configuraciones[mensaje.chat.id] = {  } 
    texto = 'Datos introducios:\n'
    try: 
        configuraciones[mensaje.chat.id]["nombreCliente"] = textom[0]
        #print(textom[0])
        if textom[0]=="":Cerrores+= 1  
        texto+= f'<code>NombreCliente:</code> {configuraciones[mensaje.chat.id]["nombreCliente"]}'
    except: 
        Cerrores+= 1 #"Orge" 
    try: 
        configuraciones[mensaje.chat.id]["nombreGestorCliente"] = textom[1]
        #print(textom[1])
        if textom[1]=="":Cerrores+= 1
        texto+= f'<code>NombreGestor.:</code> {configuraciones[mensaje.chat.id]["nombreGestorCliente"]}'
    except: 
        Cerrores+= 1 #"Orge G"
    try: 
        configuraciones[mensaje.chat.id]["provincia"] = textom[2]
        #print(textom[1])
        if textom[2]=="":Cerrores+= 1
        texto+= f'<code>Provincia....:</code> {configuraciones[mensaje.chat.id]["provincia"]}'
    except: 
        Cerrores+= 1 #"Orge G"
    try: 
        configuraciones[mensaje.chat.id]["VecesXdia"] = textom[3]
        #print(textom[2])
        if textom[3]=="":Cerrores+= 1
        texto+= f'<code>Veces x día..:</code> {configuraciones[mensaje.chat.id]["VecesXdia"]}'
    except: 
        Cerrores+= 1#"6"
    try: 
        configuraciones[mensaje.chat.id]["TiempoEntreMensajes"] = textom[4] 
        #print(textom[3])
        if textom[4]=="":Cerrores+= 1
        texto+= f'<code>Tiempo/Mensje:</code> {configuraciones[mensaje.chat.id]["TiempoEntreMensajes"]}'
    except: 
        Cerrores+= 1 #"6"
    try: 
        configuraciones[mensaje.chat.id]["HoraInicio"] = textom[5]
        #print(textom[4])
        if textom[5]=="":Cerrores+= 1
        texto+= f'<code>Hora Inicio..:</code> {configuraciones[mensaje.chat.id]["HoraInicio"]}'
    except: 
        Cerrores+= 1 #"7"
    try: 
        configuraciones[mensaje.chat.id]["FechaInicio"] = textom[6]
        #print(textom[5])
        if textom[6]=="":Cerrores+= 1
        texto+= f'<code>FechaInicio..:</code> {configuraciones[mensaje.chat.id]["FechaInicio"]}'
    except: 
        Cerrores+= 1 #"06-06-2022"
    try: 
        configuraciones[mensaje.chat.id]["FechaFin"] = textom[7]
        #print(textom[6])
        if textom[7]=="":Cerrores+= 1
        texto+= f'<code>FechaFin.....:</code> {configuraciones[mensaje.chat.id]["FechaFin"]}'
    except: 
        Cerrores+= 1 #"07-06-2022"
    if Cerrores == 0:
        mensaje = bot.send_message(mensaje.chat.id, texto, parse_mode="HTML")
    else:
        mensaje = bot.send_message(mensaje.chat.id, "Use el comando /alta para hacer nuevas configuraciones, o los comandos /ayuda o /help para obtener ayuda.", parse_mode="HTML")

    return mensaje

# def Delete_msg_send(msg_id_parametro):
	# try:
		# bot.delete_message(message.chat.id, msg_id_parametro)
	# except:
		# pq = 1
##//////////////////////----------'zzzz///////////////////////////////////'
##/nueva
#def Guardar_txt_Conf(message):

def crear_y_guardar_schedule_temp(message):
    lines = ["yuy", "234", "2343"]
    with open(path1 + "configuraciones.txt", 'r', encoding="utf8") as f1:
        lines = f1.readlines()
        #lines = [line.replace(r'\n', ' ').replace(r'\r', '') for line in lines]
    f1.close

    i = 0
    listasR0 = ""
    nombreCliente = ""
    nombreGestorCliente = ""
    provincia = ""    
    VecesXdia = 0
    TiempoEntreMensajes = 0
    HoraInicio = ""
    FechaInicio  = ""
    FechaFin  = ""
    # for i in listasC:
        # if i == 0:
    nombreCliente = lines[0] #str(i)
        # if i == 1:
    nombreGestorCliente = lines[1] #str(i)
        # if i == 2:
    provincia = lines[2] #str(i)
        # if i == 2:
    VecesXdia = int(lines[3]) #str(i)   
        # if i == 3:
    TiempoEntreMensajes = int(lines[4]) #str(i)   
        # if i == 4:
    HoraInicio = int(lines[5]) #str(i)
        # if i == 5:
    FechaInicio1 = lines[6] #str(i)
        # if i == 6:
    FechaFin1 = lines[7]#str(i)

    RecibirPublicaciones = 0

    textoV0 = nombreCliente
    textoV1 = nombreGestorCliente	
    textoV12 = provincia	
    textoV2 = VecesXdia
    textoV3 = TiempoEntreMensajes
    textoV4 = HoraInicio
    textoV5 = FechaInicio1
    textoV6 = FechaFin1
    if textoV0:
        #nombreCliente = configuraciones[message.chat.id]["nombreCliente"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["nombreGestorCliente"]}'
    if textoV1:
        #nombreGestorCliente = configuraciones[message.chat.id]["nombreGestorCliente"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["provincia"]}'
    if textoV12:
        #nombreGestorCliente = configuraciones[message.chat.id]["nombreGestorCliente"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["VecesXdia"]}'
    if textoV2:
        #VecesXdia = configuraciones[message.chat.id]["VecesXdia"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["HoraInicio"]}'    
    if textoV3:
        #TiempoEntreMensajes = configuraciones[message.chat.id]["TiempoEntreMensajes"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["HoraInicio"]}'
    if textoV4:
        #HoraInicio = configuraciones[message.chat.id]["HoraInicio"]
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["FechaInicio"]}'
    if textoV5:
        # Convertimos un string con formato <d�a>/<mes>/<a�o> en datetime
        ## una_fecha = '20/04/2019'
        demo = FechaInicio1
        
        una_fecha = re.sub(r"^\s+|\s+$", "", demo) #demo # FechaInicio1.strip(' ') #FechaInicio1 #configuraciones[message.chat.id]["FechaInicio"]
        #print("  " + FechaInicio)
        
        FechaInicio= datetime.strptime(una_fecha, '%d-%m-%Y')
        RecibirPublicaciones += 1
    #textoV = f' {configuraciones[message.chat.id]["FechaFin"]}'
    if textoV6:
        # Convertimos un string con formato <d�a>/<mes>/<a�o> en datetime
        ## una_fecha = '20/04/2019'
        #string = FechaFin1
        demo = FechaFin1
       
        una_fecha =  re.sub(r"^\s+|\s+$", "", demo) #demo # 
        #una_fecha = FechaFin1.strip(' ') #FechaFin1 #configuraciones[message.chat.id]["FechaFin"]
        FechaFin = datetime.strptime(una_fecha, '%d-%m-%Y')
        RecibirPublicaciones += 1
        Fecha = FechaInicio
        
        
    if RecibirPublicaciones == 7:
        if int(VecesXdia) > 0:
            Cada_x_Hora = 24/VecesXdia 
            Cada_x_Hora = round(Cada_x_Hora, 0)
        else:
            Cada_x_Hora = 0
        DiasT = (FechaFin - FechaInicio).days + 1
        Continue = "no"
        with open(path1 + 'schedule_temp.txt','w') as f:
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
                            ##TiempoEntreMensajesTXT
                            if TiempoEntreMensajes > 9:
                                TiempoEntreMensajesTXT = str('{:.0f}'.format(TiempoEntreMensajes))
                            else:
                                TiempoEntreMensajesTXT = "0" + str('{:.0f}'.format(TiempoEntreMensajes))                                 
                            cadena = fechaRepet + " " + HotaTXT + " "  + TiempoEntreMensajesTXT + " " + nombreCliente + " " + nombreGestorCliente  # + " " + str(message.message_id)##str(msg.message_id
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

# @bot.message_handler(commands=["start", "reset", "agregarcanal", "eliminarcanal", "mostrarcanal", "verconfig", "alta", "eliminarconfig", "enceconfig", "sendahora", "sendfechahora", "bajartxt", "IdMSG", "ayuda", "help"])
# def commands(message):   
    # cmd_texto1(message)

@bot.message_handler(commands=["RRRRRRRRRRRRR"])

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

# def guardar_schedule(schedule):
	# with open(path1 + 'schedule.txt','w') as f:
		# f.write(schedule)
		# f.close

#if __name__ == '__main__':
def ayuda1(message):
    estado = "help"
    guardar_estado(estado)
    #Correr_def = cmd_start(message)
    texto = "Datos de ayuda:\n"
    texto+= "/start : Inicia el Bot\n"
    texto+= "/reset : Borra o elimina las configuraciones y publicaciones\n"
    texto+= "/agregarcanal : Agrega persona, grupo o canal a la lista de difusión\n"
    texto+= "/eliminarcanal : Elimina persona, grupo o canal de la lista de difusión\n"
    texto+= "/mostrarcanal : Muestra la lista de persona, grupo o canal para difusión\n"
    texto+= "/publicar : Para incluir las publicaciones en la configuracion\n"
    texto+= "/cancelconfig : Para cancelar captacion de publicación y configuracion\n"        
    texto+= "/finalizar : Para terminar y guardar publicaciones en la configuración\n"
    texto+= "/verconfig : Para mostrar las configuraciones.\n"
    texto+= "/alta : Para crear nueva configuración\n"
    texto+= "/eliminarconfig : Para eliminar configuración.\n"
    texto+= "/venceconfig : Para mostrar las configuraciones que se vencen en tres.\n"
    texto+= "/sendahora : Para enviar ahora primera configuracion.\n"
    texto+= "/sendfechahora : Para enviar ahora todas configuraciones (pasadas, actuales o futuras) que cumplan con la fecha y la horas..\n"
    texto+= "/bajartxt : Para bajar las txt de configuraciones guardadas.\n"
    texto+= "/idmsg mas # Reenvia mensaje existente en nustro chat_id a ti mismo nuevamente.\n"
    texto+= "/publicarboton Para publicar botones.\n"
    texto+= "/ayuda : La presente ayuda\n"
    texto+= "/help : La presente ayuda\n"
    texto+= "/publicarboton : enviar botones con enlaces\n"
    mensaje = bot.send_message(mi_chat_id, texto, parse_mode="HTML")    
        
print('   Sub Final')
def activar_schedule():
    print("     SCHEDULE INICIADO...")
    #schedule.every().day.at(HORA_UNICA).do(report)
    #schedule.every().day.at("21:40").do(report_fecha_vence)
    ##chedule.every().day.at("21:34").do(report)#server +4
    #schedule.every().day.at("19:18").do(report)#local +4
    schedule.every().day.at("00:00").do(report)
    schedule.every().day.at("01:00").do(report)
    schedule.every().day.at("02:00").do(report)
    schedule.every().day.at("03:00").do(report)
    schedule.every().day.at("04:00").do(report)
    schedule.every().day.at("05:00").do(report)
    schedule.every().day.at("06:00").do(report)
    schedule.every().day.at("07:00").do(report)
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
    schedule.every().day.at("23:00").do(report)
    while True:
        schedule.run_pending()

def recibir_mensajes():
	##bucle infinito que comproeba si hay nuevos mensajes
		bot.infinity_polling()

# Main ####################################
if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("alta", "Para crear nueva configuración"),
        telebot.types.BotCommand("publicarboton", "Para publicar botones"),
        telebot.types.BotCommand("agregarcanal", "Agrega persona, grupo o canal a la lista de difusión"),
        telebot.types.BotCommand("eliminarcanal", "Elimina persona, grupo o canal de lista de difusión"),
        telebot.types.BotCommand("mostrarcanal", "Muestra lista de persona, grupo o canal para difusión"),
        telebot.types.BotCommand("verconfig", "Para mostrar las configuraciones."),
        telebot.types.BotCommand("eliminarconfig", "Para eliminar configuración."),
        telebot.types.BotCommand("reset", "Borra o elimina las configuraciones y publicaciones."),
        telebot.types.BotCommand("venceconfig", "Para mostrar configuraciones que se vencen en tres."),
        telebot.types.BotCommand("sendahora", "Para enviar ahora primera configuracion."),
        telebot.types.BotCommand("sendfechahora", "Envia configuracionessegun fecha y la horas."),
        telebot.types.BotCommand("bajartxt", "Para bajar las txt de configuraciones guardadas."),
        telebot.types.BotCommand("idmsg", "Más Reenvia mensaje en nustro chat a ti mismo nuevamente."),
        telebot.types.BotCommand("publicarboton", "Enviar botones con enlaces\n"),
        telebot.types.BotCommand("ayuda", "La presente ayuda")
        ])
    print('    Iniciando el BOT')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    hilo_bot = threading.Thread(name="hilo_bot", target=activar_schedule)
    hilo_bot.start()
    print('   Fin')