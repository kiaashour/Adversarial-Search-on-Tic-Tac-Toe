#Import necessary packages
import math
import time
import sys

#Implement the MinMax algorithm for tic-tac-toe on a (m,n,k)-board
class Game():
    def __init__(self, m, n, k, automatic=True, display=True):
        """ Initialize the a game of tic-tac-toe on an m x n board
            where k consecutive pieces are needed to win in a row
            or column or diagonal. This uses the Minimax algorithm
            to play the game and recommend the best moves.

            The implementation here is for a 2-player game, where
            player 1 is the maximizer and player -1  is the minimizer.
            We take player 1 to be the human player and player -1 to
            be the computer player. We will also refer to player -1 as
            player 2.

            To play the game against the computer, set automatic to False.
            When playing against the computer, the human player should enter the row and column number
            of the move in the format "i j" where i is the row number ranging from 0 to m-1, 
            and j is the column number ranging from 0 to n-1. The best move available for the human player 
            at each move is displayed.

            To play the game, run the following commands:
            game = Game(m, n, k, automatic=False, display=True)
            game.initialize_game()
            game.drawboard()
            game.play()        

        Args:
            m (int): number of rows
            n (int): number of columns
            k (int): number of pieces in a row to win
            automatic (bool): True if the Player 1 is the computer, False otherwise
            display (bool): True if the board is to be displayed after each move, False otherwise
        """
        #Initialize game board attributes
        self.m = m
        self.n = n
        self.k = k        

        #Set attributes regrading the game
        self.automatic = automatic
        self.display = display
        self.last_move = None
        self.current_player = -1  #1 for player MAX, -1 for player MIN (also referred to as player 2)
        self.all_possible_moves = {(i, j) for i in range(self.m) for j in range(self.n)}    

        #Set attributes for the game statistics
        self.times = []
        self.states_visited = 0

    def initialize_game(self):
        """ Initialize the game board by creating a m x n matrix
            and setting all the values to 0 and also creating a dictionary
            to store moves made by players.

            Note that the board attribute is mainly used for plotting.
        """
        self.board = [[0 for i in range(self.n)] for j in range(self.m)]
        self.moves = {-1: set(), 1: set()} 

    def possible_moves(self, state):
        """ Find all possible moves from a state

        Args:
            state (dict): A dictionary of the moves made by the players

        Returns:
            set: A set of all possible moves
        """
        possible_moves = self.all_possible_moves - state[1] - state[-1]
        return possible_moves

    def drawboard(self):
        """ Draw the board at the current state of the game."""
        #Print rows
        for i in range(self.m):
            print(' ---' * self.n)
            #Print columns
            for j in range(self.n):
                #Print the player's move
                if self.board[i][j] == 1:
                    print('| X ', end='')
                elif self.board[i][j] == -1:
                    print('| O ', end='')
                else:
                    print('|   ', end='')
            
            #Print separator
            print('|')
        #Print the last row
        print(' ---' * self.n)

    def max(self):
        """Compute the max value of the game."""
        #Check if the game is over
        terminal, winner = self.is_terminal(-1)
        best_move = None
        if terminal:
            return winner, best_move

        #Initialise the max value
        v = -1*math.inf

        #Look for all possible moves
        possible_moves = self.possible_moves(self.moves)
        for i, j in possible_moves:
            #Check if the move is valid
            if self.is_valid(i, j):                
                #Store the temporary last move
                temp_last_move = self.last_move

                #Make the move and compute the min value
                self.states_visited += 1
                self.last_move = (i, j)
                self.board[i][j] = 1
                self.moves[1].add((i, j))
                min_v, best_move_min = self.min()

                #If the min value is greater than the max value, update the max value
                if min_v > v:
                    best_move = (i, j)
                    v = max(v, min_v)

                #Undo the move
                self.board[i][j] = 0
                self.moves[1].remove((i, j))
                self.last_move = temp_last_move

        return v, best_move       

    def min(self):
        """Compute the min value of the game."""

        #Check if the game is over
        best_move = None
        terminal, winner = self.is_terminal(1)
        if terminal:
            return winner, best_move

        #Initialise the min value
        v = math.inf 

        #Look for all possible moves
        possible_moves = self.possible_moves(self.moves)
        for i, j in possible_moves:
            #Check if the move is valid
            if self.is_valid(i, j):
                #Store the temporary last move
                temp_last_move = self.last_move                

                #Make the move and compute the max value
                self.states_visited += 1
                self.last_move = (i, j)
                self.board[i][j] = -1
                self.moves[-1].add((i, j))
                max_v, best_move_max = self.max()

                #If the max value is less than the min value, update the min value
                if max_v < v:                        
                    best_move = (i, j)
                    v = min(v, max_v)

                #Undo the move
                self.board[i][j] = 0
                self.moves[-1].remove((i, j))
                self.last_move = temp_last_move

        return v, best_move

    def is_valid(self, i, j):
        """ Check if the move is valid

        Args:
            i (int): row
            j (int): column

        Returns:    
            bool: True if the move is valid, False otherwise
        """ 
        #Check if the move is valid
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        elif self.board[i][j] != 0:
            return False
        else:
            return True

    def move_horizontal(self, point, step):
        """ Move a point horizontally by step 

        Args:
            point (tuple): A tuple of (x, y)
            step (int): The number of steps to move

        Returns:
            A tuple of (x, y) after moving
        """
        return (point[0] + step, point[1])

    def move_vertical(self, point, step):
        """ Move a point vertically by step 

        Args:
            point(tuple): A tuple of (x, y)
            step (int): The number of steps to move

        Returns:
            A tuple of (x, y) after moving
        """
        return (point[0], point[1] + step)

    def move_diagonal_left(self, point, step):
        """ Move a point diagonally left by step 

        Args:
            point (tuple): A tuple of (x, y)
            step (int): The number of steps to move

        Returns:
            A tuple of (x, y) after moving
        """
        return (point[0] - step, point[1] + step)

    def move_diagonal_right(self, point, step):
        """ Move a point diagonally right by step 

        Args:
            point (tuple): A tuple of (x, y)
            step (int): The number of steps to move

        Returns:
            A tuple of (x, y) after moving
        """
        return (point[0] + step, point[1] + step)


    def is_terminal(self, last_player):
        """ Checks if the game is over.

            Note that the winner matches the utility.

        Args:
            last_player (int): The last player to move.
            last_move (tuple): The last move made.

        Returns:
            (terminal, winner): A tuple of whether the game is over and the winner.
                                If the game is not over, winner is None. Here, the winner
                                matches the utility.

        """
        terminal = False
        winner = None
        
        #If no previous action, then the game is not over
        if self.moves[last_player] == set():
            return terminal, winner

        #Get last moves
        prev_action = self.last_move
        prev_actions = self.moves[last_player]        

        #For each direction, check if there are k consecutive pieces
        possible_directions = [self.move_horizontal, self.move_vertical, self.move_diagonal_left, self.move_diagonal_right]
        for direction in possible_directions:
            count = 0
            #Check the previous action moving the right direction
            for step in range(1, self.k):
                next_action = direction(prev_action, step)
                if next_action in prev_actions:
                    count += 1
                else:
                    break
                
            #Check the previous action moving the left direction
            for step in range(1, self.k):
                next_action = direction(prev_action, -step)
                if next_action in prev_actions:
                    count += 1
                else:
                    break
            #If there are k consecutive actions in the same direction, then the game is over
            if count >= self.k - 1:
                terminal = True
                winner = last_player
                return terminal, winner

        #Check if the game is a draw
        if len(self.moves[-1]) + len(self.moves[1]) == self.m * self.n:
            terminal = True
            winner = 0  #0 to correspond to the utility function            
            return terminal, winner

        return terminal, winner


    def receive_move(self, player):
        """ Receive a move from the player

        Args:
            player (int): The player to move

        Returns:
            (i, j): The move
        """        
        #If the player is player 1, then take the input and recommend the best move
        time1 = time.time()
        if player == 1:
            #If automatic, then player 1 plays automatically
            if self.automatic:
                v, best_move = self.max()
                i, j = best_move
                self.last_move = (i, j)

            #If not automatic, then player 1 takes the input
            else:
                #Find the best move
                v, best_move = self.max()
                
                #Recommend move and take input                
                print(f"Player 1's should do: {best_move}")         
                i, j = list(map(int, input('Player 1: ').split()))
                while not self.is_valid(i, j):
                    i, j = map(int, input('Player 1: ').split())
                self.last_move = (i, j)
        
        #If the player is player -1, take the best move
        else:
            v, best_move = self.min()
            i, j = best_move
            self.last_move = (i, j)
            print(f"Move taken by Player 2: {best_move}")            

        #Update the board
        time2 = time.time()
        self.times.append(time2 - time1)   
        self.board[i][j] = player
        self.moves[player].add((i,j))

        #Draw the board
        if self.display:
            self.drawboard()


    def play(self):
        """ Play the game, starting with player -1."""
        last_player = 1 

        #Until the game is not over, keep playing
        while True:
            
            #Player 1 (MAX) plays
            move = self.receive_move(1)
            terminal, winner = self.is_terminal(1)

            #Check if the game is over
            if terminal and winner!=0 :
                print("The winner is player {}".format(winner))
                if self.display:
                    self.drawboard()
                break

            elif terminal and winner==0:
                print("The game is a draw")
                break
            
            #Player 2 (MIN) plays
            move = self.receive_move(-1)
            terminal, winner = self.is_terminal(-1)

            #Check if the game is over
            if terminal and winner!=0:
                print("The winner is player {}".format(winner))
                if self.display:
                    self.drawboard()
                break

            elif terminal and winner==0:
                print("The game is a draw")
                break


#Example demonstrating the game being played with player 1 as manual and player 2 as automatic
if __name__ == '__main__':
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    tictactoe = Game(m, n, k, automatic=False, display=True)
    tictactoe.initialize_game()
    tictactoe.drawboard()
    tictactoe.play()

    
