import itertools
import random
nums = [str(x) for x in range(10)]
lst = []
for per in itertools.permutations(nums, 4):
    lst.append(''.join(per))


def rating(guess, answer):
    bb = len(set(guess) & set(answer))
    aa = 0
    for i in range(4):
        if guess[i] == answer[i]:
            aa += 1
            bb -= 1
    return aa, bb


# answer = input('Input 4 digits:')
count = 0
while True:
    count += 1
    guess = random.choice(lst)
    print(f'[{count}] {guess} from {len(lst)}')

    # a, b = rating(guess, answer)
    while True:
        inp = input('?A?B:')
        if (len(inp) == 2) and (inp[0] in nums) and (inp[1] in nums) and (int(inp[0]) + int(inp[1]) <= 4):
            break
        else:
            print('Invalid Input. Retry.')
    a, b = [int(x) for x in list(inp)]

    print(f'[{count}] {guess} {a}A{b}B')

    if a == 4:
        print('FINISH.')
        break
    # if guess == answer:
    #     print('FINISH.')
    #     break

    lst_exc = []
    for i in lst:
        aa, bb = rating(i, guess)
        if (aa != a) or (bb != b):
            lst_exc.append(i)
    lst = list(set(lst) - set(lst_exc))
    if len(lst) == 0:
        print('Impossible.')
        break
