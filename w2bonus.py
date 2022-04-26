for i in range(1, 101):
    if i % 3 == 0:
        output = 'Fizz'
    elif i % 5 != 0:
        output = i
    if i % 5 == 0:
        output += 'Buzz'
    print(output)
    output = ''

#test it with comprehension
#i = list(range(1, 101))
#j = [i for i in i if (i % 5 and i % 3)!=0]
#print(j)