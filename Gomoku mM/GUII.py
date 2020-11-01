import tkinter as tk


class Application(object):
    def __init__(self, master, humanGame, aiGame):
        self.master = master
        self.humanGame = humanGame
        self.aiGame = aiGame
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Label(self)
        self.menu.config(text = "MENU", fg="brown")
        self.menu.pack(side = "top", expand = 1)

        self.humanMatch = tk.Button(self)
        self.humanMatch["text"] = "1. Human vs Human"
        self.humanMatch["command"] = self.humanGame.mainloop()
        self.humanMatch.pack( expand = 1, fill= "both")

        self.aiMatch = tk.Button(self)
        self.aiMatch["text"] = "2. Human vs AI"
        self.aiMatch["command"] = self.aiGame.mainloop()
        self.aiMatch.pack( expand = 1, fill= "both")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side = "bottom", expand = 1)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(root,None,None)
app.mainloop()