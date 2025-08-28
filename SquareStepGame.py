import collections

NO_GO_SIMBOL = 'x'
EMPTY_SQUARE_SYMBOL = ''
END_SQUARE_SYMBOL = 'end'

class GameBoard:
    def __init__(self, rows=4, cols=5):
        self.start_pos = (0, 0)
        self.end_pos = (0, 4)

        self.rows = rows
        self.cols = cols
        self.board: list[list[str | int]] = [[EMPTY_SQUARE_SYMBOL for _ in range(cols)] for _ in range(rows)]

        # Set no-go zones
        self.board[1][0] = NO_GO_SIMBOL
        self.board[2][0] = NO_GO_SIMBOL
        self.board[3][0] = NO_GO_SIMBOL
        self.board[1][4] = NO_GO_SIMBOL 
        self.board[2][4] = NO_GO_SIMBOL 
        self.board[3][4] = NO_GO_SIMBOL

        self.board[self.end_pos[0]][self.end_pos[1]] = END_SQUARE_SYMBOL
        self.board[self.start_pos[0]][self.start_pos[1]] = '0'

    def display(self):
        for row in self.board:
            print(' | '.join([str(cell) for cell in row]))
            print('-' * (self.cols * 3))

    def canMoveToEnd(self):  
        # check no cell is empty
        for row in self.board:
            for cell in row:
                if cell == EMPTY_SQUARE_SYMBOL: 
                    return False
                
        # check if end is next to max step
        (row, col) = self.getMaxStep()
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
    
    def step(self, direction):
        position = self.getMaxStep()
        r, c = position
        
        if direction == 'up':
            r = r - 1
        elif direction == 'down' :
            r = r + 1
        elif direction == 'left' :
            c = c - 1
        elif direction == 'right':
            c = c + 1
            
        if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == EMPTY_SQUARE_SYMBOL:
            next_step = int(self.board[position[0]][position[1]]) + 1
            self.board[r][c] = next_step
            return True
        
        return False
    
    def getMaxStep(self): 
        max_step, row, col = 0, 0, 0
        for r in range(self.rows): 
            for c in range(self.cols): 
                val = self.board[r][c]  
                if isinstance(val, int) and val > max_step: 
                    max_step = val 
                    row, col = r, c
        return (row, col)
        
    def solveRecursive(self): 
        for direction in ['up', 'right', 'down', 'left']:
            next_try = self.getCopiedBoard()
            if next_try.step(direction):
                if next_try.canMoveToEnd():
                    self.board = next_try.board
                    return True
                if next_try.solveRecursive():
                    self.board = next_try.board
                    return True

        return False
      
# Example usage:
if __name__ == "__main__":
    game_board = GameBoard() 
    game_board.display()

    solution = game_board.solveRecursive()
    if solution:
        game_board.display()
    else:
        print("No solution found.")


