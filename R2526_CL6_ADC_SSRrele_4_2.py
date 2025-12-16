# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 12 - 8
# Goal : LDR reading basic  -> activate RELAY
# Learning Target : Analog digital converter basic
# Ref : https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_photoresistor.html machine import ADC
# 1.0 -> 2.0 añadir calculo de resitencia de LDR
# 2.0 -> 2.1 import machine con from
# 2.1 -> 3.1 encender led en gpio 14
# 3.1 -> 4.1 añade modulo de rele en GPIO15
# 4.1 -> 4.2 cambia rele por SSR rele y la logica se invierte Activo si '0'

from machine import ADC, Pin
from time import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External LDR on GPIO27 ADC1+ 10k ->vcc + rele GPIO15 + led gpio14"
p_project = "LDR activa mod SSR Rele(activo Low)- LDR en ADC1 & LDR ohm value"
p_version = "4.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end


# 1- Crea el objeto ADC que conecta el pin central
# de un divisor de tension GND - LDR <adc1> - 10k - vcc
# adc1 = gpio 27
LDR_ADC = 1 # es el ADC1
ldr = ADC(LDR_ADC)
MAXVCC = 3.253 # voltios medidos en pin 36
FACTOR_CONVERSION = MAXVCC / (65535)

# crea led en gpio 14 enciende con '1'
ledext = Pin(14, Pin.OUT)
ledext.value(0)

# crea rele en gpio 15 conecta comun con NO con '1'
SSRrele = Pin(15, Pin.OUT)
SSRrele.value(1)

# 2- Bucle de lectura
while True:
    ldrValueRaw = ldr.read_u16()
    voltios = ldrValueRaw * FACTOR_CONVERSION
    ldrohmvalue = int(10_000 * (1 / ((MAXVCC/voltios) - 1)))
    # print(f"Voltaje leido = {voltios:.3f} voltios | Valor ADC bruto = {potvalueRaw}")
    print(f"Voltaje leido = {voltios:.2f} voltios")
    print(f"Corresponde a una resitencia LDR de = {ldrohmvalue:,d} ohms")
    
    if voltios > 2.5:
        ledext.value(1)
        SSRrele.value(0)
        print('Armado de Rele')
    else:
        ledext.value(0)
        SSRrele.value(1)
        
    sleep(.5)
    
