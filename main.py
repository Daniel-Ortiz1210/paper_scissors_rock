import random

movements = ['piedra', 'papel', 'tijera']
print('\nPiedra, papel o tijera vs una IA\n')
def game(movements):
    while True:
        user = input('You (pieda, papel, tijera): ').lower()
        ia = movements[random.randint(0, 2)]
        if user == movements[1] and ia == movements[0]:
            print('IA:', ia)
            print('¡Ganaste!')
            break
        elif user == movements[1] and ia == movements[2]:
            print('IA:', ia)
            print('¡Perdiste! :(')
            break    
        elif user == movements[1] and ia == movements[1]:
            print('IA:', ia)
            print('¡Empate! Jugamos de nuevo.')
            continue
        if user == movements[0] and ia == movements[2]:
            print('IA:', ia)
            print('¡Ganaste!')
            break
        elif user == movements[0] and ia == movements[1]:
            print('IA:', ia)
            print('¡Perdiste! :(')
            break    
        elif user == movements[0] and ia == movements[0]:
            print('IA:', ia)
            print('¡Empate! Jugamos de nuevo.')
            continue
        if user == movements[2] and ia == movements[1]:
            print('IA:', ia)
            print('¡Ganaste!')
            break
        elif user == movements[2] and ia == movements[0]:
            print('IA:', ia)
            print('¡Perdiste! :(')
            break    
        elif user == movements[2] and ia == movements[2]:
            print('IA:', ia)
            print('¡Empate! Jugamos de nuevo.')
            continue

game(movements)