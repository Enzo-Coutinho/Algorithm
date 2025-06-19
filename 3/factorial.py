def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)
    
def sum_without_recursion(arr):
    total = 0
    for x in arr:
        total += x
    return total


def sum_with_recursion(arr):
    if arr == []:
        return 0
    return arr[0] + sum_with_recursion(arr[1:])


def count_numbers(arr):
    if arr == []:
        return 0
    return 1 + count_numbers(arr[1:])


def max_value(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_value(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max_value([1, 2, 3, 4, 10]))