# ejercicio 1
def factorial(n):
    # caso base: si es 0 o 1 el resultado es 1
    if n == 0 or n == 1:
        return 1
    # paso recursivo: multiplica el numero por el anterior
    return n * factorial(n - 1)

# num = int(input('ingrese un numero entero positivo: '))
# print('factoriales desde 1 hasta', num)
# for i in range(1, num + 1):
#     print('el factorial de', i, 'es:', factorial(i))


# ejercicio 2
def fibonacci(n):
    # casos base: devuelve el mismo numero si es 0 o 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # paso recursivo: suma las dos posiciones anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)

# posicion = int(input('ingrese la posicion para fibonacci: '))
# print('serie completa de fibonacci:')
# for i in range(posicion + 1):
#     print('posicion', i, ':', fibonacci(i))


# ejercicio 3
def potencia(base, exponente):
    # caso base: todo numero elevado a la 0 da 1
    if exponente == 0:
        return 1
    # paso recursivo: multiplica la base por la potencia del exponente anterior
    return base * potencia(base, exponente - 1)

# b = int(input('ingrese la base: '))
# e = int(input('ingrese el exponente: '))
# print('el resultado de la potencia es:', potencia(b, e))


# ejercicio 4
def decimal_a_binario(n):
    # caso base: frena cuando el cociente llega a cero
    if n == 0:
        return ''
    # paso recursivo: divide por dos y pega el resto al final
    return decimal_a_binario(n // 2) + str(n % 2)

# numero = int(input('ingrese numero decimal: '))
# if numero == 0:
#     print('el numero en binario es: 0')
# else:
#     print('el numero en binario es:', decimal_a_binario(numero))


# ejercicio 5
def es_palindromo(palabra):
    # caso base: si queda una letra o ninguna es palindromo
    if len(palabra) <= 1:
        return True
    # si los extremos son distintos no es palindromo
    if palabra[0] != palabra[-1]:
        return False
    # paso recursivo: achica la palabra sacando los extremos
    return es_palindromo(palabra[1:-1])

# print('es palindromo neuquen?:', es_palindromo('neuquen'))
# print('es palindromo radar?:', es_palindromo('radar'))
# print('es palindromo python?:', es_palindromo('python'))


# ejercicio 6
def suma_digitos(n):
    # caso base: si tiene un solo digito devuelve el numero
    if n < 10:
        return n
    # paso recursivo: suma el ultimo digito con el resto del numero
    return (n % 10) + suma_digitos(n // 10)

# print('la suma de los digitos de 1234 es:', suma_digitos(1234))
# print('la suma de los digitos de 9 es:', suma_digitos(9))
# print('la suma de los digitos de 305 es:', suma_digitos(305))


# ejercicio 7
def contar_bloques(n):
    # caso base: el primer nivel tiene un solo bloque
    if n == 1:
        return 1
    # paso recursivo: suma el nivel actual mas los anteriores
    return n + contar_bloques(n - 1)

# print('total de bloques para nivel 1:', contar_bloques(1))
# print('total de bloques para nivel 2:', contar_bloques(2))
# print('total de bloques para nivel 4:', contar_bloques(4))


# ejercicio 8
def contar_digito(numero, digito):
    # caso base: termina cuando nos quedamos sin numero
    if numero == 0:
        return 0
    # vale 1 si el ultimo digito coincide y 0 si no
    actual = 1 if (numero % 10) == digito else 0
    # paso recursivo: suma el actual y analiza el resto del numero
    return actual + contar_digito(numero // 10, digito)

# print('cantidad de veces que aparece el 2:', contar_digito(12233421, 2))
# print('cantidad de veces que aparece el 5:', contar_digito(5555, 5))
# print('cantidad de veces que aparece el 7:', contar_digito(123456, 7))