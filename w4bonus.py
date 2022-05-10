draw = 0
win1 = 0
win2 = 0

with open("player1.txt") as p1:
    with open("player2.txt") as p2:
        option1 = p1.readlines()
        option2 = p2.readlines()
        if len(option1) < len(option2):
            counter = len(option1)
        else:
            counter = len(option2)
        for n in range(counter):
            if option1[n] == option2[n]:
                draw += 1 
            elif (option1[n] == 'R\n' and option2[n] == 'S\n')\
            or (option1[n] == 'P\n' and option2[n] == 'R\n')\
            or (option1[n] == 'S\n' and option2[n] == 'P\n'):
                win1 += 1
            else:
                win2 += 1

wins1 = ("Player1 wins: " + str(win1) + "\n")
wins2 = ("Player2 wins: " + str(win2) + "\n")
draws = ("Draws: " + str(draw) + "\n")

with open("result.txt", "w") as output:
    output.write(wins1)
    output.write(wins2)
    output.write(draws)