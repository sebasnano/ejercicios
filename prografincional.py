def discount(value, discount):
    return value - value * discount/100


def iva(value, vat):
    return value + value * vat/100


def priceBasket(basket, funtion):
    total = 0
    for value, discount in basket.items():
        total += funtion(value, discount)
    return total

