import math


def summ(x: int, y: int) -> float:
    """
    Function get two integer numbers and return sum
    :param x: int
    :param y: int
    :return: float
    """
    return float(x + y)


def nod(x, y):
    """
    Notation: возвращает наибольший общий делитель
    :param x: int
    :param y: int
    :return: nod
    """
    return math.gcd(x, y)

def nom(x, y):
    """
    Notation: возвращает наименьший общий множитель
    :param x: int
    :param y: int
    :return: nom
    """
    return math.lcm(x, y)


x = 6
y = 32
print(nod(x, y))
print(nom(x, y))
