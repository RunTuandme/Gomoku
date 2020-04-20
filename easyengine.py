import random

class SampleEngine:
    def __init__(self, fen = None, is_black_turn = [True]):
        self.fen = fen 
        self.is_black_turn = is_black_turn

    def run(self):
        container = []
        pos = 0
        for i in self.fen:
            if i == '0':
                container.append(pos)
            pos += 1

        best_move = random.choice(container)

        return best_move