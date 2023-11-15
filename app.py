import random
options = ['rock', 'paper', 'scissors', 'quit', 'stats', 'help','play']
stats = {
    'wins': 0,
    'losses': 0,
    'ties': 0
}

def choose_winner(user_movement, computer_movement):
    if user_movement == computer_movement:
        return 'tie'
    elif user_movement == 'rock' and computer_movement == 'scissors':
        return 'user'
    elif user_movement == 'paper' and computer_movement == 'rock':
        return 'user'
    elif user_movement == 'scissors' and computer_movement == 'paper':
        return 'user'
    else:
        return 'computer'

def update_stats(winner):
    if winner == 'user':
        stats['wins'] += 1
    elif winner == 'computer':
        stats['losses'] += 1
    else:
        stats['ties'] += 1

print('Welcome to Rock Paper Scissors')

while True:
    print('Type one of the following options to play')
    print('[ quit - help - stats - play ]')
    user_input = input('\nSelect an option: ')

    if user_input not in options:
        print('Invalid input')
    else:
        if user_input == 'quit':
            break
        elif user_input == 'help':
            print('''Type correctly one of the following options to play
                play : to start the game
                quit : to exit the game
                help : to show this menu
                stats : to show the game stats
                ''')
        elif user_input == 'stats':
            print(stats, end='\n\n')
        elif user_input == 'play':

            user_movement = None
            while user_movement not in options[:-4]:
                print('''Type one of the following options to play
                    [ rock - paper - scissors]
                    ''')
                user_movement = input('type an option: ')
                if user_movement not in options[:-3]:
                    print('Invalid input\n')

            computer_movement = random.choice(options[:-3])
            winner = choose_winner(user_movement, computer_movement)

            print(f'You chose {user_movement} and the computer chose {computer_movement}')
            if winner == 'tie':
                print('\t It is a tie!!!\n')
            else:
                print(f'\nThe winner is {winner}!!!\n')
            update_stats(winner)
            user_movement = None


if stats['wins'] != 0 or stats['losses'] != 0 or stats['ties'] != 0:
    print(f'your score is: {stats}')
    if stats['wins'] > stats['losses']:
        print('Congratulations, You are the winner')
    elif stats['wins'] < stats['losses']:
        print('Each time you lose, you learn to play better')

print('Thanks for playing')