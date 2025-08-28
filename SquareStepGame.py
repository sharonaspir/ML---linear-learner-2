import collections

class GameBoard:
    def __init__(self, rows=4, cols=5):
        self.rows = rows
        self.cols = cols
        self.board: list[list[str]] = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start_pos = (0, 0)
        self.end_pos = (0, 4)
        
        self.noGOSimbol = 'x'
        self.emptySqureSimbol = ' '

        self.board[1][0] = self.noGOSimbol
        self.board[2][0] = self.noGOSimbol
        self.board[3][0] = self.noGOSimbol
        self.board[3][4] = self.noGOSimbol
        self.board[2][4] = self.noGOSimbol 

        self.board[self.end_pos[0]][self.end_pos[1]] = 'end'
        self.firstStep()

    def firstStep(self):
        self.board[self.start_pos[0]][self.start_pos[1]] = '0'

    def display(self):
        for row in self.board:
            print(' | '.join([' ' if cell is None else str(cell) for cell in row]))
            print('-' * (self.cols * 4 - 1))

    def canMoveToEnd(self):  
        # check no cell is empty
        for row in self.board:
            for cell in row:
                if cell == self.emptySqureSimbol: 
                    return False
                
        # check if end is next to max step
        max_step, (row, col) = self.getMaxStep()
        end_row, end_col = self.end_pos
        
        if (abs(row - end_row) == 1 ) and (abs(col - end_col) == 0):
            return True
        
        if (abs(row - end_row) == 0 ) and (abs(col - end_col) == 1):
            return True
       
        return False
    
    def getCopiedBoard(self):
        new_board = GameBoard(self.rows, self.cols)
        new_board.board = [row[:] for row in self.board]
        return new_board
    
    def step(self, position, direction):
        r, c = position
        if direction == 'up':
            r = r - 1
        elif direction == 'down' :
            r = r + 1
        elif direction == 'left' :
            c = c - 1
        elif direction == 'right':
            c = c + 1
            
        if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == self.emptySqureSimbol:
            self.board[r][c] = str(int(self.board[position[0]][position[1]]) + 1)
            return True
        return False
    
    def getMaxStep(self): 
        max_step = 0 
        col = 0 
        row = 0 
        for r in range(self.rows): 
            for c in range(self.cols): 
                val = self.board[r][c] 
                try: 
                    val = int(val) 
                except (ValueError, TypeError): 
                    continue 
                if isinstance(val, int) and val > max_step: 
                    max_step = val 
                    row, col = r, c
        return max_step, (row, col)
        
    def solve(self): 
        max_step, (row, col) = self.getMaxStep()
 
        # upTry
        upTry = self.getCopiedBoard()
        if upTry.step((row, col), 'up'):
            if upTry.canMoveToEnd():
                self.board = upTry.board
                return True
            if upTry.solve():
                self.board = upTry.board
                return True

        # rightTry 
        rightTry = self.getCopiedBoard()
        if rightTry.step((row, col), 'right'):
            if rightTry.canMoveToEnd():
                self.board = rightTry.board
                return True
            if rightTry.solve():
                self.board = rightTry.board
                return True
            
        # downTry
        downTry = self.getCopiedBoard() 
        if downTry.step((row, col), 'down'):
            if downTry.canMoveToEnd():
                self.board = downTry.board
                return True
            if downTry.solve():
                self.board = downTry.board
                return True

        # leftTry
        leftTry = self.getCopiedBoard()
        if leftTry.step((row, col), 'left'):
            if leftTry.canMoveToEnd():
                self.board = leftTry.board
                return True
            if leftTry.solve():
                self.board = leftTry.board
                return True

        return False

      
# Example usage:
if __name__ == "__main__":
    game_board = GameBoard() 

    solution = game_board.solve()
    if solution:
        game_board.display()
    else:
        print("No solution found.")


