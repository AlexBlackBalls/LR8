def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    less = []
    equal = []
    greater = []
    for x in lst:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == '__main__':
    data = [7, -3, 0, 12, 5, -8, 5, 20, 1]
    print('Список:', data)

    print('5.1. Линейный поиск числа 12:', linear_search(data, 12))
    print('5.1. Линейный поиск числа 99:', linear_search(data, 99))

    sorted_data = data.copy()
    selection_sort(sorted_data)
    print('5.3. Сортировка выбором:', sorted_data)

    print('5.2. Бинарный поиск числа 12 в отсортированном списке:',
          binary_search(sorted_data, 12))
    print('5.2. Бинарный поиск числа 99:', binary_search(sorted_data, 99))

    print('5.4. Быстрая сортировка:', quick_sort(data))
