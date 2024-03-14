'''Use uno de los tipos más comunes de Python para representar texto. Desde la aplicación de formato simple hasta
la representación de variables, el uso de cadenas operativas es una aptitud fundamental para los desarrolladores
de Python.'''

'''Las cadenas de Python son uno de los tipos más importantes y más comunes del lenguaje. Aprender a interactuar
con las cadenas, incluido el formato y el reemplazo de texto, es una aptitud esencial que se debe desarrollar 
para trabajar con código de Python.'''

'''Aunque las cadenas en Python parecen ser sencillas, hay cierta complejidad en las reglas de las cadenas 
que es importante comprender. El conocimiento de las reglas ayuda a evitar que le sorprenda el comportamiento 
de las cadenas al modificar valores o dar formato al texto.'''

#Una cadena simple
En el ejemplo de esta unidad, tiene un único hecho sobre la Luna que está asignado a una variable, como este:


fact = "La Luna no tiene atmósfera."

La salida muestra que el texto se ha asignado a la variable : La Luna no tiene atmósfera.

#Inmutabilidad de las cadenas
En Python, las cadenas son inmutables. Es decir, no pueden cambiar. Esta propiedad del tipo de cadena puede
ser sorprendente, ya que Python no proporciona errores al modificar cadenas.

Debe agregar otro hecho (frase) al único hecho asignado a una variable. Parece que agregar el segundo hecho
podría modificar la variable, tal como en el ejemplo siguiente:

fact = "La Luna no tiene atmósfera."
fact + "No se puede escuchar ningún sonido en la Luna"
print(fact)

Salida: La Luna no tiene atmósfera.

'''Aquí el truco es que se debe usar un valor devuelto. Al agregar cadenas, Python no modifica ninguna, 
sino que devuelve una cadena nueva como resultado. 
Para mantener este resultado nuevo, asígnelo a una nueva variable:
'''

fact = "La Luna no tiene atmósfera."
two_facts = fact + "No se puede escuchar ningún sonido en la Luna"
print(two_facts)
////////////////////////////
dato = "La Luna no tiene atmósfera."
dos_datos = dato + "No se puede escuchar ningún sonido en la Luna"
print(dos_datos)

Salida: La Luna no tiene atmósfera. No se puede escuchar ningún sonido en la Luna.

#Acerca del uso de comillas
Puede incluir las cadenas de Python entre comillas simples, dobles o triples. 
Aunque se pueden usar indistintamente, es mejor utilizar un tipo de forma coherente dentro de un proyecto. 
Por ejemplo, en la cadena siguiente se usan comillas dobles:

radio_lunar = "La Luna tiene un radio de 1.080 millas."

Pero cuando una cadena contiene palabras, números o caracteres especiales (una subcadena) que también se 
incluyen entre comillas, debe usar otro estilo. Por ejemplo, si en una subcadena se usan comillas dobles, 
incluya toda la cadena entre comillas simples, como se muestra aquí:

'La "cara cercana" es la parte de la Luna que mira hacia la Tierra'

