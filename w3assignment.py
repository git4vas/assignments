plaintext = str.lower(input("Enter text to encrypt > "))
#plaintext = "programming python is fun!"

#shift = input("shift: ")
shift = 5

dictionary = {" ": " ", ",": ",", ".": ".", "!": "!", "?": "?", "-": "-", ";": ";", ":": ":"}
encrypted = ""
letters = "abcdefghijklmnopqrstuvwxyz"
i = 0
j = 0
k = 0
l = 0

#print(len(letters))

for ltr in letters:
    if i + shift + 1 <= len(letters):
        dictionary[ltr] = letters[(i + shift)]
    else:
        dictionary[ltr] = letters[(i - len(letters) + shift)]
    i += 1
#print(dictionary)

for ltr in plaintext:
    encrypted = encrypted + dictionary[ltr]
print(encrypted)
