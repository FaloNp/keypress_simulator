import tkinter as tk
import rootWindow
import variable

root = tk.Tk()  # tworzenie nowego okienka
size = variable.main_Width + "x" + variable.main_Height
root.geometry(size)  # wymiary okienka
root.resizable(True, True)
root.minsize(width=500, height=500)
root.title("FaloNp")
Root = rootWindow.Root(root)
