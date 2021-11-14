import os
import time
import statistics

def read_solves():

    try:
        return open('./solves.txt', 'r')
    except:
        open('./solves.txt', 'w')
        read_solves()

def getStats(solves):


    stats = {
        "average": {
            "global": None
        }
    }
    stats["average"]["global"] = round(statistics.mean(solves), 2)    

    # Find Current stats

    a3_current = []
    a5_current = []
    a12_current = []
    a100_current = []

    def global_solves(x, t):

        if len(solves) >= x:
            for y in range(1, x + 1):
                t.append(solves[len(solves) - y])

            stats["a" +  str(x)] = {}   
            stats["a" +  str(x)]["current"] = round(statistics.mean(t), 2)

    global_solves(3, a3_current)
    global_solves(5, a5_current)
    global_solves(12, a12_current)
    global_solves(100, a100_current)

    # Find the Better stats

    a3_solves = []
    a5_solves = []
    a12_solves = []
    a100_solves = []

    def better_solves(x, t):

        if len(solves) >= x:
            for solve in range(1, len(solves) - 1):
                try:
                    av = []
                    for y in range(-1, x-1):

                        av.append(solves[solve + y])

                    t.append(round(statistics.mean(av), 2))
                except:
                    pass

            stats["a" +  str(x)]["global"] = min(t)


    better_solves(3, a3_solves)
    better_solves(5, a5_solves)
    better_solves(12, a12_solves)
    better_solves(100,  a100_solves)

    stats["pr"] = min(solves)
    stats["solves"] = len(solves)

    return stats 

def parse_solves():

    _solves = read_solves().read().split("\n") # Read solves
    solves = []

    # Convert STR solves to an ARRAY of FLOAT solves
    for solve in _solves:
        try:
            solves.append(float(solve))
        except:
            pass
    
    return solves

def delete(solve):

    with open("./solves.txt", "r") as f:
        lines = f.readlines()
    with open("./solves.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != solve:
                f.write(line)
        #f.truncate()

def resume():

    solves = parse_solves()
    stats = getStats(solves)

    if float(stats["pr"]) == solves[len(solves) - 1]:
        print("CONGRATS - NEW PERSONAL RECORD!", end= "\n\r")
    
    for x in ["a3", "a5", "a12", "a100"]:
        try:
            if float(stats[x]["current"]) == float(stats[x]["global"]):
                print("CONGRATS - NEW " + x.upper() + " AVERAGE PERSONAL RECORD", end="\n\r")
        except:
            pass

    print("")
    print("Last 5 solves:", end = "\n\r")

    solves.reverse()
    for solve in range(0, 5):

        #try:
            print("  " + str(solve + 1) + ") " + str(solves[solve]), end = "\n\r")
        #except:
        #    pass

    return


def delete_all(x):
    try: 
        os.remove('./solves.txt')
        
        if x == True:
            print("Solves Erased", end = "\n\r")
        else:
            print("Solves.txt not generated", end= "\n\r")

    except:
        if x == True:
            print("Solves Don't exists", end = "\n\r")
        else:
            pass

    time.sleep(0.8)


def full(clear, wait, main, y, limit, stdscr):
    
    try:
        solves = parse_solves()
    except:
        delete_all(False)
        clear()
        main()

    if len(solves) == 0:
        print("There's not solves to show")
        time.sleep(2)
        clear()
        main()
    else:
        stats = getStats(solves)

        print("")
        print("           CURRENT        GLOBAL", end="\n\r")
        print(" Average            "+ str(stats["average"]["global"]) , end="\n\r")

        if len(solves) >= 3:
            print("      a3    "+ str(stats["a3"]["current"]) + "           " +  str(stats["a3"]["global"]), end="\n\r")
        if len(solves) >= 5:
            print("      a5    "+ str(stats["a5"]["current"]) + "           " +  str(stats["a5"]["global"]), end="\n\r")
        if len(solves) >= 12:
            print("     a12    "+ str(stats["a12"]["current"]) + "           " +  str(stats["a12"]["global"]), end="\n\r")
        if len(solves) >= 100:
            print("    a100    "+ str(stats["a100"]["current"]) + "           " +  str(stats["a100"]["global"]), end="\n\r")
        print("")
        print("Total = " + str(len(solves)), end = "\n\r")
        print("")
        print("")
        print("Solves:", end = "\n\r")
        print("")

        while True:
            if limit == False:
                for x in range(((y - 1) * 10) + 1, (y * 10) + 1):
                    try:
                        print("   " + str(x) + ") " + str(solves[x - 1]), end="\n\r")
                    except:
                        limit = True

                    if (x + 1) == len(solves):
                        limit = True
            
                print("", end = "\n\r")

                if not limit == True:
                    print("W: Next page", end = "\n\r")
                if y > 1:
                    print("S: Previous Page", end = "\n\r")

                print("D: Delete Solve", end = "\n\r")
                print("C: Delete ALL Solves", end = "\n\r")
                print("esc: Back to Menu", end = "\n\r")

                break;

            elif limit == True:

                pass

        while True:

            case = wait(["s", "w", "d", "c", 27])

            if case == 0:
                
                if y == 1:
                    pass;
                else:
                    limit = False
                    y = y -1
                    break

            elif case == 1:

                if limit == True:
                    pass
                else:
                    y = y + 1
                    break
                
            elif case == 2:

                num = []

                print("Solve to Delete: ", end="\n\r")

                while True:
                    key = stdscr.getch()
                    if key == 10:
                        break
                    elif key == 27:
                        clear()
                        full(clear, wait, main, y, limit, stdscr)                        
                    elif not key == -1:
                        num.append(chr(key))
                    
                num = "".join(num)

                try:
                    num = int(num)

                    delete(str(solves[num - 1]))

                    print("DONE", end = "\n\r")

                except:

                    clear()

                    print("It's not a number or It's not in your solves list", end = "\n\r")
                    
                time.sleep(0.6)
                limit = False
                break

            elif case == 3:

                print("Are you Sure?", end = '\n\r')
                wait(" ")
                delete_all(True)
                break

            elif case == 4:
                clear()
                main()

        clear()
        full(clear, wait, main, y, limit, stdscr)


def add_solve(solve):
    if not solve == "None" and len(solve) > 1:

        try:
            open('./solves.txt', 'r')
            file = open('./solves.txt', 'a')
            file.write("\n" + solve)
        except:
            file = open('./solves.txt', 'w')
            file.write(solve)

        file.close()