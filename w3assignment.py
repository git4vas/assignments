#plaintext = input("text")
#shift = input("shift")

plaintext = "programming python is fun!"
shift = 5

dictionary = {" ": " ", ",": ",", ".": ".", "!": "!", "?": "?", "-": "-"}
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