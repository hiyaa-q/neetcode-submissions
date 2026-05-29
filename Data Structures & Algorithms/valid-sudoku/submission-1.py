class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        rowSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        columnSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for row in range(9):
            for col in range(9):
                currentStr = board[row][col]
                if (currentStr) == ".": continue

                if currentStr in rowSeenNumbers[row]:
                    return False
                else:
                    rowSeenNumbers[row].add(currentStr)

                if currentStr in columnSeenNumbers[col]:
                    return False
                else:
                    columnSeenNumbers[col].add(currentStr)

                if currentStr in subBoxSeenNumbers[(row//3)*3 + (col//3)]:
                    return False
                else:
                    subBoxSeenNumbers[(row//3)*3 + (col//3)].add(currentStr)
        
        return True
        