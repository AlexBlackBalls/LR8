def move_positives_first(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] > 0:
            left += 1
        elif lst[right] <= 0:
            right -= 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    numbers = [-1.5, 2.0, 0.0, 3.7, -4.2, 5.1, 0.0, -0.5, 8.0]
    print('Исходный список:', numbers)
    move_positives_first(numbers)
    print('Результат:      ', numbers)
