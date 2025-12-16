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
  
  - 4to Montaje : 

- Lista (no completa) de sensores analógicos en robotica

- Proyecto completo: por decidir

- Tabla resumen de programas

- TO DO y Notas

## Propuesta de estudio : entradas analógicas en micro Controladores

Más que un proyecto para ir construyendo progresivamente, esta Clase #6 será un estudio de las entradas analógicas experimentando con uno o dos sensores, hasta que los conceptos básicos queden claros

## Materiales y links a información

Materiales y links a informacion

| Material                                                                                                                                                                                                                                                                                                                                                                    | Descripcion                                                                                                                                                      | Kit SF                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [Protoboard 700](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_breadboard.html)                                                                                                                                                                                                                                                             | Placa para prototipos ver apartado [Uso de la protoboard](https://github.com/Jcspoza/2526CL1_R_CircElect0#uso-de-la-protoboard). Mejor usar la protoboard de 700 | SI                             |
| [Cables dupond M-M](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_wire.html)                                                                                                                                                                                                                                                                | Sirven para hacer conexiones en protoboard                                                                                                                       | SI                             |
| [Led rojo](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_led.html)                                                                                                                                                                                                                                                                         | Se usara para indicar comienzo de cuenta de Tiempo de reacción                                                                                                   | SI                             |
| [Resistencia 220 ohm x1](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_resistor.html)                                                                                                                                                                                                                                                      | Resistencia 220 ohm para limitar corriente de LED                                                                                                                | SI                             |
| [Potenciómetro](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_potentiometer.html)                                                                                                                                                                                                                                                          |                                                                                                                                                                  | SI                             |
| [Resistencia 10k ohm x2](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_resistor.html)                                                                                                                                                                                                                                                      | Resistencia de 10 K ohm para pull-Down                                                                                                                           | SI                             |
| [Fotoresitencia o LDR](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_photoresistor.html)                                                                                                                                                                                                                                                   | su resistencia varia con la luz desde unos 530Kohm en oscuridad a 130 ohm con luz intensa ( valores medidos reales)                                              | SI                             |
| [Modulo de Rele usado](https://www.amazon.es/dp/B06XHJ2PBJ/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B06XHJ2PBJ&pd_rd_w=yyCkH&content-id=amzn1.sym.dec61eec-c10c-476f-b9d1-109d380c1864&pf_rd_p=dec61eec-c10c-476f-b9d1-109d380c1864&pf_rd_r=BMH459G8AHTS2B1FYP0C&pd_rd_wg=UTLwg&pd_rd_r=ea22ee41-b6b5-4a2a-b997-f3e4dc2ae3b8&aref=01fjq4m3Ur&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy) | [Rele del kit SF](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_relay.html)                                                     | SI  pero necesita Hw adicional |

### Fotos del montaje final

| <img src="./doc/LDRrele_detalle.jpg" title="" alt="" width="398"> | <img title="" src="./doc/LDRreleEncendido.jpg" alt="" width="398"> | <img title="" src="./doc/LDRreleApagado.jpg" alt="" width="398"> |
| ----------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |

### Librerías importantes - No son necesarias en CL6

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

Antes de usar en programación una de las entradas analógicas del Pico w/2w, hay que entender un divisor de tensión construido con 2 resistencias. la teoria basica la podemso encontrar en el libro de electrónica de referencia 

[Electronica para makers - Paoplo Aliverti - Ed marcombo](https://github.com/Jcspoza/2526_PyR_Index/blob/main/doc/edoc.site_electronica-para-makers-paolo-aliverti.pdf)

en la pag 70 '**Divisores de tensión y de corriente'**

o la siguiente guía

[¡Domina el Divisor de Tensión! ⚡️ Aprende a Calcularlo Fácilmente &#8211; Cano Electrónica](https://proveedoracano.com/blog/todo-sobre-el-divisor-de-tension-guia-rapida-principiantes/)

de la que tomare la siguiente imagen y la formula básica del divisor de tensión

![Fórmula divisor de tensión](https://proveedoracano.com/blog/wp-content/uploads/formula-divisor-de-tension-1024x576.jpg)

![Fórmula del divisor de tensión](https://proveedoracano.com/blog/wp-content/uploads/image-15.png)

Montemos un divisor de tensión con una fuente de 5 volt ( como V in) y 2 resistencias de distintos valores : 220 ohm, 330 ohm y 16 ohm, y comprobemos la formula del Vout en R2

#### Tolerancia de las resistencias

Ya que disponemos de varias resistencias del mismo valor teórico, comprobemos como <u>si medimos varias del mismo valor </u>**NO darán los mismos exactos valores**, pero los valores estaran en el rango de tolerancia: 10%, 5%,...

### 2do Montaje : Potenciómetro

Vamos a hacer una versión simplificada del tutorial de sunfounder ( sin LED controlado por PWM) 

[2.12 Feel the Light &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_photoresistor.html)

codigo propio-Potenciómetro

Conexiones :

- el pin central del potenciometro a adc0 = gpio 26

- los otros 2 pines a +3.3 y 0 volt respectivamente

[R2526_CL6_ADC_poten_1_0.py](R2526_CL6_ADC_poten_1_0.py)

#### Truco en Thonny - ploter

En Thonny añado “plotter” a la visualización

![](./doc/thonnyPloter.png)

### 3ro Montaje : LDR

Seguiremos el montaje de Sunfounder

[2.12 Feel the Light &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_photoresistor.html)

#### LDR -1ra versión

Conexiones : el pin central de un divisor de tensión GND - LDR ->adc1< - 10k - vcc

 adc1 = gpio 27

[R2526_CL6_ADC_LDR_2_1.py](R2526_CL6_ADC_LDR_2_1.py)

#### LDR -2da versión

Añade a LDR 1ra versión , un Led rojo en GPIO14 cuando luz es poca

[R2526_CL6_ADC_LDR_3_1.py](R2526_CL6_ADC_LDR_3_1.py)

#### TFPS - Sensor de presión de película fina

Ejemplo de como aprovechar el codigo y el montaje HW del LDR para otros sensores analógicos resistivos.

[R2526_CL6_ADC_TFPS_3_1.py](R2526_CL6_ADC_TFPS_3_1.py)

#### LDR_Rele- 3ra Version

Añade a LDR 2da versión , un moduilo de Rele en GPIO15 que responde cuando luz es poca, conectando comun y NO ( normally open = normalmente abierto)

[R2526_CL6_ADC_LDRrele_4_1.py](R2526_CL6_ADC_LDRrele_4_1.py)

#### LDR Relé SSR - 4ta versión

Los reles de estado solido SSR, son una alternativa No mecánica a los reles de bobina. Este que he usado es de lógica negativa 
: se activa con '0'

Se ha cambiado el progrma de rele 4.1 -> 4.2 para cambiar la logica de activacion

[R2526_CL6_ADC_SSRrele_4_2.py](R2526_CL6_ADC_SSRrele_4_2.py)





##### Notas HW conexionado de Reles

En mi montaje he usado un modulo de relé (antiguo) que viene con el HW adicional al rele necesario ya incluido, porque disponía de el. 

Si solo se dispone de un relé como es el caso del Kit SF, hay que añadir Hw adiciona . Ver 

[2.16 Control Another Circuit &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_relay.html)

Explicación:

- El diodo, se llama diodo de fly-back y sirve para 'devolver' las corrientes parasitas que surgen a apagar la bobina del relé 

- El transistor NPN y la resistencia de base de 1k, son un circuito de transistor en corte-saturación, para poder suministrar una corriente suficiente a la bobina del rele ( necesita 120 ma) usando una corriente muy pequeña ( 1 a 2 mA) desde el pin de la PICO w/2W

- Ver [datasheet del rele](SRS--4000-.pdf)

![sch_relay_1](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/_images/sch_control_another_circuit.png)

### Lista (no completa) de sensores analógicos en robotica

pendiente

| Tutorial principal                                                                                                           | HW necesario + Link de SF o de compra                                                                                      | Qué se necesita entender                                              | Parámetro físico que traduce | Esta en Kit SF                                   | Referencia de Clase CMM PyR           |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------ | ------------------------------------- |
| [Potenciómetro](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_potentiometer.html#)          | Potenciómetro de un valor > 10k                                                                                            | **ADCnPICO** : Conversión ADC en Pico + Divisor de tensión            | Giro                         | SI                                               | 2526_CL6                              |
| [2.13 Thermometer](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_temp.html)                        | [NTC](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_thermistor.html) + resistencia 10K    | **ADCnPICO** + Resistencia de coeficiente negativo                    | **Temperatura**              | SI                                               |                                       |
| [2.12 Feel the Light](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_photoresistor.html)     | [LDR](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_photoresistor.html) + resistencia 10K | **ADCnPICO** + Foto-resistencia + Divisor de tensión                  | Nivel de **Luz**             | SI                                               | 2526_CL6                              |
|                                                                                                                              |                                                                                                                            | **ADCnPICO** + **BJCnZL** : transistor BJC en zona lineal             | **Humedad** de suelo         | No salvo que sirva el sensor de nivel de humedad | NO                                    |
| [4.1 Toggle the Joystick](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_joystick.html#py-joystick) | [Modulo de Joystick](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_joystick.html)         | **ADCnPICO** + son 2 potenciómetros en posición en cruz y un pulsador | **Mover en 2D**:  X e Y      | SI                                               | clase que dio Fernando en 2024 - 2025 |
| [2.14 Feel the Water Level](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_water.html#py-water)     | [Sensor de nivel de agua](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_water.html)       | **ADCnPICO** + **BJCnZL** : transistor BJC en zona lineal             | **Nivel de agua**            |                                                  |                                       |
|                                                                                                                              |                                                                                                                            |                                                                       |                              |                                                  |                                       |

---

## Proyecto completo: por decidir

Se trata de elegir un sensor analógico u ver un uso útil , o viceversa ver un uso donde se pueda usar un sensor analógico que este fácilmente disponible y no tenga un precio alto.

## Tabla resumen de programas

| Programa                                                     | Lenguaje | HW si Robotica y Notas                                                                                                                                                                    | Objetivo de Aprendizaje                             |
| ------------------------------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [R2526_CL6_ADC_poten_1_0.py](R2526_CL6_ADC_poten_1_0.py)     | uPy      | pin central potenciómetro a ADC0                                                                                                                                                          | Entradas analógicas + plotter de thonny             |
| [R2526_CL6_ADC_LDR_2_1.py](R2526_CL6_ADC_LDR_2_1.py)         | uPy      |                                                                                                                                                                                           |                                                     |
| [R2526_CL6_ADC_LDR_3_1.py](R2526_CL6_ADC_LDR_3_1.py)         | uPy      | añade un Led rojo en GPIO14 cuando luz es poca                                                                                                                                            |                                                     |
| [R2526_CL6_ADC_TFPS_3_1.py](R2526_CL6_ADC_TFPS_3_1.py)       | uPy      | Usa el circuito y el programa de LDR, para leer un sensor de presión de pelicula fina                                                                                                     |                                                     |
| [R2526_CL6_ADC_LDRrele_4_1.py](R2526_CL6_ADC_LDRrele_4_1.py) | uPy      | añade un modulo de rele a GPIO15 / en el kit de SF hay que hacer un montaje con un transistor y un diodo / No deberia funcionar con un voltaje de bobina de menos de 5volt, pero funciona | Se puede controlar un voltaje de 220 volt con un uC |
| [R2526_CL6_ADC_SSRrele_4_2.py](R2526_CL6_ADC_SSRrele_4_2.py) | uPy      | añade un modulo de **rele de estado solido SSR** a GPIO15, se activa con '0' / no deberia funcionar con un voltaje de 3.3 volt , pero funciona                                            | Se puede controlar un voltaje de 220 volt con un uC |

---

## TO DO y Nota

- Todo: Investigar modelos de reles de bobina y SSR que funcionen a 3,3 volt y que incluyan optoacopladores

- Investigar optoacopladores
