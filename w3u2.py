emoji = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍"
}

phrase = input("Emotional phrase to parse: ")
output = []
#angry lion think he is a python

for word in phrase.split():
    if word in emoji.keys():
       #output.append(emoji.get(word))
       output.append(emoji[word])
    else: output.append(word)

print(*output, sep=' ')
#print (output)
    #' ', '!', '?', ',', '.', '-'