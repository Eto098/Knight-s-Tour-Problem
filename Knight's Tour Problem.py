##########################################
## Project: Knight's Tour
##
## Authors: Etem Kosencig \ 170201004
##          Meliksah Cetinkaya \ 150201035
##
## Date: Jan 05, 2020
##########################################


# Possible movements in Knight's coordinates
# In y coordinate, moves are multiplied by -1 because of the structure
# of the 2D array
moves = [(1,-2), (2,-1), (2,1), (1,2),
         (-1,2), (-2,1), (-2,-1), (-1,-2)]

# Main function to calculate the tour recursively
# Backtracking here
def backtrack(board, positionX, positionY, step, n):
    
    board[positionY][positionX] = step
    
    if step == n*n-1:
        printTheBoard(board, n)
        return True

    for i in range(8): # There are only 8 moves a knight can make
        if isValid(positionX+moves[i][0], positionY+moves[i][1],
                   board, n):
            if backtrack(board, positionX+moves[i][0],
                    positionY+moves[i][1], step+1, n):
                return True
            else:
                board[positionY+moves[i][1]][positionX+moves[i][0]] = -1
                
    return False

# Main function to calculate the tour
# Warnsdorff's Algorithm here
def warnsdorffs(board, positionX, positionY, step, n):
       
    while not step == n*n-1 or not len(getPossibleMoves(positionX, positionY, board, n)) == 0:
        board[positionY][positionX] = step
        possibilities = getPossibleMoves(positionX, positionY, board, n)
        minimumDegree = possibilities[0]
        for possibility in possibilities:
            if len(getPossibleMoves(possibility[0], possibility[1], board, n)) <= len(getPossibleMoves(minimumDegree[0], minimumDegree[1], board, n)):
                minimumDegree = possibility
        positionX = minimumDegree[0]
        positionY = minimumDegree[1]
        step += 1

    board[positionY][positionX] = step
    printTheBoard(board, n)
    return True
        
        
# To get the available moves from a point
# Used in Warnsdorff's Algorithm above
def getPossibleMoves(posX, posY, board, n):
    possibleMoves = []
    for i in range(8): # There are only 8 moves a knight can make
        if isValid(posX+moves[i][0], posY+moves[i][1],
                   board, n):
            possibleMoves.append([posX+moves[i][0], posY+moves[i][1]])
    return possibleMoves
            
        
def isValid(posX, posY, board, n):
    if posX >= 0 and posX < n and posY >= 0 and posY < n and board[posY][posX] == -1:
        return True
    return False


def printTheBoard(board, n):
    for i in range(n):
        for j in range(n):
            print("{:02d}".format(board[i][j]), end=' ')
        print()

def main():
    while True:
        print("\nChoose an algorithm to solve Knight's Tour Problem",
              "\n1 - Bactracking\n2 - Warnsdorff's\n0 - Quit\n\nChoice: ", end='')
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1 or choice == 2:
            print("Enter the board size (usually 8): ", end='')
            boardSize = int(input())
            print("Enter the starting square x coordinate (0 is the leftmost): ", end='')
            posX = int(input())
            print("Enter the starting square y coordinate (0 is topmost): ", end='')
            posY = int(input())

            # Initializing Empty Chess Board 
            GameBoard = [[-1 for i in range(boardSize)] for j in range(boardSize)]
            print("\nEMPTY CHESS BOARD")
            print("-----------------------")
            printTheBoard(GameBoard, boardSize)
            print("\nFILLED CHESS BOARD")
            print("-----------------------")

            if choice == 1:
                backtrack(GameBoard, posX, posY, 0, boardSize)
            if choice == 2:
                warnsdorffs(GameBoard, posX, posY, 0, boardSize)
            print("")

        else:
            print("Please Enter 1, 2 or 3")
    
# Main program code to execute
if __name__ == "__main__":
    
    main()

        

