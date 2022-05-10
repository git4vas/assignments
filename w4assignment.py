row = ""
x = 0

with open("key.txt") as key:
    xy = [int(n) for n in key.readlines()]
with open("secret.txt") as secret:
    for line in secret:
        row += line.strip()
with open("public.txt", "w") as public:
    for col in range(xy[1]):
        public.write(row[x:(x+xy[0])]+"\n")
        x += xy[0]