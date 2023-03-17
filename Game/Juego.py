import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Opción incorrecta')
        return None, None

    computer_option = random.choice(options)
    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:
        print('Empate')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Ganaste')
            user_wins += 1

        else:
            print('Perdiste')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('Perdiste')
            computer_wins += 1

        else:
            print('Ganaste')
            user_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'piedra':
            print('Perdiste')
            computer_wins += 1

        else:
            print('Ganaste')
            user_wins += 1
            
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        
        print('*' * 10)
        print('Round: ', rounds)
        print('*' * 10)

        print('Computer wins = ', computer_wins)
        print('User wins = ', user_wins)
        rounds += 1

        user_options, computer_options = choose_options()
        user_wins, computer_wins = check_rules(user_options, computer_options, user_wins, computer_wins)
        
        if computer_wins == 2:
            print('El ganador es la computadora')
            
            break

        if user_wins == 2:
            print('El ganador es usted')

            break


run_game()