def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivo = arr[0]
    lowest = [i for i in arr[1:] if i <= pivo]
    highest = [i for i in arr[1:] if i > pivo]
    return quicksort(lowest) + [pivo] + quicksort(highest)

print(quicksort([10, 5, 2, 3, 5, 6, 7]))