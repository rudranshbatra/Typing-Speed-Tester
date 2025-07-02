import curses
import time
import random
from curses import wrapper

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Tester!\n",curses.color_pair(3))
    stdscr.addstr("Press any key to begin",curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

def display(stdscr,target,input,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM:{wpm}")
        
    for i,char in enumerate(input):
       correct=target[i]
       color=curses.color_pair(2)
       if char!=correct:
           color=curses.color_pair(1)
       stdscr.addstr(0,i,char,color)


def gen_paragraph(Text_pool, word_count):
    words = random.choices(Text_pool, k=word_count)
    paragraph = ' '.join(words)

    return paragraph.capitalize()
    

def test(stdscr):
    Text_pool=["apple", "journey", "freedom", "sky", "laptop", "keyboard", "dream", "river",
    "mountain", "silent", "cloud", "story", "orange", "mirror", "candle", "garden",
    "window", "whisper", "bottle", "paper", "notebook", "ocean", "forest", "breeze",
    "calm", "thunder", "blanket", "pillow", "dance", "flame", "light", "path",
    "wander", "believe", "smile", "courage", "shadow", "flower", "galaxy", "reason",
    "hope", "secret", "truth", "echo", "memory", "storm", "stone", "horizon", "glass",
    "magic", "travel", "energy", "space", "clock", "moment", "motion", "wonder", "color",
    "melody", "idea", "rise", "fall", "future", "past", "peace", "struggle", "sound",
    "rain", "snow", "fire", "laugh", "tear", "love", "voice", "book", "time", "beauty",
    "break", "fix", "cold", "warm", "spark", "goal", "silence", "create", "destroy",
    "open", "close", "climb", "learn", "wait", "rush", "connect", "breathe", "touch",
    "build", "search", "find", "protect", "forget", "remember", "drift"]
    target_text=gen_paragraph(Text_pool, word_count=15)
    input_text=[]
    wpm=0
    time_1=time.time()
    stdscr.nodelay(True)

    while True:
        time_passed = max(time.time()- time_1, 1)
        wpm = round((len(input_text)/(time_passed/60))/5)           #assuming an average word has 5 characters
        stdscr.clear()
        display(stdscr,target_text,input_text,wpm)
        stdscr.refresh()
        if len(input_text)> 0: 
         if "".join(input_text) == target_text:
            stdscr.nodelay(False)
            return True
         if len(input_text)==len(target_text):
             stdscr.nodelay(False)
         
        try:
          
            key=stdscr.getkey()
        
        except:
           
            continue

        if ord(key) == 27 :
            break
        if key in ("KEY_BACKSPACE",'\b',"\x7f","\x08"):
          if len(input_text)>0:
                input_text.pop()
                
        elif len(input_text)<len(target_text): 
            input_text.append(key)   
        
    

def main(stdscr):

    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start(stdscr)
    while True:
        result=test(stdscr)
        if result==True:
         stdscr.addstr(3,0,"Good Job!\nPress Esc to exit the program or Any other key to try again")
         key = stdscr.getkey()
         if ord(key)==27:
             break
        else:
           stdscr.addstr(3,0,"NOT perfect\nPress Esc to exit the program or Any other key to try again")
           key = stdscr.getkey()
           if ord(key)==27:
              break   

wrapper(main)    
