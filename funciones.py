import math


def greet():
    print("Hello word!")
    return


def greetName(name):
    print(f"Hola {name}")
    return


def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp


def iva(amount, vat=0.21):
    return amount + amount*vat


def circleArea(radius):
    return math.pi * radius**2


def cylinderedArea(radius, high):
    return 2 * circleArea(radius) + 2 * math.pi * radius*high


def squares(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list


def statistics(sample):
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(squares(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']--0.5
    return stat


def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n


def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater


def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)
