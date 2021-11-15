import random
import time 
import src.settings

def genScramble():

    faces = ['R', 'L', 'U', "D", "F", "B"]

    scramble = []

    i = 1

    scramble_length = int(src.settings.read_conf("scramble", "scramble_length"))

    while i <= scramble_length:

        rate = int(src.settings.read_conf("scramble", "rate"))
        normal = int(src.settings.read_conf("scramble", "normal"))
        double = int(src.settings.read_conf("scramble", "double")) + normal
        prime = int(src.settings.read_conf("scramble", "prime")) + double

        move = faces[random.randint(0, len(faces) -1)]
        x = random.randint(0, rate)

        if x <= normal:
            add = ""
        elif normal < x <= double:
            add = "2"
        elif double < x <= prime:
            add = "\'"

        if len(scramble) == 0:
            scramble.append(str(move) + add)
            i = i+1

        if not move == scramble[len(scramble)-1][0]:
            scramble.append(str(move) + add)
            i = i+1

    return scramble

def timer(stdscr, startTime, clear):

    # Inspection Time

    inspection_time = int(src.settings.read_conf("timer", "inspection_time"))

    if not inspection_time == 0:
        print("Inspection Time...", end = "\n\r")

        while not time.time() > startTime + inspection_time:

            key = stdscr.getch()

            if key == ord(" "):
                break

            print("   " + str( inspection_time - int(time.time() - startTime)), end = "\r")

        if time.time() > startTime + inspection_time:
            return "None"
    
    clear()

    # Timer

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
        return str(solve_time)

    return str(solve_time)