class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        rowSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        columnSeenNumbers = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for row in range(9):
            for col in range(9):
                currentStr = board[row][col]
                if (currentStr) == ".": continue

                if currentStr in rowSeenNumbers[row] or currentStr in columnSeenNumbers[col] or currentStr in subBoxSeenNumbers[(row//3)*3 + (col//3)]:
                    return False

                rowSeenNumbers[row].add(currentStr)
                columnSeenNumbers[col].add(currentStr)
                subBoxSeenNumbers[(row//3)*3 + (col//3)].add(currentStr)
        
        return True
        