def decres(i):
    print(i)
    if i <= 1:
        return
    decres(i - 1)
    
print(decres(5))