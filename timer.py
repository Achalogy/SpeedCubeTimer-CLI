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

    print("TIMER")

    try:

        key = None
        num = 0 

        while True:
            num += 0.01
            key=stdscr.getch()
            if key == ord(" "):
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

    key = None
    return scramble

def stop():
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    raise SystemExit

def main():
    key = None
    while True:
        key=stdscr.getch()
        try:
            if key == ord(' '):
                # Envia el scramble
                print(" ".join(genScramble()))
                break
            elif key == ord('t'):
                try:
                    r = open('times.txt', 'r')

                    times = r.read().split("\n")

                    for time in times:
                        times[times.index(time)] = float(time)

                    print(times)

                    while True:
                        key = stdscr.getch()
                        try:
                            if key == ord(' '):
                                break
                            elif key == 27:
                                stop()
                        except KeyboardInterrupt:
                            stop()
                        
                    curses.echo()
                    curses.nocbreak()
                    curses.endwin()
                    main()

                except:
                    print("Not Solves avaliable")

            elif key == ord('c'):

                try:
                    os.remove('./times.txt')
                    print("Solves Erased")
                except:
                    print("Solves Don't exists")

                timeD.sleep(2)

                curses.echo()
                curses.nocbreak()
                curses.endwin()
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
        r = open('times.txt', 'r')
        f = open('times.txt', 'a')
        f.write("\n" + str(round(num,2)))
        f.close()
    except:
        f = open('times.txt', 'w')
        f.write(str(round(num,2)))
        f.close()
        r = open('times.txt', 'r')

    print("Time: " + str(round(num, 2)), end="\n")

    times = r.read().split("\n")

    for time in times:
        times[times.index(time)] = float(time)

    print("Last 5 Solves:")

    for x in range(1, 6):

        if not len(times) - x < 0:
            try:
                print(str(x) + ") " + str(times[len(times)-x]))
            except:
                pass

    while True:

        key = stdscr.getch()
        try:
            if key == ord(' '):
                curses.echo()
                curses.nocbreak()
                curses.endwin()
                main()
        except KeyboardInterrupt:
            stop()


    

if __name__ == "__main__":
    main()