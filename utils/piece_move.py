import time
import curses
from utils.pieces import RESET_COLOR
from utils.game_suspend import PauseHandler
LEVELS = {
    'normal': 0.5,        
    'fast': 0.25,
    'fast_and_furious': 0.10 
}

class PieceMover:
    def __init__(self, board, piece, piece_queue, stdscr, level,best_score):
        self.board = board
        self.piece_queue = piece_queue 
        self.piece = piece
        self.piece_x = (self.board.width - 4) // 2  
        self.piece_y = 0 
        self.stdscr = stdscr
        self.last_fall_time = time.time()
        self.fall_speed = LEVELS[level]
        self.pause_handler = PauseHandler(stdscr)
        self.best_score = best_score
        self.level=level

    def can_move(self, dx, dy):
        for row_idx, row in enumerate(self.piece):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    new_x = self.piece_x + col_idx + dx
                    new_y = self.piece_y + row_idx + dy
                    if not self.board.is_within_bounds(new_x, new_y) or not self.board.is_position_free(new_x, new_y):
                        return False
        return True

    def move_left(self):
        if self.can_move(-1, 0):
            self.piece_x -= 1

    def move_right(self):
        if self.can_move(1, 0):
            self.piece_x += 1

    def move_down(self):
        if self.can_move(0, 1):
            self.piece_y += 1
            return True
        return False

    def rotate_piece(self):
        rotated_piece = list(zip(*self.piece[::-1])) 
        if self.can_rotate(rotated_piece):
            self.piece = rotated_piece

    def can_rotate(self, rotated_piece):
        for row_idx, row in enumerate(rotated_piece):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    new_x = self.piece_x + col_idx
                    new_y = self.piece_y + row_idx
                    if not self.board.is_within_bounds(new_x, new_y) or not self.board.is_position_free(new_x, new_y):
                        return False
        return True

    def place_piece_on_board(self):
        self.board.add_piece_to_board(self.piece, self.piece_x, self.piece_y)

    def render(self):
        temp_grid = [row[:] for row in self.board.grid]
        for row_idx, row in enumerate(self.piece):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    temp_grid[self.piece_y + row_idx][self.piece_x + col_idx] = cell

        self.stdscr.clear()
        
        max_y, max_x = self.stdscr.getmaxyx()

        if self.board.height + 2 < max_y and self.board.width * 3 + 20 < max_x: 
            for row_idx, row in enumerate(temp_grid):
                self.stdscr.addstr("|")
                for cell in row:
                    self.stdscr.addstr(" . " if cell == 0 else f" X ")
                self.stdscr.addstr("|\n")
            
            self.stdscr.addstr("+" + "---" * self.board.width + "+\n")

            next_piece = self.piece_queue.preview_piece()
            if next_piece:
                preview_x = self.board.width * 3 + 10  
                
                self.stdscr.addstr(1, preview_x, "Next Piece:",curses.A_UNDERLINE)
                for row_idx, row in enumerate(next_piece):
                    self.stdscr.addstr(3 + row_idx, preview_x, " ".join([" . " if cell == 0 else " X " for cell in row]))

                self.stdscr.addstr(10,preview_x,f"LEVEL {self.level.upper()}\n",curses.A_UNDERLINE)
                self.stdscr.addstr(11,preview_x,f"Score: {self.board.get_score()}\n")
                self.stdscr.addstr(12,preview_x,f"Best Score: {self.best_score}\n")
        else:
            self.stdscr.addstr("Screen too small to display the game!\n")

        if self.pause_handler.paused:
            self.stdscr.addstr(max_y - 2, 0, "Game Paused. Press SPACE to resume or 'q' to quit.\n")

        self.stdscr.refresh()


    def run(self):
        while True:
            if self.pause_handler.paused:
                self.pause_handler.handle_pause()
                continue

            self.render()
            now = time.time()

            if now - self.last_fall_time > self.fall_speed:
                if not self.move_down():
                    self.place_piece_on_board()
                    self.board.clear_lines()
                    if not self.can_move(0, 0):
                        break
                    self.piece = self.piece_queue.get_piece() 
                    self.piece_x = (self.board.width - 4) // 2
                    self.piece_y = 0
                self.last_fall_time = now

            if not self.handle_input():
                break

    def handle_input(self):
        key = self.stdscr.getch()
        if key == curses.KEY_LEFT:
            self.move_left()
        elif key == curses.KEY_RIGHT:
            self.move_right()
        elif key == curses.KEY_DOWN:
            if not self.move_down():
                self.place_piece_on_board()
                self.board.clear_lines()
                if not self.can_move(0, 0):
                    return False
                self.piece = self.piece_queue.get_piece()
                self.piece_x = (self.board.width - 4) // 2
                self.piece_y = 0
        elif key == curses.KEY_UP:
            self.rotate_piece()
        elif key == ord(' '):
            self.pause_handler.paused = not self.pause_handler.paused
        elif key == ord('q') and self.pause_handler.paused:
            self.stdscr.addstr("Quitting game...")
            self.stdscr.refresh()
            time.sleep(1)
            exit()
        return True
