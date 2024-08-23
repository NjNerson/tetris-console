import time
import curses
from utils.game_end import end_game
from utils.level import select_level
from utils.board import Board
from utils.piece_move import PieceMover
from utils.piece_queue import PieceQueue
from utils.score import Score

def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(1)   
    stdscr.timeout(100) 

    while True:
        level = select_level(stdscr)
        board = Board(width=10, height=20)
        piece_queue = PieceQueue() 
        score= Score()


        while not board.is_full():
            piece = piece_queue.get_piece()
            mover = PieceMover(board, piece, piece_queue, stdscr, level,score.get_best_score(level)) 
            mover.run()
        
        # Game over
        score.update_score(level,board.get_score())
        replay = end_game(stdscr, board.get_score())
        if not replay:
            stdscr.clear()
            stdscr.addstr("BYE BYE!\n")
            stdscr.refresh()
            time.sleep(0.5)         
            break


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Quitting....")
        time.sleep(0.5)
