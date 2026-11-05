def count_less_than(lst, c):
    count = 0
    for x in lst:
        if x < c:
            count += 1
    return count


def sum_of_abs(lst):
    total = 0
    for x in lst:
        total += abs(x)
    return total


def product_odd_positions(lst):
    result = 1
    for i in range(0, len(lst), 2):
        result *= lst[i]
    return result


if __name__ == '__main__':
    numbers = [3.5, -2.0, 1.5, 0.0, -4.25, 7.0, 2.0, -1.5]
    print('Список:', numbers)

    c = float(input('Введите число C: '))
    print('1.1. Элементов меньше C:', count_less_than(numbers, c))
    print('1.2. Сумма модулей:', sum_of_abs(numbers))
    print('1.3. Произведение элементов с нечетными номерами:',
          product_odd_positions(numbers))
