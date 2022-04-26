star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

t = int(input("enter the trilogy No:"))
e = int(input("enter the episode No:"))

if t in (1, 2, 3):
    if e in (1, 2, 3): #if (t in (1, 2, 3) and e in (1, 2, 3)):
        t = t-1
        e = e-1
        print(star_wars_movies[t][e])
    else:#
        print("no such episode")#
else:#
    print("no such trilogy")#

# eval. does not accept more than one print, so commented out the marked lines