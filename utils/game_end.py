import curses
from utils.score import Score

def display_game_end(stdscr, score,new_best,level):
    # Clear the screnn and display the final score
    stdscr.clear()
    stdscr.addstr("Game Over!\n")
    if new_best:
        stdscr.addstr(f"NEW BEST SCORE FOR LEVEL {level.upper()}\n")
        stdscr.addstr(f"Your new best score is: {score}\n")
    else :
        stdscr.addstr(f"Your final score is: {score}\n")
    stdscr.addstr("Do you want to play again? (y/n)\n")
    stdscr.refresh()

    # Get user input for replay or leave
    while True:
        key = stdscr.getch()
        if key == ord('y') or key == ord('Y'):
            return True  
        elif key == ord('n') or key == ord('N'):
            return False  

def end_game(stdscr, score,level):
    score_man=Score()
    new_best=score_man.update_score(level,score)
    replay = display_game_end(stdscr, score,new_best,level)
    return replay


