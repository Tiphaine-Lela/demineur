import time
import tkinter as tk


class Lbl_chrono(tk.Label):
    def __init__(self, master=None, width=None, height=None):
        tk.Label.__init__(self, master=master, width=width, height=height)
        self.__setitem__('text', "0")
        self.flag = 0
        self.beginning = 0

    def start_chrono(self):
        # allows to call start_chrono again and have no effect on the chrono
        if self.flag == 1:
            return
        self.flag = 1
        self.beginning = time.time()
        self.top_horloge()
        return

    def stop_chrono(self):
        self.flag = 0

    def top_horloge(self):
        y = time.time()-self.beginning
        minutes = time.localtime(y)[4]
        secondes = time.localtime(y)[5]
        if self.flag:
            self.__setitem__('text', "%i" %(60 * minutes + secondes))
        self.after(1000, self.top_horloge)

