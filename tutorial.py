import curses
from curses import  wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Sleep Typing Test!\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

    stdscr.clear()
    target_text="This is sample string !"
    curr_text=[]

    start_time=time.time()
    correct_char=0

    stdscr.nodelay(True)
    while True:
        stdscr.clear()

        time_elapsed=max(time.time()-start_time,1)
        wpm=round((correct_char/(time_elapsed/60))/5)
        correct_char=display_text(stdscr,target_text,curr_text,wpm)
        stdscr.refresh()


        try:
            key=stdscr.getkey()
        except:
            continue
        if(curr_text==[]):
            start_time=time.time()

            
        if(ord(key)==27):
            exit() 
        if(key in ("KEY_BACKSPACE",'\b',"\x7f")):
            if(len(curr_text)>0):
                curr_text.pop()
            else:
                continue
        elif(len(curr_text)<len(target_text)):
            curr_text.append(key)


def display_text(stdscr,target_text,curr_text,wpm):
    correct_char=0
    stdscr.addstr(target_text)
    stdscr.addstr(1,0,f"WPM : {wpm}")
    stdscr.addstr(0,0,"")
    for i,text in enumerate(curr_text):
        color_green=curses.color_pair(3)
        color_red=curses.color_pair(2)
        if(text==target_text[i]):
            stdscr.addstr(0,i,text,color_green)
            correct_char+=1
        else:
            stdscr.addstr(0,i,"f",color_red)
    return correct_char


def main(stdscr):

    # Initialising color schemes for the terminal .
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    start_screen(stdscr)
    


wrapper(main)
