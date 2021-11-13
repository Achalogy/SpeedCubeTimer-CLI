import random
import time 

def genScramble():

    faces = ['R', 'L', 'U', "D", "F", "B"]

    scramble = []

    i = 1

    while i <= 20:

        move = faces[random.randint(0, len(faces) -1)]
        x = random.randint(0, 4)

        if x == 3:
            add = "\'"
        elif x == 4:
            add = "2"
        else:
            add = ""

        if len(scramble) == 0:
            scramble.append(str(move) + add)
            i = i+1

        if not move == scramble[len(scramble)-1][0]:
            scramble.append(str(move) + add)
            i = i+1

    return scramble

def timer(stdscr, startTime):

    print("TIMER (Stop with any key)", end="\n\r\n")
    print("")

    solve_time = None

    try:
        key = None
        while True:
            key=stdscr.getch()

            if not key == -1: # Pausar con cualquier tecla
                if not key == 27:
                    solve_time = round(time.time() - startTime, 2)
                break
            elif key == 27:
                break
            
            print("   " + str(round(time.time() - startTime, 2)), end = "\r")
                
    except KeyboardInterrupt:
        return solve_time

    return str(solve_time)