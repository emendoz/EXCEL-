""" Choose your own path - Dragon Realm Program """

import random, time

play = 'Y'
while play == 'Y':
    print('''You are in a land full of dragons. In front of you, you see two caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is greedy and hungry, and will eat you on sight.''')
    time.sleep(2)
    print()
    print('You approach the cave...')
    print('It is dark and spooky...')
    print()
    time.sleep(2)
    caveNumber = ''
    caveNumber = input('Which cave will you go into? (1 or 2): ')
    print()
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if caveNumber == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

    print("\n\n")
    play = input("Play again(Y/N): ")
    play = play.upper()

print("Game ended")
    