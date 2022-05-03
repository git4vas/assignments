
list = []

list.append(input("Please enter the given name of the student: "))
list.append(input("Please enter the surname of the student: "))
list.append(input("Please enter the filed of study of the student: "))

id = tuple(list)
print(id)

# ('Harry', 'Potter', 'Defence  Against the Dark Arts')
