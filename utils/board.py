class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score=0
        self.grid = [[0] * width for _ in range(height)]
    
    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def is_position_free(self, x, y):
        return self.grid[y][x] == 0

    def add_piece_to_board(self, piece, x, y):
        for row_idx, row in enumerate(piece):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    self.grid[y + row_idx][x + col_idx] = cell

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(cell != 0 for cell in row)]
        self.update_score(len(lines_to_clear))
        for i in reversed(lines_to_clear):
            del self.grid[i]
            self.grid.insert(0, [0] * self.width)

    def update_score(self, lines_cleared):
        bonus= round(lines_cleared/2) if lines_cleared>1 else 0
        self.score += (lines_cleared * 10 )  + bonus

    def get_score(self):
        return self.score

    def is_full(self):
        return any(cell != 0 for cell in self.grid[0])

    def render(self, stdscr):
        stdscr.clear()
        for row in self.grid:
            stdscr.addstr("|")
            for cell in row:
                stdscr.addstr(" . " if cell == 0 else " X ")
            stdscr.addstr("|\n")
        stdscr.addstr("+" + "---" * self.width + "+\n")
        stdscr.refresh()
