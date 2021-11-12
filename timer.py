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

def timer(startTime):

    print("TIMER (Stop with any key)", end="\n\r\n")

    try:
        key = None
        while True:
            key=stdscr.getch()
            if not key == -1:
                break 
            elif key == 27:
                stop()
            
            print(round(timeD.time() - startTime, 2),  end = "\r")
                
    except KeyboardInterrupt:
        stop()

    return timeD.time()

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

def printCube(w, y, r, o, b, g):

    print("")
    print("\033[30;40m" + "                " + w[0][0] + " " + w[0][1] + " " +  w[0][2], end= " \n\r")
    print("\033[30;40m" + "                " + w[1][0] + " " + w[1][1] + " " +  w[1][2], end= " \n\r")
    print("\033[30;40m" + "                " + w[2][0] + " " + w[2][1] + " " +  w[2][2], end= " \n\r")    
    print("", end= "\n\r")
    print("\033[30;40m" + "    " + o[0][0] + " " + o[0][1] + " " + (o[0][2] + " ") + "\033[30;40m" + "   " + g[0][0] + " " + g[0][1] + " " + (g[0][2] + " ") + "\033[30;40m" + "   " + r[0][0] + " " + r[0][1] + " " + (r[0][2] + " ") + "\033[30;40m" + "   " + b[0][0] + " " + b[0][1] + " " + b[0][2], end= " \n\r")
    print("\033[30;40m" + "    " + o[1][0] + " " + o[1][1] + " " + (o[1][2] + " ") + "\033[30;40m" + "   " + g[1][0] + " " + g[1][1] + " " + (g[1][2] + " ") + "\033[30;40m" + "   " + r[1][0] + " " + r[1][1] + " " + (r[1][2] + " ") + "\033[30;40m" + "   " + b[1][0] + " " + b[1][1] + " " + b[1][2], end= " \n\r")
    print("\033[30;40m" + "    " + o[2][0] + " " + o[2][1] + " " + (o[2][2] + " ") + "\033[30;40m" + "   " + g[2][0] + " " + g[2][1] + " " + (g[2][2] + " ") + "\033[30;40m" + "   " + r[2][0] + " " + r[2][1] + " " + (r[2][2] + " ") + "\033[30;40m" + "   " + b[2][0] + " " + b[2][1] + " " + b[2][2], end= " \n\r")
    print("", end= "\n\r")
    print("\033[30;40m" + "                " + y[0][0] + " " + y[0][1] + " " + y[0][2], end= " \n\r")
    print("\033[30;40m" + "                " + y[1][0] + " " + y[1][1] + " " + y[1][2], end= " \n\r")
    print("\033[30;40m" + "                " + y[2][0] + " " + y[2][1] + " " + y[2][2], end= " \033[0;40m\n\r")    
    print("")

