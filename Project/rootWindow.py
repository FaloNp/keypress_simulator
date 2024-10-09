import tkinter as tk
import time

import function
import globalVar
import variable
import addWindow
import settingWindow
import pyautogui


class Root:
    def __init__(self, window):
        self.run = False

        self.size_width = int(variable.main_Width)
        self.size_height = int(variable.main_Height)

        self.root = window

        # Declaring elements in window:
        self.mainFrame = tk.Frame(self.root)
        self.leftColumn = tk.Canvas(self.mainFrame, width=self.size_width / 2)
        self.rightColumn = tk.Frame(self.mainFrame, bg="green", width=self.size_width / 2)
        self.headerLabel = tk.Label(self.leftColumn, text="BUTTON LIST")

        self.clock = tk.Label(self.rightColumn, text="", bg="white")

        self.buttonStart = tk.Button(self.root, text="Start", command=lambda: self.clock_start_fun(5))
        self.buttonAdd = tk.Button(self.root, text="Dodaj przycisk", command=self.add_button_fun)
        self.buttonStop = tk.Button(self.root, text="Stop", command=self.stop_fun, state=tk.DISABLED)
        self.buttonSetting = tk.Button(self.root, text="Ustawienia", command=lambda: self.open_setting_fun(self.root))
        self.buttonExit = tk.Button(self.root, text="Wyjscie", command=self.exit_fun)

        # Declaring array:
        self.idLabelList = []  # Inicjowanie tablicy w ktorej beda przechowywane nastepe obiekty "label" by sie pozniej do nich odnieść
        self.labelIdButtonList = []
        self.labelTimeButtonList = []

        self.buffId = []
        self.buffTime = []

        self.refresh()
        self.check_state_fun()
        self.root.mainloop()

    # Funkcje
    def refresh(self):

        self.root.update()

        # Place declared element
        self.mainFrame.pack(fill=tk.BOTH, expand=True)  # ustawia rozmiary ramki na takie jakie ma glowne okienko root
        self.leftColumn.grid(row=0, column=0, sticky="nsew")
        self.rightColumn.grid(row=0, column=1, sticky="nsew")  # prawa kolumna

        # Set grid 2x2
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.headerLabel.place(relwidth=1, relheight=0.1)

        if globalVar.fileName:
            information = function.file_read_fun(globalVar.fileName)
            # pobieranie informacji z pliku, dane sa zapisane w formacie [a b] gdzie a to przycisk ktory ma byc symulowany, b to czas
            self.buffId = function.spliter_fun(information, 0)  # rozbicie tablicy i pobranie parametru a
            self.buffTime = function.spliter_fun(information, 1)  # rozbicie tablicy i pobranie parametru b
        if globalVar.buttonId:
            self.buffId = self.buffId + globalVar.buttonId
            self.buffTime = self.buffTime + globalVar.buttonTime
        # Dynamiczna tabela (Ilosc elementow label jest zalezna od bazy danych information)
        if self.buffId:
            counter = 0
            for item in self.buffId:
                self.label = tk.Label(self.leftColumn)
                self.label.place(relwidth=1, relheight=0.1, relx=0, rely=0.1 * (counter + 1))
                self.labelIdButton = tk.Label(self.label, text=item, bg="white")
                self.labelIdButton.place(relwidth=0.5, relheight=1)
                self.labelTimeButton = tk.Label(self.label, text=self.buffTime[counter], bg="white")
                self.labelTimeButton.place(relwidth=0.5, relheight=1, relx=0.5)
                self.labelIdButtonList.append(self.labelIdButton)
                self.labelTimeButtonList.append(self.labelTimeButton)
                self.idLabelList.append(self.label)
                counter = counter + 1
        else:
            label = tk.Label(self.leftColumn, text="Select file from setting", bg="white")
            label.place(relwidth=1, relheight=0.1, relx=0.1, rely=0.4)

        # Place element in righ panel
        self.clock.place(relwidth=0.1, relheight=0.1, relx=0.1, rely=0.1)
        # Adding control panel
        self.buttonStart.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.1)
        self.buttonAdd.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.25)
        self.buttonStop.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.4)
        self.buttonSetting.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.55)
        self.buttonExit.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.7)

        self.root.update()

    def check_state_fun(self):
        """Update button states based on the program's run state"""
        if self.run:
            self.buttonStart.config(state=tk.DISABLED)
            self.buttonAdd.config(state=tk.DISABLED)
            self.buttonSetting.config(state=tk.DISABLED)
            self.buttonStop.config(state=tk.NORMAL)
        else:
            self.buttonStart.config(state=tk.NORMAL)
            self.buttonAdd.config(state=tk.NORMAL)
            self.buttonSetting.config(state=tk.NORMAL)
            self.buttonStop.config(state=tk.DISABLED)
        if not self.buffId:
            self.buttonStart.config(state=tk.DISABLED)
            self.root.update()
        else:
            self.buttonStart.config(state=tk.NORMAL)
        self.root.update()

    def clock_start_fun(self, i):
        """Countdown clock function"""
        if i > 0:
            self.clock.config(text=f'{i}')
            self.root.after(1000, self.clock_start_fun, i - 1)
        else:
            self.clock.config(text=" ")
            self.start_fun()

    def start_fun(self):
        self.run = True
        self.check_state_fun()
        counter = 0
        print(self.buffId)
        print(self.buffTime)
        while self.run:  # Continue as long as self.run is True
            for key, duration in zip(self.buffId, self.buffTime):
                self.labelIdButtonList[counter].config(bg='green')
                self.labelTimeButtonList[counter].config(bg='green')
                self.root.update()
                pyautogui.keyDown(key)
                time.sleep(float(duration))
                pyautogui.keyUp(key)
                self.labelIdButtonList[counter].config(bg='white')
                self.labelTimeButtonList[counter].config(bg='white')
                self.root.update()
                counter = (counter + 1) % len(self.buffId)  # Loop through buffId indices
                if not self.run:  # Check if self.run is still True
                    break  # Exit the loop if self.run is False
        self.check_state_fun()

    def stop_fun(self):
        self.run = False
        self.check_state_fun()

    def add_button_fun(self):
        function.window_clear_fun(self.root)
        state = addWindow.addWindow(self.root)

    def open_setting_fun(self, mainWindow):
        function.window_clear_fun(self.root)
        state = settingWindow.Setting(mainWindow)

    def exit_fun(self):
        self.root.destroy()
