from time import sleep
from machine import Pin
from machine import mem32
from machine import ADC

#Orden de los semaforos

#Semaroro_1: Semaforo especial
vv_especial= Pin(15, Pin.OUT)
av_especial= Pin(2, Pin.OUT)
rv_especial= Pin(0, Pin.OUT)

#Semaforo_5: semaforo_vehicular_01 y semaforo_peatonal_01
vv_01= Pin(4, Pin.OUT)
av_01= Pin(16, Pin.OUT)
rv_01= Pin(17, Pin.OUT)

vp_01= Pin(5, Pin.OUT)
rp_01= Pin(18, Pin.OUT)

#Semaforo_2: semaforo_vehicular_02 y semaforo_peatonal_02
vv_02= Pin(13, Pin.OUT)
av_02= Pin(12, Pin.OUT)
rv_02= Pin(14, Pin.OUT)

vp_02= Pin(19, Pin.OUT)
rp_02= Pin(21, Pin.OUT)

#Semaforo_4: semaforo_peatonal_04
vp_04= Pin(33, Pin.OUT)
rp_04= Pin(32, Pin.OUT)

#Semaforo_3: semaforo_vehicular_03 y semaforo_peatonal_03
vv_03= Pin(27, Pin.OUT)
av_03= Pin(26, Pin.OUT)
rv_03= Pin(25, Pin.OUT)

vp_03= Pin(22, Pin.OUT)
rp_03= Pin(23, Pin.OUT)

GPIO_SET=const(0x3FF44004) #posición en memoria

while True:
  
   mem32[GPIO_SET]=0B0100000010011000100010000000100001
   sleep(5)
   mem32[GPIO_SET]=0B0100000010011000100000000000100001 #parpadeo semaforo_02 verde
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010011000100010000000100001
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010011000100000000000100001
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010011000100010000000100001
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010011000100000000000100001
   sleep(0.5) 
   mem32[GPIO_SET]=0B0100000010011000100001000000100001 #cambio semaforo_02 a amarillo
   sleep(2)
###mem32[GPIO_SET]=0b3210987654321098765432109876543210
   mem32[GPIO_SET]=0B1000001000100010101100000000100000
   sleep(9)

