import itertools
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

nums = [str(x) for x in range(10)]


def rating(guess, answer):
    bb = len(set(guess) & set(answer))
    aa = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            aa += 1
            bb -= 1
    return aa, bb


count_lst = []
for _ in tqdm(range(500)):
    lst = []
    for per in itertools.permutations(nums, 4):
        lst.append(''.join(per))
    answer = random.choice(lst)
    count = 0
    while True:
        count += 1
        guess = random.choice(lst)

        a, b = rating(guess, answer)

        if guess == answer:
            break

        lst_exc = []
        for i in lst:
            aa, bb = rating(i, guess)
            if (aa != a) or (bb != b):
                lst_exc.append(i)
        lst = list(set(lst) - set(lst_exc))
    count_lst.append(count)
plt.figure()
plt.hist(count_lst, bins=(max(count_lst) - min(count_lst) + 1))
plt.show()
