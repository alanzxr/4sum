import random
lst = [str(x) for x in range(10)]
answer = random.sample(lst, 4)
count = 0
cheat = False
while True:
    count += 1
    while True:
        guess = input('Input 4 digits:')
        if guess == 'whosyourdaddy':
            print('CHEATING', ''.join(answer))
            cheat = True
            break
        if (len(set(guess) & set(lst)) == 4):
            break
        print('Invalid Input. Retry.')
    if cheat:
        break
    b = len(set(guess) & set(answer))
    a = 0
    for i in range(4):
        if guess[i] == answer[i]:
            a += 1
            b -= 1
    if a == 4:
        print(f'[{count}] Congratulations!')
        break
    else:
        print(f'[{count}] {guess} {a}A{b}B')
