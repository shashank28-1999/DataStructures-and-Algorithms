# place N queens in a NxN board such that no queen is attacking each other
n=int(input("enter number of queens: "))
board=[['.' for i in range(n)] for i in range(n)]

def solveNQ(board,col):
    if(col>=n):
        return True
    for i in range(0,n):
        if(safe(board,i,col)):
            board[i][col]='Q'
            if(solveNQ(board,col+1)):
                return True
            board[i][col]='.'
    return False

def safe(board,row,col):
    for i in range(0,col):
        if(board[row][i]=='Q'):
            return False

    i, j = row, col
    while(i>=0 and j>=0):
        if(board[i][j]=='Q'):
            return False
        i=i-1
        j=j-1
        
    i, j = row, col
    while(i<n and j>=0):
        if(board[i][j]=='Q'):
            return False
        i=i+1
        j=j-1
    return True

if(solveNQ(board,0) is False):
    print("no solution exist")
else:
    for i in range(0,n):
        for j in range(0,n):
            print(board[i][j],end=" ")
        print()