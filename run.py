import random


class Board:
    """
    Represents the game board.
    """

    def __init__(self, size, num_ships, ship_size):
        self.size = size
        self.num_ships = num_ships
        self.ship_size = ship_size
        self.board = []
        for i in range(size):
            self.board.append(["O"] * size)
        self.ships = []
        self.place_ships()

    def place_ships(self):
        """
        Randomly places ships on the board.
        """
        for i in range(self.num_ships):
            ship = []
            row, col = self.get_random_row_col()
            for j in range(self.ship_size):
                if random.randint(0, 1) == 0:
                    ship.append([row, col + j])
                else:
                    ship.append([row + j, col])
            self.ships.append(ship)

    def get_random_row_col(self):
        """
        Returns a random row and column coordinate within the board size.
        """
        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        return row, col

    def get_board(self):
        """
        Returns the current state of the game board.
        """
        return self.board

    def get_ships(self):
        """
        Returns the current state of the ships.
        """
        return self.ships

    def mark_hit(self, row, col):
        """
        Marks the given coordinate as a hit.
        """
        self.board[row][col] = "X"
        for ship in self.ships:
            if [row, col] in ship:
                ship.remove([row, col])
                if not ship:
                    self.ships.remove(ship)
        print("HIT!")

    def mark_miss(self, row, col):
        """
        Marks the given coordinate as a miss.
        """
        self.board[row][col] = "M"
        print("MISS!")

    def is_game_over(self):
        """
        Returns True if all ships have been sunk, False otherwise.
        """
        return not self.ships


board_size = 5
num_ships = 4
ship_size = 3

# Set up game board
board = Board(board_size, num_ships, ship_size)

# Start game loop
print("Welcome to ULTIMATE BATTLESHIPS!!")
print(f"Board Size: {board_size}. Number of ships: {num_ships}")
print("Top left corner is row: 0, col: 0")
print()
player_name = input("Please enter your name: ")
print()

num_turns = 0
while True:
    # Print board and ask for user input
    print(f"{player_name}, it's your turn!")
    guess_row = int(input("Guess row (0-4): "))
    guess_col = int(input("Guess col (0-4): "))
    print()

    # Check if guess is a hit or a miss
    if [guess_row, guess_col] in board.get_ships():
        board.mark_hit(guess_row, guess_col)
    else:
        board.mark_miss(guess_row, guess_col)

    # Check if game is over
    if board.is_game_over():
        print(f"Congratulations {player_name}, you sank all the ships!")
        print(f"You took {num_turns} turns.")
        break

    # Increment turn counter
    num_turns
