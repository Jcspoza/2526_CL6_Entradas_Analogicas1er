# 2526_CL6_Entradas_Analogicas1er

Clase 6- Entradas Analogicas 1er Estudio

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## Clase 6 - Indice

- Propuesta de estudio : entradas analógicas en micro Controladores

- Materiales y links a información
  
  * Lista de materiales
  
  * Links a Tutoriales  e informacion
  - Librerías importantes - No necesarias

- Aprender / Entender: entradas analógicas en micro Controladores
  
  - Intro Teórica breve a los ADC´s
  
  - 1er montaje : Divisor de tensión
  
  - 2do Montaje : Potenciómetro
  
  - 3ro Montaje : LDR

- Lista (no completa) de sensores analógicos en robotica

- Proyecto completo: por decidir

- Tabla resumen de programas

- TO DO y Notas

## Propuesta de estudio : entradas analógicas en micro Controladores

## Materiales y links a información

### Librerías importantes - No necesarias

## Aprender / Entender: entradas analógicas en micro Controladores

### Intro Teórica breve a los ADC´s

El mundo real es analógico, luego si queremos controlarlo con electrónica programable (=microcontroladores), tenemos que poder 'leer' informacion analógica y viceversa, tenemos que poder convertir de vuelta al mundo real, informacion digital en una magnitud física como un voltaje que se corresponda con la informacion digital.

Por eso, no es raro que desde el inicio los micro Controladores tuvieran entradas que podían convertir la informacion analógica, normalmente un valor de voltaje, informacion digital: el controlador Arduino UNO R3 ( lanzado en 2011)  tiene 6 entradas analógicas directas, o ADC´s. La conversión contraria, desde digital a analógico o DAC no es común en los uControladores porque priorizan la funcionalidad básica, el bajo costo y el bajo consumo, y el **ADC es más crítico para la mayoría de las interacciones con el mundo analógico**; además, para aplicaciones de alta fidelidad o velocidad (audio, video), un DAC externo ofrece mejor rendimiento, precisión, flexibilidad y diseño modular. 

<img src="./doc/ADCenuC.png" title="" alt="" width="515">

El uC PICO W/2W tiene 4 conversores analógico a digital ADC disponibles 

* 3 x en ellos pines 26, 27 y 28  ADC0, ADC1, ADC2

* Y 1 mas que lee la temperatura

#### Conceptos a conocer Conversión Analógico-> Digital

**Muestreo**: complejo, no es importante a baja velocidad 

**Rango de entrada** En el Pico y Pico W : **0 volt a 3.3 volt**

**Resolución** En el Pico y Pico W : **12 bits expandidos a 16bits** La expansión es por expansión de Taylor no una simple multiplicación La resolución = Rango / (2 n -1)= 3.3 volt / (2 16 -1)= **50 uvolt** 

**Off-set** complejo

**Linealidad** complejo

### 1er montaje : Divisor de tensión sin  uControlador

Antes de usar en programación una de las entradas analógicas del Pico w/2w, hay que entender un divisor de tensión construido con 2 resistencias

### 2do Montaje : Potenciómetro

### 3ro Montaje : LDR

### Lista (no completa) de sensores analógicos en robotica

---

## Proyecto completo: por decidir

## Tabla resumen de programas

## TO DO y Notas![]()
