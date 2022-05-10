#plaintext = "programming: Python is fun!"
#i = ord("a")
#while chr(i).isalpha():
#    plaintext += chr(i)
#    i += 1
#print(plaintext)

#shift = input("shift (0-25): ")
#while not(shift.isdecimal() and (int(shift)) in range(26)):
#    print(shift, "is not a number between 0 and 25")

plaintext = str.lower(input("Enter text to encrypt >"))

shift = (input("Enter a number to shift (will be converted to 0-25) >"))
while not(shift.isdecimal()):
    shift = (input("Enter number to shift (will be converted to 0-25) >"))
shift = int(shift)

if shift > ord("z") - ord("a"):
    shift = (shift % (ord("z") - ord("a")))
    print("the shift you entered has been converted to", shift)

i = 0
encrypted = ""

for ltr in plaintext:
    if ltr.isalpha():
        encrypted += chr((shift + ord(ltr) - ord("a")) % (ord("z") - ord("a") + 1) + ord("a"))
    else:
        encrypted += ltr
    i += 1
    
print(encrypted)