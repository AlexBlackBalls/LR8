import random


def replace_zeros_with_negative(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = random.randint(-100, -1)


def replace_even_with_reciprocal(lst):
    for i in range(len(lst)):
        if lst[i] != 0 and lst[i] % 2 == 0:
            lst[i] = 1 / lst[i]


if __name__ == '__main__':
    numbers = [4, 0, -3, 7, 0, -6, 5, 10, 0, 2]

    first = numbers.copy()
    print('Исходный список:', numbers)
    replace_zeros_with_negative(first)
    print('4.1. Нули заменены:', first)

    second = numbers.copy()
    replace_even_with_reciprocal(second)
    print('4.2. Четные заменены на обратные:', second)
