import random

user_hand = None
draw, loss, win = {}, {}, {}

resp = {
    'win': lambda: f'Sorry, but the computer chose {random.choice(win[user_hand])}',
    'draw': lambda: f'There is a draw ({draw[user_hand][0]})',
    'loss': lambda: f'Well done. The computer chose {random.choice(loss[user_hand])} and failed'
}

# user score based on computer results
score = {
    'win': 0,
    'draw': 50,
    'loss': 100,
}

rating = 0
wins, draws = 0, 0
all_hands = []
if __name__ == '__main__':
    user = input('Enter your name: ')
    print(f'Hello, {user}!')
    with open('rating.txt', 'r') as file:
        for line in file:
            name, load_score = line.split()
            if name == user:
                rating = int(load_score)

    all_hands = input().split(',')
    if all_hands == ['']:
        all_hands = ['rock', 'paper', 'scissors']

    n = len(all_hands)
    if n % 2 == 0:
        raise ValueError('List length must be odd.')
    half = n // 2
    for mid, h in enumerate(all_hands):
        draw[h] = [h]
        win[h] = [all_hands[(mid+i)%n] for i in range(1, half+1)]
        loss[h] = [all_hands[(mid+i)%n] for i in range(-half, 0)]

    print("Okay, let's start")
    while True:
        match input():
            case '!exit':
                print('Bye!')
                break
            case '!rating':
                print(f'Your rating: {rating}')
            case hand if hand in all_hands:
                user_hand = hand
                choice = random.choice(['draw', 'loss', 'win'])
                if choice == 'draw':
                    draws += 1
                elif choice == 'loss':
                    wins += 1
                rating += score[choice]
                print(resp[choice]())
            case _:
                print('Invalid input')

    # print(wins, draws, wins*100, draws*50, wins*100 + draws*50)
