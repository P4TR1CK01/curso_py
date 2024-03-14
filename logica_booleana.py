'''Para este paso se le presentará el objetivo del ejercicio, seguido de una celda vacía.'''

tamaño_objeto = 10
if tamaño_objeto > 5:
    print('necesitamos vigilar este objeto')
else:
    print('El objeto no representa ninguna amenaza.')

'''Los operadores booleanos son palabras o símbolos que permiten combinar conceptos o términos para ampliar,
limitar o definir tus búsquedas. El operador Booleano solo puede tener dos valores, según lógica binaria,
y por lo general se muestran con un dato que puede ser verdadero o falso.'''

'''Puede conectar dos expresiones booleanas, o de prueba, mediante el operador booleano or.
Para que toda la expresión se evalúe como True, al menos una de las subexpresiones debe ser true.
Si ninguna de las subexpresiones es true, toda la expresión se evalúa como False.
Por ejemplo, en la expresión siguiente, toda la expresión de prueba se evalúa como True, porque
se ha cumplido una de las condiciones de las subexpresiones:'''

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

'''Si las dos subexpresiones son true, toda la expresión de prueba también se evalúa como True.'''

'''Una expresión booleana que usa or tiene la sintaxis siguiente:'''

sub-expression1 or sub-expression2

'''El operador and
También puede conectar dos expresiones de prueba mediante el operador booleano and. 
Las dos condiciones de la expresión de prueba deben cumplirse para que toda la expresión
de prueba se evalúe como True. En cualquier otro caso, la expresión de prueba es False. 
En el ejemplo siguiente, toda la expresión de prueba se evalúa como False, porque solo una de las condiciones 
de las subexpresiones es true:'''

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

'''Una expresión booleana que usa and tiene la sintaxis siguiente:'''

sub-expression1 and sub-expression2

'''Diferencia entre and y or
Para resaltar la diferencia entre los dos operadores booleanos, puede usar una tabla de verdad. 
Una tabla de verdad muestra cómo se evalúa toda la expresión de prueba en función de las dos subexpresiones.
Esta es la tabla de verdad para and:'''

subexpression1	Operador	subexpression2	Resultado
True	          and	      True	          True
True	          and	      False	          False
False	          and	      True	          False
False	          and	      False	          False

'''Esta es la tabla de verdad para or:'''

subexpression1	Operador	subexpression2	Resultado
True	          or	       True	          True
True	          or	       False          True
False	          or	       True	          True
False	          or	       False          False

'''Ejercicio: Utilice una lógica compleja para determinar posibles maniobras evasivas.
En el ejercicio anterior creó código para probar el tamaño del objeto. Ahora probarás tanto el tamaño como
la proximidad del objeto. Utilizará el mismo umbral para un tamaño de 5 m3. Si el objeto es más grande que
el umbral y está dentro de los 1000 km del barco, se requerirán maniobras evasivas.

Para este paso se le presentará el objetivo del ejercicio, seguido de una celda vacía. 
Ingrese su Python en la celda y ejecútelo. La solución está al final del ejercicio.

Agregue el código a la celda siguiente para crear dos variables: tamaño_objeto y proximidad. 
Establezca object_size en 10 para representar 10 m3. Establezca la proximidad en 9000.

Luego agregue el código para mostrar un mensaje que diga Se requieren maniobras evasivas si el tamaño_objeto 
es mayor que 5 y la proximidad es menor que 1000. De lo contrario, muestre un mensaje que diga
El objeto no representa ninguna amenaza.'''

tamaño_objeto = 10
proximidad = 9000

if tamaño_objeto > 5 and proximidad < 1000:
    print('Maniobras evasivas requeridas')
else:
    print('El objeto no representa ninguna amenaza')

'''Salida deseada 
Cuando ejecuta el notebook, debería ver el siguiente resultado:
El objeto no representa ninguna amenaza
'''

Comprobación de conocimientos

1. ¿En qué condiciones se evalúa como True una expresión de prueba que usa el operador and? 


Una expresión de prueba que usa el operador and se evalúa como True cuando las dos subexpresiones son verdaderas.

Una expresión de prueba que usa el operador and se evalúa como True cuando una subexpresión es true y la otra es false.

Una expresión de prueba que usa el operador and se evalúa como True cuando las dos subexpresiones son falsas.



2. ¿De qué es abreviatura la palabra clave elif en Python? 


más si

sólo si

demás



3. ¿Qué valores de una expresión de prueba siempre se interpretan como false? 


Los valores distintos de cero

Vacío

Ninguno y 0




