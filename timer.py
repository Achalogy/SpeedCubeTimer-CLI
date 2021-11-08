import time as timeD
import datetime
import curses
import os
import random
#from pynput import keyboard as kb

stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(1)

def timer():

    print("TIMER (Stop with any key)", end="\n\r\n")

    try:

        key = None
        num = 0 

        while True:
            num += 0.01
            key=stdscr.getch()
            if not key == -1:
                break 
            elif key == 27:
                stop()

            print(round(num, 2), end="\r")

            timeD.sleep(0.01)

        return num 
    except KeyboardInterrupt:
        stop()

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

def stop():
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    raise SystemExit

def reset():
    curses.endwin()
    curses.initscr()
def main():

    #curses.noecho()
    #curses.nocbreak()
    #curses.endwin()

    key=stdscr.getch()
    print('Spacebar: Send Scramble', end="\n\r")
    print('T: Show Solves', end="\n\r")
    print('C: Clear Solves', end="\n\r")
    print('esc: Exit', end="\n\r")    
    print('')
    while True:
        key=stdscr.getch()
        try:
            if key == ord(' '):
                curses.endwin()
                curses.initscr()

                # Envia el scramble
                print(" ".join(genScramble()), end="\n\r")
                break
            elif key == ord('t'):
                reset()
                try:
                    r = open('solves.txt', 'r')

                    times = r.read().split("\n")

                    for time in times:
                        times[times.index(time)] = float(time)

                    print("Exit with Spacebar", end="\n\r")
                    print("")
                    print(times, end="\n\r")

                    while True:
                        key = stdscr.getch()
                        try:
                            if key == ord(' '):
                                break
                            elif key == 27:
                                stop()
                        except KeyboardInterrupt:
                            stop()
                        
                    reset()
                    main()

                except:
                    print("Solves not avaliable")

                timeD.sleep(2)

                reset()
                main()

            elif key == ord('c'):

                try:
                    os.remove('./solves.txt')
                    print("Solves Erased")
                except:
                    print("Solves Don't exists")

                timeD.sleep(2)
                reset()
                main()

            elif key ==27:
                stop()
        except KeyboardInterrupt:
            stop()
    
    while True:
        key = stdscr.getch()
        try:
            if key == ord(' '):
                num = timer()
                break
            elif key == 27:
                stop()
        except KeyboardInterrupt:
            stop()


    try:
        r = open('solves.txt', 'r')
        f = open('solves.txt', 'a')
        f.write("\n" + str(round(num,2)))
        f.close()
    except:
        f = open('solves.txt', 'w')
        f.write(str(round(num,2)))
        f.close()
        r = open('solves.txt', 'r')

    print("TIME: " + str(round(num, 2)), end="\n\r\n")

    times = r.read().split("\n")

    for time in times:
        times[times.index(time)] = float(time)

    print("Last 5 Solves:", end="\n\r")

    curses.cbreak()

    for x in range(1, 6):

        if not len(times) - x < 0:
            try:
                print("  " + str(x) + ") " + str(times[len(times)-x]), end="\n\r")
            except:
                pass

    while True:

        key = stdscr.getch()
        try:
            if key == ord(' '):
                reset()
                main()
        except KeyboardInterrupt:
            stop()


    

if __name__ == "__main__":
    main()