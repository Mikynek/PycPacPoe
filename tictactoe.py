class Board:
    board = [" " for x in range(10)]
    turn = True # True -> Circle, False -> Cross

    def __init__(self) -> None:
        self.print_board()
        print("Player 1 Turn")

    def print_board(self):
        for rows in range(3):
            print("   |   |")
            print(" "+ self.board[1+rows*3] +" | "+ self.board[2+rows*3] +" | "+ self.board[3+rows*3])
            print("   |   |")
            if(rows != 2):
                print(" _________\n")
        print("\n")

    def choose_field(self):
        field = input("Choose a field from 1-9: ")
        field = int(field)
        while self.board[field] is not " ":
            field = input("Already selected! Select another field from 1-9: ")
            field = int(field)

        # players taking turns
        if(self.turn):
            self.add_circle(field)
            self.turn = False
        else:
            self.add_cross(field)
            self.turn = True
    
    def add_circle(self, index):
        self.board[index] = "O"
        self.print_board()
        print("Player 2 Turn")

    def add_cross(self, index):
        self.board[index] = "X"
        self.print_board()
        print("Player 1 Turn")


    # determines whether the game is over
    def game_end(self):
        # player won
        # draw -> all fields are occupied
        return False


if __name__ == "__main__":
    newBoard = Board()

    while(not newBoard.game_end()):
        newBoard.choose_field()