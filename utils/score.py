import os

class Score:
    def __init__(self, filename="score.txt"):
        self.filename = filename
        self.scores = self.load_scores()
    
    def load_scores(self):
        scores = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    level, score = line.strip().split(':')
                    scores[level] = int(score)
        else:
            with open(self.filename, 'w') as file:
                file.write("normal:0\nfast:0\nfast_and_furious:0\n") 
            scores = {"normal": 0, "fast": 0, "fast_ad_furious": 0}
        return scores
    
    def update_score(self, level, score):
        level = str(level)
        if level in self.scores:
            if score > self.scores[level]:
                self.scores[level] = score
                self.save_scores()
    
    def save_scores(self):
        with open(self.filename, 'w') as file:
            for level, score in self.scores.items():
                file.write(f"{level}:{score}\n")
    
    def get_best_score(self, level):
        level = str(level)
        return self.scores.get(level, 0)

