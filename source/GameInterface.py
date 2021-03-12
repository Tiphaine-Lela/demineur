from source.Board import Board
import tkinter as tk


class GameInterface(tk.Frame):
    def __init__(self, master=None, dim_x=10, dim_y=10, nb_mines=20):
        self.game_board = Board(dim_x, dim_y, nb_mines)
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.nb_mines = nb_mines
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    # appearance of the game
    def create_widgets(self):
        # title display
        self.frm_top = tk.Frame(master=self)
        self.lbl_title = tk.Label(master=self.frm_top, text="Démineur")
        self.lbl_title.pack()
        self.frm_top.pack()

        # some infos display
        self.frm_middle = tk.Frame(master=self)
        self.lbl_middle = tk.Label(master=self.frm_middle, text="", width=25, height=1)
        # info : the number of mines to find
        self.lbl_nb_left_mines = tk.Label(master=self.frm_middle, text=str(self.nb_mines), width=25, height=1)
        # rajouter un bouton pour choisir la taille de la grille et le nombre de mines
        # rajouter un bouton pour réinitialiser le jeu
        self.lbl_middle.pack()
        self.lbl_nb_left_mines.pack()
        self.frm_middle.pack()

        # gameboard display
        self.frm_game = tk.Frame(master=self)
        for row in range(self.dim_x):
            for column in range(self.dim_y):
                # relief et borderwidth sont necessaires pour avoir les traits qui separent les Frames
                frm_grid = tk.Frame(master=self.frm_game, relief=tk.RAISED, borderwidth=1)
                btn_grid = tk.Button(master=frm_grid, text=".", width=2, height=1)
                btn_grid.bind("<Button-1>", self.handle_left_click)
                btn_grid.bind("<Button-3>", self.handle_right_click)
                btn_grid.pack()
                frm_grid.grid(row=row, column=column)

        self.frm_game.pack()
        return

    def handle_left_click(self, event):
        # dig the square
        grid_info = event.widget.master.grid_info()
        x = grid_info["row"]
        y = grid_info["column"]
        res_digging = self.game_board.dig(x, y)
        # check whether it's the end
        if res_digging:
            if self.game_board.get_win():
                self.lbl_middle["text"] = "Félicitations, vous avez gagné !"
            else:
                self.lbl_middle["text"] = "Désolée, vous avez perdu..."
            # disable the Buttons in the grid
            for x in range(self.dim_x):
                for y in range(self.dim_y):
                    frm_grid = self.frm_game.grid_slaves(x, y)[0]
                    btn_grid = frm_grid.winfo_children()[0]
                    btn_grid.config(state="disable")

        # display the game
        board_display = self.game_board.display_matrix()
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                frm_grid = self.frm_game.grid_slaves(x, y)[0]
                btn_grid = frm_grid.winfo_children()[0]
                btn_grid["text"] = board_display[x][y]
        return

    def handle_right_click(self, event):
        # flag modification
        grid_info = event.widget.master.grid_info()
        x = grid_info["row"]
        y = grid_info["column"]
        self.game_board.modify_state_flag(x, y)
        # modify only the widget's appearance
        board_display = self.game_board.display_matrix()
        event.widget["text"] = board_display[x][y]
        # modify the number of mines to find
        if board_display[x][y] == "@":
            to_decrease = int(self.lbl_nb_left_mines["text"])
            self.lbl_nb_left_mines["text"] = str(to_decrease - 1)
        else:
            to_increase = int(self.lbl_nb_left_mines["text"])
            self.lbl_nb_left_mines["text"] = str(to_increase + 1)
        return

"""
est-ce qu'on peut obtenir tous les widgets qui se trouvent dans une Frame, a partir de la Frame ?
Oui, avec .winfo_children()
"""

"""
si j'ai bien compris, quand on appelle TkInterface, si on ne met pas root comme master,
alors quand on ferme, il n'y a pas de probleme
apres test, c'est bon
"""
"""
les boutons pour la taille de la grille et le nombre de mines : 
il faut definir l'interface avant le game board, 
demander les chiffres, puis definir le game board et la grille dans l'interface. 
les boutons pour entrer les parametres ne doivent plus etre utilisables apres
"""

app = GameInterface()
app.mainloop()
