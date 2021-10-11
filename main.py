import random

movements = ['piedra', 'papel', 'tijeras']
def game(movements):
    while True:
        ia = movements[random.randint(len(movements))]
        user = input('Haz un movimiento: ').lower()
        