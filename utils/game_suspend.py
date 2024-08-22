import time
import curses

class PauseHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.paused = False

    def handle_pause(self):
        self.stdscr.clear()
        self.stdscr.addstr("Game Paused. Press SPACE to resume or 'q' to quit.")
        self.stdscr.refresh()
        
        while True:
            ch = self.stdscr.getch()
            if ch == ord(' '):
                self.paused = False
                self.stdscr.clear()
                self.stdscr.refresh()
                break
            elif ch == ord('q'):
                self.stdscr.clear()
                self.stdscr.addstr("Quitting game...")
                self.stdscr.refresh()
                time.sleep(1)
                exit()

    def check_pause(self):
        if self.stdscr.getch() == ord(' '):
            self.paused = True
