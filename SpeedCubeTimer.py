import time
import curses
import os
import random
import statistics
import src.timer 
import src.stats
import src.settings
import src.simulate

# I don't clearly understand this

stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(1)

def stop():
    # Clear and ends process
    curses.endwin()
    raise SystemExit

def clear():
    # Clear old outputs
    curses.endwin()
    curses.initscr()

def wait(x):
    print("", end = "\n\r")
    
    if isinstance(x, list):

        while True:
            key_pressed = stdscr.getch()

            for key in x:

                try:

                    if key_pressed == 27:
                        return len(x) - 1
                    elif key_pressed == ord(key):
                        return x.index(key)
        
                except:
                    pass

    else:
        print('\033[30;40m' + 'Press ' + x + ' to Continue...', end = "\n\r")

        while True:
            key = stdscr.getch()

            if key == ord(x):
                break

def main():
    # Use "\n\r" to keep spaces before print() 

    key = stdscr.getch() # Keep Print in Screen
    print('Spacebar: Send Scramble', end="\n\r")
    print('T: Show Stats', end="\n\r")
    #print("CURRENTLY WORKING ON " + 'S: Settings', end="\n\r")
    print('esc: Exit', end="\n\r")    
    print('')

    # Listening

    while True:
        key = stdscr.getch() # This is the key pressed

        try: 

            if key == ord(' '):

                clear()
                scramble = src.timer.genScramble()
                simulated_cube = src.simulate.simulate(scramble)

                print(' '.join(scramble), end = '\n\r')

                # Print a visual cube

                src.simulate.printCube(
                    simulated_cube[0],
                    simulated_cube[1],
                    simulated_cube[2],
                    simulated_cube[3],
                    simulated_cube[4],
                    simulated_cube[5]
                )

                print('')
                print('Press Spacebar to Start Timer...')

                # Wait until Starts Timer

                while True:
                    key = stdscr.getch()

                    if key == ord(' '):

                        clear()
                        solve_time = src.timer.timer(stdscr, time.time())
                        clear()

                        print('Solve Time: ' + '\033[1m' + solve_time, end = '\n\r\033[0;40m\n\r')

                        src.stats.add_solve(str(solve_time))
                        src.stats.resume()

                        wait(' ')
                        clear()
                        main()

                    elif key == 27:
                        break

                clear()
                main()

            elif key == ord("t"):

                key = None

                clear()

                try:

                    src.stats.full(clear, wait, main, 1, False, stdscr)
                    
                    clear()
                    main()

                except:
                    pass

            elif key == 27: # escape
                stop()

        except Exception as e:

            print(e)

    key = None

if __name__ == "__main__":
    main()