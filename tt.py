import random


class TranspositionTable:
    def __init__(self):
        self.t = {}

    def save(self, cell, loc):
        self.t[cell] = loc

    def search(self, cell):
        return self.t.get(cell)

    def returnTable(self):
        return self.t


class ZobristHash:

    def __init__(self, boardSize):
        self.zobristArray = []
        self.boardIndices = boardSize*boardSize

        for _ in range(self.boardIndices):
            self.zobristArray.append([random.getrandbits(64) for _ in range(3)])

    def hash(self, board):
        hashCode = self.zobristArray[0][board[0]]
        for i in range(1,self.boardIndices):
            hashCode = hashCode ^ self.zobristArray[i][board[i]]
        
        return hashCode