Del mismo modo, si en alguna parte de la cadena hay comillas simples 
(o un apóstrofo, como en Moon's en el ejemplo siguiente), incluya toda la cadena entre comillas dobles:

"We only see about 60% of the Moon's surface."

Si no se alternan las comillas simples y dobles, el intérprete de Python puede generar un error de sintaxis, 
como se muestra aquí:

'We only see about 60% of the Moon's surface.'
  File "<stdin>", line 1
    'We only see about 60% of the Moon's surface.'
                                      ^
SyntaxError: invalid syntax

Cuando el texto tiene una combinación de comillas simples y dobles, puede usar comillas triples para 
evitar problemas con el intérprete:

"""We only see about 60% of the Moon's surface, this is known as the "near side"."""

#Texto multilínea
Hay diferentes maneras de definir varias líneas de texto como una sola variable. 
Las más comunes son las siguientes:

Usar un carácter de nueva línea (\n).
Usar comillas triples ( " " " ).         
Los caracteres de nueva línea separan el texto en varias líneas al imprimir la salida:

multiline = "Datos sobre la Luna:\n No hay atmósfera.\n No hay sonido."
print(multiline)

Datos sobre la Luna:
No hay atmósfera.
No hay sonido.
                
Puede lograr el mismo resultado con las comillas triples:

multiline = """Datos sobre la Luna:
 No hay atmósfera.
 No hay sonido."""
print(multiline)

#Métodos de cadena en Python

Los métodos de cadena son uno de los tipos de método más comunes en Python. A menudo tendrá que manipular 
cadenas para extraer información o ajustarse a un formato concreto. Python incluye varios métodos de cadena 
diseñados para realizar las transformaciones más comunes y útiles.

Los métodos de cadena forman parte del tipo str. Esto significa que los métodos existen como variables de 
cadena o directamente como parte de la cadena. Por ejemplo, el método .title() devuelve la cadena en mayúsculas 
y se puede usar directamente con una cadena:

print("temperaturas y datos sobre la luna".title())

Salida/output: Temperatures And Facts About The Moon

El mismo comportamiento y utilización se produce en una variable:

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
////////////////////////////
encabezado = "temperaturas y datos sobre la luna"
encabezado_superior = encabezado.título()
print(encabezado_superior)

#División de una cadena
Un método de cadena común es .split(). Sin argumentos, el método separará la cadena en cada espacio. 
Esto crearía una lista de todas las palabras o números separados por un espacio:

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
////////////////////////////
temperaturas = "Luz diurna: 260 F Durante la noche: -280 F"
lista_temperaturas = temperaturas.split()
print(lista_temperaturas)

Salida/output: ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']
////////////////////////////
salida: ['Luz diurna:', '260', 'F', 'Noche:', '-280', 'F']

En este ejemplo, trabaja con varias líneas, por lo que el carácter de nueva línea (implícito) se puede usar 
para dividir la cadena al final de cada línea, y crear líneas únicas:

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
////////////////////////////
temperaturas = "Luz diurna: 260 F\n Noche: -280 F"
lista_temperaturas = temperaturas.split('\n')
imprimir(lista_temperaturas)

Salida: ['Daylight: 260 F', 'Nighttime: -280 F']

Este tipo de división resulta útil cuando se necesita un bucle para procesar o extraer información, 
o bien cuando se cargan datos desde un archivo de texto.

#Búsqueda de una cadena
Algunos métodos de cadena pueden buscar contenido antes del procesamiento, sin necesidad de usar un bucle. 
Imagine que tiene dos oraciones que analizan las temperaturas de varios planetas y lunas, pero solo le interesan 
las temperaturas relacionadas con la Luna. Es decir, si las oraciones no se refieren a la Luna, no se deben 
procesar para extraer información.

La manera más sencilla de detectar si existe una palabra, un carácter o un grupo de caracteres determinados 
en una cadena es usar el operador in:

print("Moon" in "This text will describe facts and challenges with space travel")
////////////////////////////
print("Luna" in "Este texto describirá hechos y desafíos de los viajes espaciales")

Salida/output: False

print("Moon" in "This text will describe facts about the Moon")
////////////////////////////
print("Luna" in "Este texto describirá datos sobre la Luna")

Salida/output: True

Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método 
.find():

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
////////////////////////////
Temperaturas = """Saturno tiene una temperatura diurna de -170 grados Celsius, mientras que Marte tiene -28 Celsius."""
print(temperaturas.find("Luna"))

Salida/output: -1

El método .find() devuelve -1 cuando no se encuentra la palabra, o bien devuelve el índice 
(el número que representa la posición en la cadena). Así es como se comportaría si busca la palabra Mars:

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
////////////////////////////
Temperatures = """Saturno tiene una temperatura diurna de -170 grados Celsius, mientras que Marte tiene -28 Celsius."""
print(temperaturas.find("Marte"))

Salida/output: 64

64 es la posición donde "Mars" aparece en la cadena.

Otra manera de buscar contenido consiste en usar el método .count(), que devuelve el número total de 
repeticiones de una palabra determinada en una cadena:

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
////////////////////////////
Temperatures = """Saturno tiene una temperatura diurna de -170 grados Celsius, mientras que Marte tiene -28 Celsius."""
print(temperaturas.count("Marte"))
imprimir(temperaturas.count("Luna"))

Output/salida

1
0

Las cadenas en Python distinguen mayúsculas de minúsculas, lo que significa que Luna y luna se consideran 
palabras diferentes. Para realizar una comparación sin distinguir mayúsculas de minúsculas, puede convertir 
una cadena en letras minúsculas mediante el método .lower():

print("The Moon And The Earth".lower())
////////////////////////////
print("La Luna y la Tierra".lower())

Salida/output: the moon and the earth

Como sucede con el método .lower(), las cadenas tienen un método .upper() que hace lo contrario y convierte 
todos los caracteres en mayúsculas:

print("The Moon And The Earth".upper())
////////////////////////////
print("La Luna y la Tierra".upper())

Salida: THE MOON AND THE EARTH
Salida/output: LA LUNA Y LA TIERRA

#### Al buscar y comprobar contenido, un enfoque más sólido consiste es convertir en minúsculas una cadena 
#### para que el uso de mayúsculas y minúsculas no impida una coincidencia. Por ejemplo, si va a contar el número 
#### de veces que aparece la palabra the, el método no contaría las veces en las que aparece The, aunque las dos 
#### sean la misma palabra. Puede usar el método .lower() para cambiar todos los caracteres a minúsculas.

#Comprobación del contenido
Hay ocasiones en las que procesará texto para extraer información con una presentación irregular. Por ejemplo, 
la cadena siguiente es más fácil de procesar que un párrafo no estructurado:

temperatures = "Mars Average Temperature: -60 C"
////////////////////////////
temperaturas = "Temperatura promedio de Marte: -60 C"

Para extraer la temperatura media en Marte, puede hacerlo con los métodos siguientes:

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
////////////////////////////
temperaturas = "Temperatura promedio de Marte: -60 C"
partes = temperaturas.split(':')
print(partes)
print(partes[-1])

Salida/output: 
['Mars average temperature', ' -60 C']
' -60 C'

El código anterior confía en que todo lo que hay después de los dos puntos (:) es una temperatura. 
La cadena se divide en :, lo que genera una lista de dos elementos. El uso de [-1] en la lista devuelve el 
último elemento que, en este ejemplo, es la temperatura.

Si el texto es irregular, no puede usar los mismos métodos de división para obtener el valor. 
Debe recorrer en bucle los elementos y comprobar si los valores son de un tipo determinado. 
Python tiene métodos que ayudan a comprobar el tipo de cadena:

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
////////////////////////////
temperatura_marte = "La temperatura más alta en Marte es de unos 30 C"
para el artículo en temperatura_marte.split():
    si elemento.isnumeric():
        imprimir (artículo)

Salida: 30

Como sucede con el método .isnumeric(), .isdecimal() puede buscar cadenas que parezcan decimales.

## Le sorprenderá saber que "-70".isnumeric() devolverá False. Esto se debe a que todos los caracteres de la 
## cadena tendrían que ser numéricos y el guión (-) no lo es. Si tiene que comprobar números negativos en una 
## cadena, el método .isnumeric() no funcionará.

Hay validaciones adicionales que puede aplicar en las cadenas para comprobar si hay valores. 
En el caso de los números negativos, el guion se agrega como prefijo al número y se puede detectar con el método 
.startswith():

print("-60".startswith('-'))

Salida: True

De forma similar, el método .endswith() ayuda a comprobar el último carácter de una cadena:

if "30 C".endswith("C"):
print("This temperature is in Celsius")

Salida: This temperature is in Celsius

####Transformar texto
Hay otros métodos que ayudan en situaciones en las que el texto se debe transformar en algo distinto. 
Hasta ahora, ha visto cadenas que pueden usar C para Celsius y F para Fahrenheit. Puede usar el método 
.replace() para buscar y reemplazar repeticiones de un carácter o grupo de caracteres:

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
////////////////////////////
print("Saturno tiene una temperatura diurna de -170 grados Celsius, mientras que Marte tiene -28 Celsius.".replace("Celsius", "C"))

Salida: Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.
////////////////////////////
Salida: Saturno tiene una temperatura diurna de -170 grados C, while//mientras que Marte tiene -28 C.

Como se ha mencionado antes, .lower() es una buena manera de normalizar el texto para realizar una búsqueda 
sin distinguir mayúsculas de minúsculas. 
Ahora se comprobará rápidamente si algún texto analiza las temperaturas:

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
////////////////////////////
texto = "Las temperaturas en la Luna pueden variar mucho."
print("temperaturas" in texto)  

Salida: False

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
////////////////////////////
texto = "Las temperaturas en la Luna pueden variar mucho."
print("temperaturas" in texto.lower())

Salida: True

Es posible que no tenga que realizar la comprobación sin distinguir mayúsculas de minúsculas todo el tiempo, 
pero convertir en minúsculas todas las letras es un buen enfoque cuando en el texto se usa una mezcla de 
mayúsculas y minúsculas.

Después de dividir el texto y realizar las transformaciones, es posible que tenga que volver a ensamblar todas 
las piezas. Al igual que el método .split() puede separar caracteres, el método .join() puede volver a agruparlos.

El método .join() necesita un elemento iterable (como una lista de Python) como argumento, 
por lo que su uso es diferente al de otros métodos de cadena:


moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
////////////////////////////
datos_luna = ["La Luna se está alejando de la Tierra.", "En promedio, la Luna se mueve unos 4 cm cada año."]


Outout: The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.
////////////////////////////
Salida: La Luna se está alejando de la Tierra. En promedio, la Luna se mueve unos 4 cm cada año.

En este ejemplo, se usa ' ' para unir todos los elementos de la lista.  


