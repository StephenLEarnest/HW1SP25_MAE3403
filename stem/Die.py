import random

def rollFairDie():
    # Generate a random floating point number between 0.0 and 1.0
    x = random.random()

    # Fair die, 6 equal intervals
    if x <= 1.0 / 6:
        return 1
    elif x <= 2.0 / 6:
        return 2
    elif x <= 3.0 / 6:
        return 3
    elif x <= 4.0 / 6:
        return 4
    elif x <= 5.0 / 6:
        return 5
    else:
        return 6

def rollUnFairDie():
    # Generate a random floating point number between 0.0 and 1.0
    x = random.random()

    # Unfair die, 1 has a larger chance (0.2), other numbers have smaller chances
    if x <= 0.2:
        return 1
    elif x <= 0.4:
        return 2
    elif x <= 0.6:
        return 3
    elif x <= 0.8:
        return 4
    elif x <= 0.9:
        return 5
    else:
        return 6