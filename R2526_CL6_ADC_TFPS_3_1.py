# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 12 - 8
# Goal : Sensor d epresion de pelicula delgada -TFPS reading basic
# Learning Target : Analog digital converter basic
# Ref : https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_photoresistor.html machine import ADC
# basado en 3.1 LDR

from machine import ADC, Pin
from time import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External LDR on GPIO27 ADC1+ 10k ->vcc + led gpio14"
p_project = "TFPS enciende LED- TFPS en ADC1 & TFPS ohm value"
p_version = "3.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end


# 1- Crea el objeto ADC que conecta el pin central
# de un divisor de tension GND - LDR <adc1> - 10k - vcc
# adc1 = gpio 27
TFPS_ADC = 1 # es el ADC1
tfps = ADC(TFPS_ADC)
MAXVCC = 3.253 # voltios medidos en pin 36
FACTOR_CONVERSION = MAXVCC / (65535)

# crea led en gpio 14 enciende con '1'
ledext = Pin(14, Pin.OUT)
ledext.value(0)

# 2- Bucle de lectura
while True:
    tfpsValueRaw = tfps.read_u16()
    voltios = tfpsValueRaw * FACTOR_CONVERSION
    tfpsohmvalue = int(10_000 * (1 / ((MAXVCC/voltios) - 1)))
    # print(f"Voltaje leido = {voltios:.3f} voltios | Valor ADC bruto = {potvalueRaw}")
    print(f"Voltaje leido = {voltios:.2f} voltios")
    print(f"Corresponde a una resitencia TFPS de = {tfpsohmvalue:,d} ohms")
    
    if tfpsohmvalue < 2000:
        ledext.value(1)
    else:
        ledext.value(0)
        
    sleep(.5)
    
