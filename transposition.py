import random

class TranspositionTable:
    def __init__(self):
        self.t = {}

    def save(self, cell, move):
        self.t[cell] = move

    def get(self, cell):
        return self.t.get(cell)

    def table(self):
        return self.t

class ZobristHash:
    def __init__(self, board_size):
        self.hashList = []
        
        for i in range(board_size * board_size):
            for j in range(3):
                self.hashList.append(random.getrandbits(64))
        
    def hash(self, board):
        hashCode = self.hashList[0][board[0]]

        for i in range(1, board_size * board_size):
            hashCode = hashCode ^ self.hashList[i][board[i]]

        return hashCode
