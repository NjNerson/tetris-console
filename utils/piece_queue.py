from collections import deque
from utils.pieces import get_random_piece

class PieceQueue:
    def __init__(self):
        self.queue = deque()
        self.fill_queue()
    
    def fill_queue(self):
        while len(self.queue) < 5:  
            self.queue.append(get_random_piece())
    
    def get_piece(self):
        if not self.queue:
            self.fill_queue()
        return self.queue.popleft()
    
    def preview_piece(self):
        if self.queue:
            return self.queue[0]  
        return None
