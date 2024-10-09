import tkinter as tk
from PIL import Image, ImageTk

class Error:
    def __init__(self,info):
       self.root = tk.Tk()
       self.root.geometry("500x200")
       self.root.resizable(False, False)
       self.root.title("Error!")
       self.info=info
       self.path = "photo/error.png"
       print(self.info)
       # Load the image using Pillow
       self.image_file = Image.open(self.path)
       self.image = ImageTk.PhotoImage(self.image_file)

       self.mainFrame = tk.Frame(self.root)
       self.mainFrame.pack(fill=tk.BOTH, expand=True)

       self.leftColumn = tk.Frame(self.mainFrame)
       self.leftColumn.place(relwidth=0.5, relheight=1, relx=0, rely=0)

       #nie mam pojecia czemu nie dziala xd
       #self.label = tk.Label(self.leftColumn, image=self.image)
       #self.label.pack()

       self.rightColumn = tk.Frame(self.mainFrame)
       self.rightColumn.place(relwidth=0.7, relheight=1, relx=0.15, rely=0)

       self.informationFrame=tk.Frame(self.rightColumn)
       self.informationFrame.place(relwidth=1, relheight=0.2, relx=0, rely=0.2)
       self.errorinfo = tk.Label(self.informationFrame, text="Error!")
       self.errorinfo.pack()
       self.errordescription = tk.Label(self.informationFrame, text=self.info)
       self.errordescription.pack()

       self.button = tk.Button(self.root, text="Ok", command=self.exit_fun)
       self.button.place(relwidth=0.2, relheight=0.2, relx=0.7, rely=0.5)
       self.root.attributes('-topmost', True)
       self.root.mainloop()

    def exit_fun(self):
        self.root.destroy()

