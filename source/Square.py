
class Square:

    def __init__(self):
        self.__x = 0  # est-ce que la position est utile pour les mines ? elle est deja dans le board
        self.__y = 0
        self.__mine = False
        self.__nb_mines_neighbors = 0
        self.__unveiled = False
        self.__flag = False

    # TESTED
    def set_position(self, x, y):
        self.__x = x
        self.__y = y
        return

    # TESTED
    def get_position(self):
        tuple_pos = (self.__x, self.__y)
        return tuple_pos

    # TESTED
    def get_unveiled(self):
        return self.__unveiled

    # TESTED
    def get_mine(self):
        return self.__mine

    # TESTED
    def set_mine(self, mine):
        self.__mine = mine
        return

    def get_mines_neighbors(self):
        return self.__nb_mines_neighbors

    # TESTED
    def increase_mines_neighbors(self):
        self.__nb_mines_neighbors += 1

    # TESTED
    def dig_square(self):
        if not self.__flag:
            self.__unveiled = True
        return True

    def get_flag(self):
        return self.__flag

    # TESTED
    # a square can't be flagged if it is unveiled
    def modify_flag(self):
        if not self.__unveiled:
            self.__flag = not self.__flag
        return

    # TESTED
    def display(self):
        if not self.__unveiled:
            return "."
        if not self.__mine:
            # TODO : next step, return the flag
            return str(self.__nb_mines_neighbors)
        return "*"
