shift = input("shift (0-25): ")
while not(shift.isdecimal() and (int(shift)) in range(26)):
    print(shift, "is not a number between 0 and 25")
    shift = (input("shift (0-25): "))

plaintext = str.lower(input("Enter text to encrypt > "))
#plaintext = "programming: Python is fun!"

i = 0
encrypted = ""

for ltr in plaintext:
    if ltr.isalpha():
        if ord(ltr) + int(shift) <= ord("z"):
            encrypted += chr(ord(ltr) + int(shift))
        else:
            encrypted += chr(ord(ltr) + int(shift) - 26)
    else:
        encrypted += ltr
    i += 1

print(encrypted)