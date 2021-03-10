from source.Board import Board
import tkinter as tk


class GameInterface(tk.Frame):
    def __init__(self, master=None, dim_x=10, dim_y=10, nb_mines=20):
        self.game_board = Board(dim_x, dim_y, nb_mines)
        self.dim_x = dim_x
        self.dim_y = dim_y
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # title display
        self.frm_top = tk.Frame(master=self)
        self.lbl_title = tk.Label(master=self.frm_top, text="Démineur")
        self.lbl_title.pack()
        self.frm_top.pack()

        # some infos display
        self.frm_middle = tk.Frame(master=self)  # pas sure du master=self
        self.lbl_middle = tk.Label(master=self.frm_middle, text="", width=25, height=1)
        self.lbl_middle.pack()
        self.frm_middle.pack()

        # gameboard display
        self.frm_game = tk.Frame(master=self)  # pas sure du master=self
        for row in range(self.dim_x):
            for column in range(self.dim_y):
                # relief et borderwidth sont necessaires pour avoir les traits qui separent les Frames
                frm_grid = tk.Frame(master=self.frm_game, relief=tk.RAISED, borderwidth=1)
                btn_grid = tk.Button(master=frm_grid, text=".", width=2, height=1) # affichage
                btn_grid.bind("<Button-1>", self.handle_left_click)
                btn_grid.bind("<Button-3>", self.handle_right_click)
                btn_grid.pack()
                frm_grid.grid(row=row, column=column)

        self.frm_game.pack()
        return

    def handle_left_click(self, event):
        # appeler dig
        grid_info = event.widget.master.grid_info()
        x = grid_info["row"]
        y = grid_info["column"]
        res_digging = self.game_board.dig(x, y)
        # voir si le joueur a gagne ou perdu
        if res_digging:
            if self.game_board.get_win():
                self.lbl_middle["text"] = "Félicitations, vous avez gagné !"
            else:
                self.lbl_middle["text"] = "Désolée, vous avez perdu..."
            # disable the Buttons
            for x in range(self.dim_x):
                for y in range(self.dim_y):
                    frm_grid = self.frm_game.grid_slaves(x, y)[0]
                    btn_grid = frm_grid.winfo_children()[0]
                    btn_grid.config(state="disable")

        # afficher
        board_display = self.game_board.display_matrix()
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                frm_grid = self.frm_game.grid_slaves(x, y)[0]
                btn_grid = frm_grid.winfo_children()[0]
                btn_grid["text"] = board_display[x][y]
        return

    def handle_right_click(self, event):
        # modification du drapeau
        # ce n'est pas le bouton qui est grid, c'est le frame qui le contient
        grid_info = event.widget.master.grid_info()
        x = grid_info["row"]
        y = grid_info["column"]
        self.game_board.modify_state_flag(x, y)
        # modification de ce qui est a l'ecran
        board_display = self.game_board.display_matrix()
        event.widget["text"] = board_display[x][y]
        return


# est-ce qu'on peut obtenir tous les widgets qui se trouvent dans une Frame, a partir de la Frame ?

# si j'ai bien compris, quand on appelle TkInterface, si on ne met pas root comme master,
# alors quand on ferme, il n'y a pas de probleme
# apres test, c'est bon

app = GameInterface()
app.mainloop()
