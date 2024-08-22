import curses

def display_game_end(stdscr, score):
    # Clear the screnn and display the final score
    stdscr.clear()
    stdscr.addstr("Game Over!\n")
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

def end_game(stdscr, score):
    replay = display_game_end(stdscr, score)
    return replay


