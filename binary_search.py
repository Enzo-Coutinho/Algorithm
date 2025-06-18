
print("Program of binary search")

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        meio = (low + high) // 2
        number = list[meio]
        if number == item:
            return number
        if number > item:
            high = meio - 1
        else:
            low = meio + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 6))
print(binary_search(my_list, -1))