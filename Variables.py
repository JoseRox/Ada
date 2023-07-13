# Definir variables de cada tipo de primitivo
entero = 10234
flotante = 3.1433
caracter = 'AB'
booleano = False

# Concatenar las variables en una cadena
cadena = str(entero) + str(flotante) + caracter + str(booleano)

# Imprimir la cadena resultante
print(cadena)

# Límites de los enteros en Python
entero_maximo = 2 ** 31 - 1  # Límite máximo de un entero con signo de 32 bits
entero_minimo = -2 ** 31     # Límite mínimo de un entero con signo de 32 bits

# Límites de los flotantes en Python
flotante_maximo = 1.8 e 308   # Límite máximo de un flotante
flotante_minimo = -1.8 e 308  # Límite mínimo de un flotante

# Fórmula para la suma de los primeros n números pares
n = 5
suma_pares = n * (n + 1)

# Imprimir los resultados
print("Límite máximo de enteros:", entero_maximo)
print("Límite mínimo de enteros:", entero_minimo)
print("Límite máximo de flotantes:", flotante_maximo)
print("Límite mínimo de flotantes:", flotante_minimo)
print("Suma de los primeros", n, "números pares:", suma_pares)