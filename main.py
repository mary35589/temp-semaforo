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

s_temperatura=ADC(Pin(36))
s_temperatura.atten(ADC.ATTN_11DB)

conversion= 3.3/4095*100

GPIO_SET=const(0x3FF44004) #posición en memoria

global variable, muestra_temp
variable=0
muestra_temp= False 

def interrupcion(Pin):
    global variable
    print("Entre a la funcion interrupcion")
    variable=1  

pul_interrupcion=Pin(35,Pin.IN,)
pul_interrupcion.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion)


while True:
   mem32[GPIO_SET]=0B0100000010011000100010000000100001 #semaforo_02=verde semaforo_03=rojo semaforo_05=rojo semaforo_especial=rojo
   sleep(9)
   mem32[GPIO_SET]=0B0100000010011000100000000000100001 #parpadeo semaforo_02=verde
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
   mem32[GPIO_SET]=0B1000001000100011101100000000000000 #semaforo_03=verde semaforo_02=rojo semaforo_05=rojo semaforo_especial=verde 
   sleep(7)
   mem32[GPIO_SET]=0B1000000000100011101100000000000000 #parpadeo semaforo_03=verde
   sleep(0.5)
   mem32[GPIO_SET]=0B1000001000100011101100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B1000000000100011101100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B1000001000100011101100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B1000000000100011101100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B1000000100100011101100000000000000 #cambio semaforo_03 a amarillo
   sleep(2)
   mem32[GPIO_SET]=0B0100000010010011001100000000010000 #semaforo_especial=verde semaforo_02=rojo semaforo_03=rojo semaforo_05=verde
   sleep(9) 
   mem32[GPIO_SET]=0B0100000010010011000100000000000000 #parpadeo semaforo_especial=verde y semaforo_05=verde
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010010011001100000000010000
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010010011000100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010010011001100000000010000
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010010011000100000000000000
   sleep(0.5)
   mem32[GPIO_SET]=0B0100000010010011010100000000000100#cambio semaforo_especial a amarillo semaforo_05=amarillo
   sleep(2)

   if variable==1:
      mem32[GPIO_SET]=0B1000000010010010100100000000100001 
      sleep(10)
      variable=0
###mem32[GPIO_SET]=0b3210987654321098765432109876543210


