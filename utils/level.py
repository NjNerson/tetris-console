import time

LEVELS = {
    'normal': 0.5,        
    'fast': 0.25,
    'fast_and_furious': 0.10 
}

def select_level(stdscr):
    stdscr.clear()
    stdscr.addstr("Select level:\n")
    stdscr.addstr("1. Normal\n")
    stdscr.addstr("2. Fast\n")
    stdscr.addstr("3. Fast and Furious\n")
    stdscr.refresh()
    
    
    level = None
    while level not in ['normal', 'fast', 'fast_and_furious']:
        ch = stdscr.getch()
        if ch == ord('1'):
            level = 'normal'
        elif ch == ord('2'):
            level = 'fast'
        elif ch == ord('3'):
            level = 'fast_and_furious'
    stdscr.addstr(f"Level chosen {level.upper()}")
    stdscr.refresh()
    time.sleep(1)
    return LEVELS[level]
