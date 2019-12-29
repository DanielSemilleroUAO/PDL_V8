# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:21:21 2018

@author: Daniel Delgado Rodrìguez
         Juan Fernando Guerrero F.  
"""
###############################################################################
###############################################################################
        #########           ###########                ###########            
        #        #      @        #                          # 
        #        #               #                          #
        #        #      #        #         #########        #
        #########       #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #########       #   ###########    #########        #
###############################################################################
###############################################################################

import paho.mqtt.client as mqtt
#-------------------FUNCIONES MQTT---------------------------------------------
def leer_valores(archivo):
    f = open(archivo)
    linea = f.readline()
    f.close()
    return linea
def guardar_valores(archivo,mensaje):
    f = open(archivo,'w+')
    f.write(mensaje)
    f.close()   
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([("cantidad/papelcarton",2),("cantidad/organico",2),("cantidad/plastico",1),("cantidad/vidrio",1),("cantidad/metal",0)])
def on_message(client, userdata, msg):
    dato_c = msg.payload.decode()
    dato = dato_c.split(",")
    print(dato)        
    if dato[0] == 'CPC':
        guardar_valores("MEDIDA_CONTENEDORES/CPC.txt",dato[1])
    if dato[0] == 'COR':
        guardar_valores("MEDIDA_CONTENEDORES/COR.txt",dato[1])
    if dato[0] == 'CP':
        guardar_valores("MEDIDA_CONTENEDORES/CP.txt",dato[1])
    if dato[0] == 'CV':
        guardar_valores("MEDIDA_CONTENEDORES/CV.txt",dato[1])
    if dato[0] == 'CO':
        guardar_valores("MEDIDA_CONTENEDORES/CO.txt",dato[1])
    if dato[0] == 'CM':
        guardar_valores("MEDIDA_CONTENEDORES/CM.txt",dato[1])
    if dato[0] == "Off":
        client.disconnect()
#----------------INICIO PROGRAMA-----------------------------------------------
client = mqtt.Client()
client.connect("192.168.4.1",1883,2)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
