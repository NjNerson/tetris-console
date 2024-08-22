import curses
from utils.board import Board
from utils.piece_move import PieceMover
from utils.pieces import get_random_piece,get_random_color
from utils.game_end import end_game
import time
from utils.level import select_level

def main(stdscr):

    curses.curs_set(0)  
    stdscr.nodelay(1)   
    stdscr.timeout(100) 
    while True :
        level=select_level(stdscr)
        board = Board(width=10, height=20)

        while not board.is_full():
            piece = get_random_piece()

            mover = PieceMover(board, piece, stdscr,level)
            mover.run()
        
        # Game over
        replay=end_game(stdscr,board.get_score())
        if not replay :
            stdscr.clear()
            stdscr.addstr("BYE BYE!\n")
            stdscr.refresh()
            time.sleep(0.5)         
            break

if __name__ == "__main__":
    curses.wrapper(main)
