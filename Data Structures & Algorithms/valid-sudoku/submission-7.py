from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # have to check for duplicates in each row, col, and 3x3 box
        # I could do two separate passes, one just checking duplicates
        # in each box, the other going down the diagonal checking 
        # each row and col
        
        # lets start with going diagonal
        for i in range(len(board)):
            rowmap = defaultdict(int)
            colmap = defaultdict(int)
            row = board[i]
            col = [r[i] for r in board]
            for i in range(len(row)):
                if row[i]!=".":
                    rowmap[row[i]]+=1
                if col[i]!=".":
                    colmap[col[i]]+=1
            print(list(rowmap.values()))
            print(list(colmap.values()))
            for key,num in list(rowmap.items()):
                
                if num>1:
                    print(key,num)
                    return False
            for key,num in list(colmap.items()):
                
                if num>1:
                    print(key,num)
                    return False
        # now that we've confirmed the diagonals are good, lets check all the 3x3 boxes
        # we could try starting at (1,1) then moving in steps of 3 and checking surrounding vals
        for i in range(1,len(board),3):
            for j in range(1,len(board[i]),3):
                checkbox = defaultdict(int)
                if board[i][j] != ".":
                    checkbox[board[i][j]]+=1
                if board[i+1][j] != ".":
                    checkbox[board[i+1][j]]+=1
                if board[i-1][j] != ".":
                    checkbox[board[i-1][j]]+=1
                if board[i-1][j-1] != ".":
                    checkbox[board[i-1][j-1]]+=1
                if board[i+1][j+1] != ".":
                    checkbox[board[i+1][j+1]]+=1
                if board[i][j+1] != ".":
                    checkbox[board[i][j+1]]+=1
                if board[i][j-1] != ".":
                    checkbox[board[i][j-1]]+=1
                if board[i-1][j+1] != ".":
                    checkbox[board[i-1][j+1]]+=1
                if board[i+1][j-1] != ".":
                    checkbox[board[i+1][j-1]]+=1
                for key,num in list(checkbox.items()):
                    if num>1:
                        print("box failed")
                        print(key,num)
                        return False

        return True



            