import time as timeD
import datetime
import curses
import os
import random
import statistics

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

def getStats(times):
    
    stats = {}

    global_average = round(statistics.mean(times), 2)
    
    stats["average"] = {}
    stats["average"]["global"] = global_average    

    a3_current = []
    a5_current = []
    a12_current = []
    a100_current = []

    if len(times) >= 3:
        for x in range(1, 4):
            a3_current.append(times[len(times) - x])
        stats["a3"] = {}
        stats["a3"]["current"] = round(statistics.mean(a3_current), 2)

    if len(times) >= 5:
        for x in range(1, 6):
            a5_current.append(times[len(times) - x])
        stats["a5"] = {}
        stats["a5"]["current"] = round(statistics.mean(a5_current), 2)

    if len(times) >= 12:
        for x in range(1, 13):
            a12_current.append(times[len(times) - x])
        stats["a12"] = {}
        stats["a12"]["current"] = round(statistics.mean(a12_current), 2)

    if len(times) >= 100:
        for x in range(1, 101):
            a100_current.append(times[len(times) - x])
        stats["a100"] = {}
        stats["a100"]["current"] = round(statistics.mean(a100_current), 2)

    # Find the Better stats

    a3_times = []
    a5_times = []
    a12_times = []
    a100_times = []

    if len(times) >= 3:
        for x in range(1, len(times) -1 ):
            try:
                av3 = []

                for y in range(-1, 2):
                    av3.append(times[x + y])
            except:
                pass

            a3_times.append(round(statistics.mean(av3), 2))
        stats["a3"]["global"] = min(a3_times)

    if len(times) >= 5:
        for x in range(1, len(times) -1 ):
            try:
                av5 = []

                for y in range(-1, 4):
                    av5.append(times[x + y])
            except:
                pass

            a5_times.append(round(statistics.mean(av5), 2))
        stats["a5"]["global"] = min(a5_times)

    if len(times) >= 12:
        for x in range(1, len(times) -1 ):
            try:
                av12 = []

                for y in range(-1, 11):
                    av12.append(times[x + y])
            except:
                pass

            a12_times.append(round(statistics.mean(av12), 2))
        stats["a12"]["global"] = min(a12_times)

    if len(times) >= 100:
        for x in range(1, len(times) -1 ):
            try:
                av100 = []

                for y in range(-1, 99):
                    av100.append(times[x + y])
            except:
                pass

            a100_times.append(round(statistics.mean(av100), 2))
        stats["a100"]["global"] = min(a100_times)

    return stats 

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

                    stats = getStats(times)
                    print("Exit with Spacebar", end="\n\r")
                    print("")
                    print("           CURRENT      GLOBAL", end="\n\r")
                    print(" Average           "+ str(stats["average"]["global"]) , end="\n\r")

                    if len(times) >= 3:
                        print("      a3    "+ str(stats["a3"]["current"]) + "        " +  str(stats["a3"]["global"]), end="\n\r")
                    if len(times) >= 5:
                        print("      a5    "+ str(stats["a5"]["current"]) + "        " +  str(stats["a5"]["global"]), end="\n\r")
                    if len(times) >= 12:
                        print("     a12    "+ str(stats["a12"]["current"]) + "        " +  str(stats["a12"]["global"]), end="\n\r")
                    if len(times) >= 100:
                        print("    a100    "+ str(stats["a100"]["current"]) + "        " +  str(stats["a100"]["global"]), end="\n\r")
                    print("")
                    print("Total = " + str(len(times)), end = "\n\r")
                    print("")
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