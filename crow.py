import sys
from random import randint

sys.setrecursionlimit(10000)
pre_clac_p = {}
dice_sides = 6


def get_win_probabiltiy(fruit_left, steps_left, depth=0):
    # pre-calc
    cur_tupple = (tuple(fruit_left), steps_left)
    if cur_tupple in pre_clac_p:
        return pre_clac_p[cur_tupple]
    # loose check
    if steps_left == 0:
        pre_clac_p[cur_tupple] = 0.
        # print(len(pre_clac_p), depth)
        return 0.
    # win check
    max_ind = 0
    total_left = 0
    for i, f_c in enumerate(fruit_left):
        if f_c > fruit_left[max_ind]:
            max_ind = i
        total_left += f_c
    # print('left ', total_left)
    if fruit_left[max_ind] == 0:
        pre_clac_p[cur_tupple] = 1.
        # print(len(pre_clac_p), depth)
        return 1.

    expexted = 0
    # crow
    expexted += get_win_probabiltiy(fruit_left, steps_left-1)
    # wild card
    fruit_left[max_ind] -= 1
    expexted += get_win_probabiltiy(fruit_left, steps_left, depth+1)
    fruit_left[max_ind] += 1
    return_count = 0.
    for outcome in range(len(fruit_left)):
        if fruit_left[outcome] > 0:
            fruit_left[outcome] -= 1
            win_p = get_win_probabiltiy(fruit_left, steps_left, depth + 1)
            # print('returned', win_p)
            expexted += win_p
            fruit_left[outcome] += 1
        else:
            return_count += 1
    final = expexted / dice_sides / (1 - return_count / dice_sides)
    pre_clac_p[cur_tupple] = final
    # print(len(pre_clac_p), depth)
    return final


if __name__ == '__main__':
    print(get_win_probabiltiy([4, 4, 4, 4], 6))
    print(get_win_probabiltiy([2, 2, 2, 2], 3))
    best = 1.
    best_tuple = 0
    min_crow_steps = 3
    for i in range(100500):
        rand_fruit = randint(0, 4)
        # my_list = [randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4)]
        my_list = [rand_fruit, rand_fruit, rand_fruit, rand_fruit]
        my_crow = randint(min_crow_steps, 6)
        result = get_win_probabiltiy(my_list, my_crow)
        if abs(result - 0.5) < best - 1e-7:
            best_tuple = (my_list, my_crow)
            best = abs(result - 0.5)
    print(best_tuple, get_win_probabiltiy(best_tuple[0], best_tuple[1]))
    # print(pre_clac_p)

