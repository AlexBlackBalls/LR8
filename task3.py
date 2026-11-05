def sum_after_first_max(lst):
    if len(lst) == 0:
        return 0
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    total = 0
    for i in range(max_index + 1, len(lst)):
        total += lst[i]
    return total


def product_after_penultimate_negative(lst):
    negatives_found = 0
    penultimate_index = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            negatives_found += 1
            if negatives_found == 2:
                penultimate_index = i
                break
    if penultimate_index == -1:
        return None
    result = 1
    for i in range(penultimate_index + 1, len(lst)):
        result *= lst[i]
    return result


if __name__ == '__main__':
    numbers = [4, -2, 9, 3, 0, 9, -5, 6, -1, 8]
    print('Список:', numbers)
    print('3.1. Сумма после первого максимума:', sum_after_first_max(numbers))
    result = product_after_penultimate_negative(numbers)
    if result is None:
        print('3.2. Отрицательных элементов меньше двух')
    else:
        print('3.2. Произведение правее предпоследнего отрицательного:', result)
