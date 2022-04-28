array = list(map(int, input('Введите последовательность чисел через пробел = ').split(' ')))  # ввод чисел через пробел


def quick_sort(array):
    if len(array) <= 1:
        return array

    element = array[0]
    left = list(filter(lambda x: x < element, array))
    center = [i for i in array if i == element]
    right = list(filter(lambda x: x > element, array))

    return quick_sort(left) + center + quick_sort(right)


def binary_search(my_array, num, left, right):
    if left > right:
        return False

    middle = (left + right) // 2
    if my_array[middle] < num <= my_array[middle + 1]:
        return middle
    elif num <= my_array[middle]:
        return binary_search(my_array, num, left, middle - 1)
    else:
        return binary_search(my_array, num, middle + 1, right)


my_array = quick_sort(array)
print(my_array)
left = 0
right = len(my_array)-1
num = int(input("Введите любое целое число = "))

if num <= my_array[left] or num >= my_array[right]:
    print('Условия не выполнены. Выход за границы списка.')
else:
    print("Индекс мин.элемента {}: {}".format(my_array[binary_search(my_array, num, left, right)], binary_search(my_array, num, left, right)))
    print("Индекс макс.элемента {}: {}".format(my_array[binary_search(my_array, num, left, right)+1], binary_search(my_array, num, left, right)+1))




