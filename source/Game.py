# from source.Square import Square
from source.Board import Board


class Game:
    def __init__(self):
        # ask the dimensions of the board
        print("Veuillez entrer la largeur du plateau")
        dim_y = self.input_number()
        print("Veuillez entrer la hauteur du plateau")
        dim_x = self.input_number()
        # ask the number of mines
        print("Veuillez entrer le nombre de mines souhaité")
        nb_mines = self.input_number()
        while nb_mines > dim_x * dim_y:
            print("Le nombre de mines est supérieur au nombre de cases. Veuillez entrer une autre valeur.")
            nb_mines = self.input_number()
        # create the board
        self.game_board = Board(dim_x, dim_y, nb_mines)

        self.play()
        return

    # tested
    # ask a number and deal with error
    def input_number(self):
        x = "-1"
        x_int = -1
        x_not_ok = True
        while x_not_ok:
            x = input()
            try:
                x_int = int(x)
                x_not_ok = False
            except ValueError as ve:
                print("La valeur n'est valide. Veuillez la ressaisir : ")
        return x_int

    # manage the player and the moves
    def play(self):
        game_continues = True
        while game_continues:
            self.game_board.display()

            if self.ask_action() == "C":
                # ask the position of the square to dig
                res_digging = self.play_dig()
                game_continues = not res_digging
            else:
                self.play_flag()

        # end
        if self.game_board.get_win():
            print("Félicitation, vous avez gagné !")
            self.game_board.display()
        else:
            print("Désolée, vous avez perdu... ")
            self.game_board.display()
        return

    # return the string with the action to perform
    # TESTED
    def ask_action(self):
        print("Veuillez entrer l'action à jouer (D : drapeau ; C : creuser)")
        x = ""
        x_not_ok = True
        while x_not_ok:
            x = input()
            x = x.strip()
            if x != "C" and x != "D":
                print("L'action n'a pas été comprise. Veuillez la ressaisir : ")
            else:
                x_not_ok = False
        return x

    # return True if the digging signals the end of the game
    # TESTED
    def play_dig(self):
        print("Veuillez entrer le numéro de la ligne de la case à creuser :")
        pos_x = self.input_number()
        print("Veuillez entrer le numéro de la colonne de la case à creuser :")
        pos_y = self.input_number()

        res_digging = self.game_board.dig(pos_x, pos_y)
        return res_digging

    def play_flag(self):
        print("Veuillez entrer le numéro de la ligne de la case (poser/enlever un drapeau) :")
        pos_x = self.input_number()
        print("Veuillez entrer le numéro de la colonne de la case (poser/enlever un drapeau) :")
        pos_y = self.input_number()

        self.game_board.modify_state_flag(pos_x, pos_y)
        return


def main():
    g1 = Game()
    # g1.ask_action()
    return


if __name__ == '__main__':
    main()