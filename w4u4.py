even = []

with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for n in lines:
        if int(n) % 2 == 0:
            even.append(n)
with open("even_numbers.txt", "w") as file:
    for n in even:
        file.write(n)
        
print("List of even numbers created!")


#with open("numbers.txt", "r") as file1:
 #   with open("even_numbers.txt", "w") as file2:    
  #      for line in file1:
   #         number = int(line)
    #        if number % 2 == 0:
     #           num = str(number) + "\n"
      #          file2.write(num)