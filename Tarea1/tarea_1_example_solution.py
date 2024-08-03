# Autores: Marco Cambronero Villalobos y Cristhofer Loría Calderón
# Curso de Microcontroladores y Microprocesadores
# Tarea 1
# Verificación de funcionamiento de código mediante Pytest

def operation_selector(num1, num2, op):
    # Verificar que num1 y num2 sean números enteros:
    if not (isinstance(num1, int) and isinstance(num2, int)) \
            or (isinstance(num1, bool) or isinstance(num2, bool)):
        return -50, None
        # Código de error 1: num1 o num2 no es un número entero

    # Verificar que op sea de tipo string:
    if not isinstance(op, str):
        return -60, None  # Código de error 2: op no es de tipo string

    # Verificar que op sea alguna de las 4 opciones permitidas
    if op not in ['+', '-', '*', '&']:
        return -70, None
        # Código de error 3: op no es una de las opciones permitidas

    # Realizar la operación según el valor de op
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '&':
        resultado = num1 & num2
    return 0, resultado  # Código de éxito 0: Operación exitosa


def calculo_promedio(lista_valores):
    # Verificar que todos los elementos en la lista sean números
    for valor in lista_valores:
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return -80, None  # Código de error 1: Un elemento no es un número

    # Verificar que el tamaño de la lista no sea mayor a 10 elementos
    if len(lista_valores) > 10:
        return -90, None
        # Código de error 2: La lista tiene más de 10 elementos

    # Calcular el promedio
    promedio = sum(lista_valores) / len(lista_valores)
    return 0, promedio  # Código de éxito 0: Cálculo exitoso
