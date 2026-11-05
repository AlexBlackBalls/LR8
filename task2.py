def count_and_sum_abs(lst, c):
    less_than_c = [x for x in lst if x < c]
    abs_values = [abs(x) for x in lst]
    return len(less_than_c), sum(abs_values)


if __name__ == '__main__':
    numbers = [3.5, -2.0, 1.5, 0.0, -4.25, 7.0, 2.0, -1.5]
    print('Список:', numbers)

    c = float(input('Введите число C: '))
    count, total = count_and_sum_abs(numbers, c)
    print('1.1. Элементов меньше C:', count)
    print('1.2. Сумма модулей:', total)
