import tkinter as tk
import function
import globalVar
import rootWindow
import variable

class addWindow:
    def __init__(self,window):
        self.root = window

        self.mainFrame = tk.Frame(self.root)
        self.idLabel = tk.Label(self.mainFrame, text="Button ID")
        self.idEntry = tk.Entry(self.mainFrame)
        self.timeLabel = tk.Label(self.mainFrame, text="Time press [s]")
        self.timeEntry = tk.Entry(self.mainFrame)
        # uzywam lambdy poniewaz funkcja dataIntegrator wymaga podania argumentow
        self.setconfiguration = tk.Button(self.mainFrame, text="Set",
                                          command=lambda: self.data_integrator_fun(self.idEntry.get(),
                                                                                   self.timeEntry.get()))
        self.buttonReturn = tk.Button(self.mainFrame, text="RETURN", command=self.return_fun)
        self.refresh_fun()
    def refresh_fun(self):
        self.mainFrame.pack(fill=tk.BOTH, expand=True)
        self.idLabel.place(relwidth=1, relheight=0.1, rely=0.1)
        self.idEntry.place(relwidth=0.5, relheight=0.1, rely=0.2, relx=0.1)
        self.timeLabel.place(relwidth=1, relheight=0.1, rely=0.5)
        self.timeEntry.place(relwidth=0.5, relheight=0.1, relx=0.1, rely=0.7)
        self.setconfiguration.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.4)
        self.buttonReturn.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.75)
    def data_integrator_fun(self,id,time):
        if not id or not time:
            #sprawdzanie czy zmienne nie sa puste
            function.error_fun(variable.listError[2])
            return
        else:
            if len(id) != 1:
                #sprawdzanie czy zmienna id sklada sie z jednego przycisku
                function.error_fun(variable.listError[3])
                return
            else:
                #sprawdzanie czy zmienna time zawiera znaki nie bedace liczbami
                for item in time:
                    if item.isalpha():
                        function.error_fun(variable.listError[4])
                        return
                print("Correct!")
                globalVar.buttonId.append(id)
                globalVar.buttonTime.append(time)
                self.return_fun()
    def return_fun(self):
        function.window_clear_fun(self.root)
        state = rootWindow.Root(self.root)