for i in range(1, 101):
    if i % 3 == 0:
        output = 'Fizz'
    elif i % 5 != 0:
        output = i
    if i % 5 == 0:
        output += 'Buzz'
    print(output)
    output = ''