from source.Square import Square
import random


class Board:

    def __init__(self, dimensions_x, dimensions_y, number_mines):
        self.dim_x = dimensions_x
        self.dim_y = dimensions_y
        self.nb_mines = number_mines
        self.dug_squares = 0
        self.board = []
        self.build_board()
        self.win = False

    # TESTED
    def build_board(self):
        # create all squares
        for i in range(self.dim_x):
            self.board.append([])
            for j in range(self.dim_y):
                squ = Square()
                squ.set_position(i, j)
                self.board[i].append(squ)
        # create the mines
        position_mines = self.pos_mines()
        for pos_mine in position_mines:
            self.board[pos_mine[0]][pos_mine[1]].set_mine(True)
            # tell the neighbors there is a mine nearby
            neighbors = self.get_neighbors(pos_mine)
            for neigh in neighbors:
                self.board[neigh[0]][neigh[1]].increase_mines_neighbors()
        return

    def get_board(self):
        return self.board

    def get_win(self):
        return self.win

    # TESTED
    # return the position of all the mines
    def pos_mines(self):
        pos_mines = []
        while len(pos_mines) != self.nb_mines:
            # get two random numbers
            position = (random.randint(0, self.dim_x-1), random.randint(0, self.dim_y-1))
            if position not in pos_mines:
                pos_mines.append(position)
        return pos_mines

    # return the position of all the neighbors of the give mine
    # TESTED
    def get_neighbors(self, position_mine):
        x = position_mine[0]
        y = position_mine[1]
        list_neighbors = []
        for i in range(-1, 2):
            if 0 <= i + x < self.dim_x:
                for j in range(-1, 2):
                    if 0 <= j + y < self.dim_y:
                        list_neighbors.append((i + x, j + y))
        list_neighbors.remove((x, y))
        return list_neighbors

    def modify_state_flag(self, pos_x, pos_y):
        self.board[pos_x][pos_y].modify_flag()
        return

    # return True if the digging signals the end of the game
    # smart digging implemented
    def dig(self, pos_x, pos_y):
        # check whether the square had been already dug
        if self.board[pos_x][pos_y].get_unveiled():
            return False

        # check whether there is a flag
        if self.board[pos_x][pos_y].get_flag():
            return False

        # dig the square
        self.board[pos_x][pos_y].dig_square()
        # if it explodes, end of the game
        if self.board[pos_x][pos_y].get_mine():
            return True

        self.dug_squares += 1
        # smart digging
        if self.board[pos_x][pos_y].get_mines_neighbors() == 0:
            # dig all the not-already-dug neighbors
            neighbors = self.get_neighbors((pos_x, pos_y))
            for neigh_pos in neighbors:
                neigh_x, neigh_y = neigh_pos[0], neigh_pos[1]
                if not self.board[neigh_x][neigh_y].get_unveiled():
                    self.dig(neigh_x, neigh_y)

        # if it is the last square without mines, it is the end (win)
        if self.dug_squares == self.dim_x * self.dim_y - self.nb_mines:
            self.win = True
            return True
        return False

    # TESTED
    def display(self):
        # board = self.game_board.get_board()
        list_display = []
        title_top = ["\t" + str(i) for i in range(0, self.dim_y)]
        list_display.extend(title_top)
        list_display.append("\n")
        for x in range(len(self.board)):
            list_display.append(str(x) + "|\t")
            for y in range(len(self.board[0])):
                list_display.append(self.board[x][y].display())
                list_display.append("\t")
            list_display.append("|\n")
        to_display = "".join(list_display)
        print(to_display)
        return


