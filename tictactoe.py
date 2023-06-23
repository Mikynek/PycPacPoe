class Board:
    def __init__(self) -> None:
        self.board = [" " for _ in range(10)]
        self.turn = True    # True -> Circle, False -> Cross
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
        while self.board[field] != " ":
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
    def game_end(self) -> bool:
        winning_conditions = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]  # Diagonals
        ]
        for condition in winning_conditions:
            if all(self.board[i] == "O" for i in condition):
                print("Player 1 WON!")
                return True
            elif all(self.board[i] == "X" for i in condition):
                print("Player 2 WON!")
                return True

        if all(cell != " " for cell in self.board[1:]):
            print("DRAW")
            return True

        return False


if __name__ == "__main__":
    newBoard = Board()

    while(not newBoard.game_end()):
        newBoard.choose_field()