from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for i in range(9)]

        for i, row in enumerate(board):
            rowCounter = defaultdict(int)
            for j, v in enumerate(row):
                cols[j].append(v)
                if v != ".":
                    rowCounter[v] += 1
                    if rowCounter[v] >= 2:
                        return False

        for i, col in enumerate(cols):
            rowCounter = defaultdict(int)
            for j, v in enumerate(col):
                if v != ".":
                    rowCounter[v] += 1
                    if rowCounter[v] >= 2:
                        return False

        for i in range(0, 9, 3):         
            for k in range(0, 9, 3):    
                rowCounter = defaultdict(int)
                for j in range(0, 3):
                    rowInd = i + j
                    for c in range(0, 3):
                        colInd = k + c
                        v = board[rowInd][colInd]
                        if v != ".":
                            rowCounter[v] += 1
                            if rowCounter[v] >= 2:
                                return False

        return True