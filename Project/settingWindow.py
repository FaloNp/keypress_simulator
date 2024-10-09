import glob

import function
import globalVar
import rootWindow
import variable
import tkinter as tk


class Setting():
    def __init__(self, window):
        self.root = window
        self.clicked = 0
        self.buffor = ""

        self.leftColumn = tk.Label(self.root, bg="white")
        self.header = tk.Label(self.leftColumn, text="Lista wykrytych szablonow")

        self.rightColumn = tk.Label(self.root)
        self.buttonLoad = tk.Button(self.rightColumn, text="LOAD", command=self.load_fun, state=tk.DISABLED)
        self.buttonReturn = tk.Button(self.rightColumn, text="RETURN", command=self.return_fun)

        self.refresh_fun()

        self.root.mainloop()

    def refresh_fun(self):
        self.root.update()
        self.leftColumn.place(relwidth=0.5, relheight=1, relx=0, rely=0)
        self.header.pack()

        filename = glob.glob('*.txt')  # wyciaganie nazw wszystkich plikow tekstowtych do zmiennej filename
        for i, name in enumerate(filename):  # przekazuje tekst z fumckji tk.Entry
            x = tk.Button(self.leftColumn, bg="orange", text=name, command=lambda n=name: self.caught_text_fun(n))
            x.place(relwidth=1, relheight=0.05, relx=0, rely=0 + i * 0.05)

        self.rightColumn.place(relwidth=0.5, relheight=1, relx=0.5, rely=0)
        self.buttonLoad.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.4)
        self.buttonReturn.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.7)
        self.root.update()

    def load_fun(self):
        globalVar.fileName = self.buffor
        self.return_fun()

    def return_fun(self):
        function.window_clear_fun(self.root)
        state = rootWindow.Root(self.root)

    def caught_text_fun(self, text):
        self.buffor = text
        self.clicked = 1
        print(self.buffor)
        self.buttonLoad.config(state=tk.NORMAL)
        self.root.update()
