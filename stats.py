import math


def mean(ser) -> float:
    length: int = len(ser)
    total: float = 0
    for number in ser:
        total += number
    return round(total / length, 3)


def variance(ser) -> float:
    length: int = len(ser)
    avg: float = mean(ser)
    total: float = 0
    for number in ser:
        total += (number - avg) ** 2
    return round(total / length, 3)


def standard_deviation(ser) -> float:
    return round(math.sqrt(variance(ser)), 3)


