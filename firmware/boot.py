
# Servidor
try:
	import usocket as socket
except:
	import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import utime

# credenciales para conectase con la red 
ssid = 'nombre de la red aqui' 
password = 'contrasena aqui'

#configurando  Conexion

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#es[eradno hasta opetner conexion y establecer una ip]
while station.isconnected() == False:
	print('waiting...')
	pass

#se imprime la ip atraves de la consola 
print('Connection successful')
print(station.ifconfig())
# led para indicar el estado de funcionamiento
led = Pin(13, Pin.OUT)
