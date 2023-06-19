class Board:
    board = [" " for x in range(10)]
    circleRound = True
    # add list/set for num track

    def __init__(self) -> None:
        pass

    def printBoard(self):
        for rows in range(3):
            print("   |   |")
            print(" "+ self.board[1+rows*3] +" | "+ self.board[2+rows*3] +" | "+ self.board[3+rows*3])
            print("   |   |")
            if(rows != 2):
                print(" _________\n")
        print("\n")

    def chooseField(self):
        choosedNum = input("Choose a field from 1-9:")
        choosedNum = int(choosedNum)
        #choosedNum = input("Already choosen! Choose a different field from 1-9:")
        # if a index value is already given ask for field again
        if(self.circleRound):
            self.addCircle(choosedNum)
        else:
            self.addCross(choosedNum)
    
    def addCircle(self, index):
        self.board[index] = "O"
        self.printBoard()

    def addCross(self, index):
        self.board[index] = "X"
        self.printBoard()



newBoard = Board()
newBoard.printBoard()
newBoard.chooseField()
newBoard.addCircle(2)
newBoard.addCross(3)