def simulate(s):
    """

    Cube Should Looks like this

            W W W
            W W W
            W W W
            
    O O O   G G G   R R R   B B B
    O O O   G G G   R R R   B B B
    O O O   G G G   R R R   B B B

            Y Y Y
            Y Y Y
            Y Y Y

    """

    white =  [["\033[30;47m" + " W", "\033[30;47m" + " W", "\033[30;47m" + " W"],["\033[30;47m" + " W", "\033[30;47m" +" W", "\033[30;47m" +" W"],["\033[30;47m" +" W", "\033[30;47m" +" W", "\033[30;47m" +" W"]]
    yellow = [["\033[30;43m" + " Y", "\033[30;43m" + " Y", "\033[30;43m" + " Y"],["\033[30;43m" + " Y", "\033[30;43m" +" Y", "\033[30;43m" +" Y"],["\033[30;43m" +" Y", "\033[30;43m" +" Y", "\033[30;43m" +" Y"]]
    red =    [["\033[30;45m" + " R", "\033[30;45m" + " R", "\033[30;45m" + " R"],["\033[30;45m" + " R", "\033[30;45m" +" R", "\033[30;45m" +" R"],["\033[30;45m" +" R", "\033[30;45m" +" R", "\033[30;45m" +" R"]]
    orange = [["\033[30;41m" + " O", "\033[30;41m" + " O", "\033[30;41m" + " O"],["\033[30;41m" + " O", "\033[30;41m" +" O", "\033[30;41m" +" O"],["\033[30;41m" +" O", "\033[30;41m" +" O", "\033[30;41m" +" O"]]
    blue =   [["\033[30;46m" + " B", "\033[30;46m" + " B", "\033[30;46m" + " B"],["\033[30;46m" + " B", "\033[30;46m" +" B", "\033[30;46m" +" B"],["\033[30;46m" +" B", "\033[30;46m" +" B", "\033[30;46m" +" B"]]
    green =  [["\033[30;42m" + " G", "\033[30;42m" + " G", "\033[30;42m" + " G"],["\033[30;42m" + " G", "\033[30;42m" +" G", "\033[30;42m" +" G"],["\033[30;42m" +" G", "\033[30;42m" +" G", "\033[30;42m" +" G"]]

    def R_L (o,c):

        m1 = []
        m2 = []
        m3 = []
        m4 = []
        r = []

        def rotate(l, w, rl):
            
            if l == "R":
                
                l = red
            
            elif l == "L":
            
                l = orange

            if w == False:
                
                l[0][2] = rl[0][0]
                l[1][2] = rl[0][1]
                l[2][2] = rl[0][2]

                l[2][1] = rl[1][2]
                l[2][0] = rl[2][2]
                                    
                l[1][0] = rl[2][1]
                l[0][0] = rl[2][0]

                l[0][1] = rl[1][0]

            elif w == True:
                l[0][0] = rl[0][2]
                l[0][1] = rl[1][2]
                l[0][2] = rl[2][2]

                l[0][2] = rl[2][2]
                l[1][2] = rl[2][1]
                l[2][2] = rl[2][0]
                                    
                l[2][2] = rl[2][0]
                l[2][1] = rl[1][0]
                l[2][0] = rl[0][0]

                l[1][0] = rl[0][1]
                    

        if o == "R":
            pieces = [2, 0]

            for x in range(0, 3):
                m1.append(white[x][pieces[0]])
                m2.append(green[x][pieces[0]])
                m3.append(yellow[x][pieces[0]])
                m4.append(blue[x][pieces[1]])
            
            for x_red in red:
                
                apnd = []

                for x_x_red in x_red:
                    apnd.append(x_x_red)
                
                r.append(apnd)

        
        elif o == "L":
            pieces = [0, 2]

            for x in range(0, 3):
                m1.append(yellow[x][pieces[0]])
                m2.append(blue[x][pieces[1]])
                m3.append(white[x][pieces[0]])
                m4.append(green[x][pieces[0]])

            for l_orange in orange:
                
                apnd = []

                for l_l_orange in l_orange:
                    apnd.append(l_l_orange)
                
                r.append(apnd)
        
        rotate(o,c,r)

        if c == False:

            m1.reverse()

            if o == "R":
                m4.reverse()

            if o == "L":
                m2.reverse()

            for x in range(0, 3):
                white[x][pieces[0]] = m2[x]
                green[x][pieces[0]] = m3[x]
                yellow[x][pieces[0]] = m4[x]
                blue[x][pieces[1]] = m1[x]

        else:

            m3.reverse()

            if o == "L":
                m2.reverse()

            if o == "R":
                m4.reverse()

            for x in range(0, 3):
                white[x][pieces[0]] = m4[x]
                green[x][pieces[0]] = m1[x]
                yellow[x][pieces[0]] = m2[x]
                blue[x][pieces[1]] = m3[x]

    def U_D (o,c):
        m1 = []
        m2 = []
        m3 = []
        m4 = []
        r = []

        def rotate(l, w, rl):

            if l == "U":
                l = white
            elif l == "D":
                l = yellow

            if w == False:
                
                l[0][2] = rl[0][0]
                l[1][2] = rl[0][1]
                l[2][2] = rl[0][2]

                l[2][1] = rl[1][2]
                l[2][0] = rl[2][2]
                                    
                l[1][0] = rl[2][1]
                l[0][0] = rl[2][0]

                l[0][1] = rl[1][0]

            elif w == True:
                l[0][0] = rl[0][2]
                l[0][1] = rl[1][2]
                l[0][2] = rl[2][2]

                l[0][2] = rl[2][2]
                l[1][2] = rl[2][1]
                l[2][2] = rl[2][0]
                                    
                l[2][2] = rl[2][0]
                l[2][1] = rl[1][0]
                l[2][0] = rl[0][0]

                l[1][0] = rl[0][1]

        layer = 0

        if o == "U":
            layer = 0
            for x_white in white:
                appnd = []
                
                for x_x_white in x_white:
                    appnd.append(x_x_white)
                
                r.append(appnd)

        elif o == "D":
            layer = 2
            for x_yellow in yellow:
                appnd = []
                
                for x_x_yellow in x_yellow:
                    appnd.append(x_x_yellow)
                
                r.append(appnd)

        m1.append(green[layer])
        m2.append(red[layer])
        m3.append(orange[layer])
        m4.append(blue[layer])
        
        if c == False:

            if o == "U":
                orange[layer] = m1[0]
                green[layer] = m2[0]
                red[layer] = m4[0]
                blue[layer] = m3[0]
            elif o == "D":
                orange[layer] = m4[0]
                green[layer] = m3[0]
                red[layer] = m1[0]
                blue[layer] = m2[0]                
        
        elif c == True:

            if o == "U":
                orange[layer] = m4[0]
                green[layer] = m3[0]
                red[layer] = m1[0]
                blue[layer] = m2[0]
            elif o == "D":
                orange[layer] = m1[0]
                green[layer] = m2[0]
                red[layer] = m4[0]
                blue[layer] = m3[0]                

        rotate(o,c,r)

    def F_B (o,c):

        m1 = []
        m2 = []
        m3 = []
        m4 = []
        r = []        

        def rotate(l, w):

            rl = []

            if l == "F":
                l = green

                for x_green in green:
                    appnd = []

                    for x_x_green in x_green:
                        appnd.append(x_x_green)

                    rl.append(appnd)

            elif l == "B":
                l = blue

                for x_blue in blue:
                    appnd = []

                    for x_x_blue in x_blue:
                        appnd.append(x_x_blue)

                    rl.append(appnd)

            if w == False:
                
                l[0][2] = rl[0][0]
                l[1][2] = rl[0][1]
                l[2][2] = rl[0][2]

                l[2][1] = rl[1][2]
                l[2][0] = rl[2][2]
                                    
                l[1][0] = rl[2][1]
                l[0][0] = rl[2][0]

                l[0][1] = rl[1][0]

            elif w == True:
                l[0][0] = rl[0][2]
                l[0][1] = rl[1][2]
                l[0][2] = rl[2][2]

                l[0][2] = rl[2][2]
                l[1][2] = rl[2][1]
                l[2][2] = rl[2][0]
                                    
                l[2][2] = rl[2][0]
                l[2][1] = rl[1][0]
                l[2][0] = rl[0][0]

                l[1][0] = rl[0][1]

        layer = 0

        if o == "F":
            layer = 0
        elif o == "B":
            layer = 2

        if o == "F":

            m1.append(white[2])
            m2.append([red[0][0], red[1][0], red[2][0]])
            m3.append(yellow[0])
            m4.append([orange[0][2], orange[1][2], orange[2][2]])

            if c == False:

                m4[0].reverse()
                m2[0].reverse()

                white[2] = m4[0]
                red[0][0] = m1[0][0]
                red[1][0] = m1[0][1]
                red[2][0] = m1[0][2]
                yellow[0] = m2[0]
                orange[0][2] = m3[0][0]
                orange[1][2] = m3[0][1]
                orange[2][2] = m3[0][2]

            elif c == True:

                m1[0].reverse()
                m3[0].reverse()

                white[2] = m2[0]
                red[0][0] = m3[0][0]
                red[1][0] = m3[0][1]
                red[2][0] = m3[0][2]
                yellow[0] = m4[0]
                orange[0][2] = m1[0][0]
                orange[1][2] = m1[0][1]
                orange[2][2] = m1[0][2]            

            rotate(o, c)

        elif o == "B":

            m1.append(white[0])
            m2.append([red[0][2], red[1][2], red[2][2]])
            m3.append(yellow[2])
            m4.append([orange[0][0], orange[1][0], orange[2][0]])

            if c == False:

                m3[0].reverse()
                m1[0].reverse()

                white[0] = m2[0]
                red[0][2] = m3[0][0]
                red[1][2] = m3[0][1]
                red[2][2] = m3[0][2]
                yellow[2] = m4[0]
                orange[0][0] = m1[0][0]
                orange[1][0] = m1[0][1]
                orange[2][0] = m1[0][2]

            elif c == True:

                m2[0].reverse()
                m4[0].reverse()

                white[0] = m4[0]
                red[0][2] = m1[0][0]
                red[1][2] = m1[0][1]
                red[2][2] = m1[0][2]
                yellow[2] = m2[0]
                orange[0][0] = m3[0][0]
                orange[1][0] = m3[0][1]
                orange[2][0] = m3[0][2]

            rotate(o, c)

    for move in s:

        clockwise = False


        if len(move) > 1:

            clockwise = True

        if move[0] == "R" or move[0] == "L":

            try:

                if move[1] == "2":
                    R_L(move[0], clockwise)
                    R_L(move[0], clockwise)
                else:
                    R_L(move[0], clockwise)

            except:
                    R_L(move[0], clockwise)

        elif move[0] == "U" or move[0] == "D":

            try:

                if move[1] == "2":

                    U_D(move[0], clockwise)
                    U_D(move[0], clockwise)

                else:
                    U_D(move[0], clockwise)
            
            except:
                
                U_D(move[0], clockwise)

        elif move[0] == "F" or move[0] == "B":

            try:

                if move[1] == "2":
                    F_B(move[0], clockwise)
                    F_B(move[0], clockwise)
                else:
                    F_B(move[0], clockwise)

            except:

                F_B(move[0], clockwise)

        #printCube(white, yellow, red, orange, blue, green)

    return [white, yellow, red, orange, blue, green]
    
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

                s = genScramble()

                print(" ".join(s), end="\n\r")
                
                S = simulate(s)
                
                printCube(S[0], S[1], S[2], S[3], S[4], S[5])

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
                startTime = timeD.time()
                endTime = timer(startTime)

                num = endTime - startTime

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