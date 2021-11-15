import configparser
import os
import time

file_name = "config.ini"

def write_changes(Config):

    with open(file_name, "w") as f:
        Config.write(f)
        f.close()

def create_conf_file( return_file ):
    Config = configparser.ConfigParser()
    Config.add_section("scramble")

    Config.set("scramble", "scramble_length", "20")
    Config.set("scramble", "rate", "4")
    Config.set("scramble", "normal", "2")
    Config.set("scramble", "double", "1")
    Config.set("scramble", "prime", "1")
    
    Config.add_section("timer")
    Config.set("timer", "inspection_time", "0")
    Config.set("timer", "visual_scramble", "True")    
    Config.set("timer", "better_visual_scramble", "True")
    Config.set("timer", "show_faces_initials", "True")

    Config.add_section("better_visual_scramble")
    Config.set("better_visual_scramble", "white", "#ffffff")
    Config.set("better_visual_scramble", "yellow", "#fee638")
    Config.set("better_visual_scramble", "red", "#ff0000")
    Config.set("better_visual_scramble", "orange", "#ffa02d")
    Config.set("better_visual_scramble", "blue", "#2d2dff")
    Config.set("better_visual_scramble", "green", "#2dcc1d")

    if return_file == False:
        write_changes(Config)
    else:
        return Config

def get_conf():
    try:

        if not os.path.isfile(file_name):
            create_conf_file(False)

        Config = configparser.ConfigParser()
        Config.read(file_name)

        control_file = create_conf_file(True)

        if not Config.sections() == control_file.sections():
            create_conf_file(False)

        for section in Config.sections():

            if not Config.options(section) == control_file.options(section):
                create_conf_file(False)
                break

        return Config

    except:

        os.remove(file_name)

        return get_conf()

def write_conf(section, option, new_value):
    try:

        new_value = str(new_value)

        Config = get_conf()
        Config = get_conf()

        if Config == None: 
            return False
        else:

            Config[section][option] = new_value

            write_changes(Config)

            return True

    except:
        return False


def read_conf(section, option):
    try:

        Config = get_conf()
        Config = get_conf()

        if Config == None:
            return False
        else:
            return Config[section][option]

    except:
        return False

def menu(clear, wait, main, stdscr, focus):
    clear()

    print("SETTINGS ----", end= "\n\r\n")

    Config = get_conf()
    Config = get_conf()

    configs_array = []

    for section in Config.sections():
        
        x = 0
        apnd = []

        print("\x1b[1;31m" + section, end="\n\r")
        if Config.sections().index(section) == focus[0]:
            for option in Config.options(section):

                if Config.options(section).index(option) == focus[1]:

                    print("\x1b[1;31m" + "- " + "\033[0;40m" + option + " : " + "\x1b[1;33m" + Config[section][option], end = "\n\r\033[0;40m")
                else:
                    print("\033[0;40m" + option + " : " + "\x1b[1;33m" + Config[section][option], end = "\n\r\033[0;40m")
                apnd.append(str(x))
                x = x +1 

        else:
            for option in Config.options(section):
                print("\033[0;40m" + option + " : " + "\x1b[1;33m" + Config[section][option], end = "\n\r\033[0;40m")
                apnd.append(str(x))
                x = x +1         
            
        print("")
        configs_array.append(apnd)

    if focus[1] == 0:

        if focus[0] == 0:
            prev_focus = [focus[0], focus[1]]
        else:
            prev_focus = [focus[0] - 1, len(configs_array[focus[0] - 1]) - 1]

        new_focus = [ focus[0], focus[1] + 1 ]    

    else:
        prev_focus = [focus[0], focus[1] - 1]

        if not focus[1] == len(configs_array[focus[0]]) -1:
            new_focus = [ focus[0], focus[1] + 1 ]
        else:

            if not focus[0] == len(configs_array) -1:
                new_focus = [ focus[0] + 1 , 0]
            else:
                new_focus = focus

    print("space bar: Back tu menu", end = "\n\r")
    print("e: Edit (USE THE CORRECT INPUT OR IT WILL BREAK)", end = "\n\r")
    print("r: Restore default config", end = "\n\r")

    key = wait(["w", "s", "e", "r"," "])

    # DOWN
    #print("Prev  " + prev_focus)

    if key == 4: # 

        return

    if key == 3: # r

        clear()
        os.remove(file_name)
        main()

    if key == 2: # e

        time.sleep(0.7)

        new_value = []

        print("Enter to submit")
        while True:

            key = stdscr.getch()

            if key == 10:

                break

            elif not key == -1:
                
                new_value.append(chr(key))

            print("".join(new_value), end = "\r")
        
        edit_section = Config.sections()[focus[0]]
        edit_option = Config.options(edit_section)[focus[1]]
        new_value = "".join(new_value)

        write_conf(edit_section, edit_option, new_value)

        menu(clear, wait, stdscr, main, focus)

    elif key == 1: # s
        menu(clear, wait, stdscr, main, new_focus)
    elif key == 0: # w
        menu(clear, wait, stdscr, main, prev_focus)

