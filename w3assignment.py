plaintext = str.lower(input("Enter text to encrypt > "))
#plaintext = "programming: Python is fun!"
encrypted = ""
#shift = input("shift: ")
shift = 5
i = 0

for ltr in plaintext:
    if ltr.isalpha():
        if ord(ltr) + shift <= ord("z"):
            encrypted += chr(ord(ltr) + shift)
        else:
            encrypted += chr(ord(ltr) + shift - 26)
    else:
        encrypted += ltr
    i += 1

#dictionary = {" ": " ", ",": ",", ".": ".", "!": "!", "?": "?", "-": "-", ";": ";", ":": ":"}
#letters = "abcdefghijklmnopqrstuvwxyz"
#print(len(letters))
#for ltr in letters:
#    if i + shift + 1 <= len(letters):
#        dictionary[ltr] = letters[(i + shift)]
#    else:
#        dictionary[ltr] = letters[(i - len(letters) + shift)]
#    i += 1
#print(dictionary)
#for ltr in plaintext:
#    encrypted = encrypted + dictionary[ltr]

print(encrypted)
