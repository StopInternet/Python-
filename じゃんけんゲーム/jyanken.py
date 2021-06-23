import tkinter as tk
import random as rd

class Image():
    def __init__(self, image, x, y, z):
        self.image = tk.PhotoImage(file = "image/" + image).subsample(z)
        self.x = x
        self.y = y

class Application(tk.Frame):
    def __init__(self, player, enemy, master):
        super().__init__(master)

        master.geometry("300x350")
        master.title("じゃんけんゲーム")

        self.Player = player
        self.Enemy = enemy
        self.RandCounter = 0
        self.JudgeNumber = 0
        self.EnemyLabel = []

        for i in range(3):
            tk.Label(master, image = self.Player[i].image).place(x = self.Player[i].x, y = self.Player[i].y)

        for i in range(3):
            self.EnemyLabel.append(tk.Label(master, image = self.Enemy[i].image))

        self.RButton = tk.Button(master, text = "グー")
        self.RButton.place(x = 45, y = 300)

        self.SButton = tk.Button(master, text = "チョキ")
        self.SButton.place(x = 130, y = 300)

        self.PButton = tk.Button(master, text = "パー")
        self.PButton.place(x = 225, y = 300)

        self.RetryButton = tk.Button(master, text = "リトライ！")
        self.RetryButton.place(x = 220, y = 160)

        self.WinText = tk.Label(master, text = "勝ち！", fg = "red", font = ("Impact", 20, "bold"))
        self.LoseText = tk.Label(master, text = "負け！", fg = "black", font = ("Impact", 20, "bold"))
        self.DrowText = tk.Label(master, text = "引き分け！", fg = "green", font = ("Impact", 20, "bold"))

        master.after(50, self.Update)

        self.pack()

    def Update(self):

        if self.JudgeNumber == 0:
            self.EnemyLabel[self.RandCounter].place_forget()
            self.RandCounter = rd.randint(0,2)
            self.PrintEnemy(self.RandCounter)

        self.master.after(50, self.Update)

    def PrintEnemy(self, randCounter):

        if randCounter == 0:
            self.EnemyLabel[randCounter].place(x = self.Enemy[randCounter].x, y = self.Enemy[randCounter].y)

        elif randCounter == 1:
            self.EnemyLabel[randCounter].place(x = self.Enemy[randCounter].x, y = self.Enemy[randCounter].y)

        else:
            self.EnemyLabel[randCounter].place(x = self.Enemy[randCounter].x, y = self.Enemy[randCounter].y)

    def Win(self):
        self.WinText.place(x = 50, y = 150)

    def Lose(self):
        self.LoseText.place(x = 50, y = 150)

    def Drow(self):
        self.DrowText.place(x = 50, y = 150)


def main():

    win = tk.Tk()

    Player = []
    Enemy = []

    Player.append(Image("gu.ppm", 25, 220, 3))
    Player.append(Image("tyoki.ppm", 120, 205, 3))
    Player.append(Image("pa-.ppm", 200, 220, 3))

    Enemy.append(Image("gu.ppm", 100, 25, 2))
    Enemy.append(Image("tyoki.ppm", 100, 15, 2))
    Enemy.append(Image("pa-.ppm", 100, 25, 2))


    app = Application(Player, Enemy, master = win)


    def RJudge():
        app.JudgeNumber = 1

        if app.RandCounter == 0:
            app.Drow()
        elif app.RandCounter == 1:
            app.Win()
        elif app.RandCounter == 2:
            app.Lose()

    def SJudge():
        app.JudgeNumber = 1

        if app.RandCounter == 0:
            app.Lose()
        elif app.RandCounter == 1:
            app.Drow()
        elif app.RandCounter == 2:
            app.Win()

    def PJudge():
        app.JudgeNumber = 1

        if app.RandCounter == 0:
            app.Win()
        elif app.RandCounter == 1:
            app.Lose()
        elif app.RandCounter == 2:
            app.Drow()

    def RetryJudge():
        app.DrowText.place_forget()
        app.WinText.place_forget()
        app.LoseText.place_forget()
        app.JudgeNumber = 0

    app.RButton["command"] = RJudge
    app.SButton["command"] = SJudge
    app.PButton["command"] = PJudge
    app.RetryButton["command"] = RetryJudge

    app.mainloop()

if __name__ == "__main__":

    main()