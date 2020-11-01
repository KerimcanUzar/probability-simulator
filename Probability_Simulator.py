play = True
while play:
    sides = int (input("\nHow many sides your dice have? (max 10)\n\n"))
    dices = int (input("\nHow many dices you want to roll?\n\n"))
    times = int (input("\nHow many times you want to repeat it?\n\n"))
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    s0 = 0
    import random
    for x in range (0,times):
        for y in range (0,dices):
            roll = random.randint(1,sides)
            if roll == 1: s1 = s1+1
            if roll == 2: s2 = s2+1
            if roll == 3: s3 = s3+1
            if roll == 4: s4 = s4+1
            if roll == 5: s5 = s5+1
            if roll == 6: s6 = s6+1
            if roll == 7: s7 = s7+1
            if roll == 8: s8 = s8+1
            if roll == 9: s9 = s9+1
            if roll == 10: s0 = s0+1
    print ("\nYour rolls:\n1: " + str(s1) + "\n2: " + str(s2) + "\n3: " + str(s3) + "\n4: " + str(s4) + "\n5: " + str(s5) + "\n6: " + str(s6) + "\n7: " + str(s7) + "\n8: " + str(s8) + "\n9: " + str(s9) + "\n10: " + str(s0) + "\n\n")
    z = str (input("\nDo you want to try again? (y/n)\n\n"))
    if z == "y": play = True
    if z == "n": play = False
