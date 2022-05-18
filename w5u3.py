def is_even(number):
    return int(number) % 2 == 0
    
for n in range(100):
    if is_even(n):
        print(n, "is even")
    else:
        print(n, "is not even")