class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Initializing three hashsets
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        # Traverse each element col through row
        for r in range(9):
            for c in range(9):
                
                # Ignore the .
                if board[r][c] == ".":
                    continue
                
                # Check if the element is in all three hashsets, if found exit the code as there's a duplicate and not a valid sudoku
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add element to the hashset for future comparisons
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # returns positive if there are no duplicates
        return True
            