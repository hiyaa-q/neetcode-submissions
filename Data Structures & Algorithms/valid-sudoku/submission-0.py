class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxSeenNumbers = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        rowSeenNumbers = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        columnSeenNumbers = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for row in range(9):
            for col in range(9):
                currentStr = board[row][col]
                if (currentStr) == ".": continue

                if currentStr in rowSeenNumbers[row]:
                    return False
                else:
                    rowSeenNumbers[row][currentStr] = 1

                if currentStr in columnSeenNumbers[col]:
                    return False
                else:
                    columnSeenNumbers[col][currentStr] = 1

                if currentStr in subBoxSeenNumbers[(row//3)*3 + (col//3)]:
                    return False
                else:
                    subBoxSeenNumbers[(row//3)*3 + (col//3)][currentStr] = 1
        
        return True
        