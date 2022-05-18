def calculate_shifts(key_char):
    return ord(key_char) - ord("a")

def encrypt_letter(char, shift):
    if char.isalpha():
        return chr((shift + ord(char) - ord("a")) % (ord("z") - ord("a") + 1) + ord("a"))
    return char

def encrypt_text(text, key):  
    i = 0
    encrypted_text = ""
    for char in text:
        if key != "":
            shift = calculate_shifts(key[i%len(key)])
        else: shift = 0
        encrypted_text += encrypt_letter(char, shift)
        i += 1
    return encrypted_text


plaintext = str.lower(input("Enter text to encrypt > "))
#plaintext = "PyThOn is BeauTiful".lower()

keystring = str.lower(input("Enter key to encrypt the text > "))
#keystring = "RandOm".lower()
#keystring = "".lower()

print(encrypt_text(plaintext, keystring))
#print(encrypt_text(plaintext, keystring) == "gygkcz if pqrugltgc")

# shifts first letter backwards in autotests WHY???????