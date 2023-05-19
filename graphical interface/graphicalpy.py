from tkinter import *
from ttk import *
import random
import Rock_Paper_Scissors
import Hangman
import Poker

root = Tk()
root.title("Games")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text="Welcome to the Games app!")

intro.pack(side = TOP)

rps_button = Button(mainframe, text="Rock, Paper, Scissors", command = rock_paper_scissors)
rps_button.pack()

hm_button = Button(mainframe, text="Hangman", command = hangman)
hm_button.pack()

hm_button = Button(mainframe, text="Poker", command = poker)
hm_button.pack()

exit_button = Button(mainframe, text="Exit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()

from tkinter import *
from ttk import *
import random

def gui():
    rock = 1
    paper = 2
    scissors = 3

    names = { rock: "Rock", paper:"Paper", scissors:"Scissors"}
    rules = { rock: scissors, paper: rock, scissors: paper}

    def start():
        while game():
            pass
    def game():
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer)

    def resut(player, computer):
        new_score = 0
        if player == computer:
            resut_set.set("Tie game.")
        else:
            if rules[player] == computer:
                result_set.set("Your victory has been assured.")
                new_score = player_score.get()
                new_score += 1
                player_score.set(new_score)
            else:
                resut_set.set("The computer laughs as you realise you have been defeaated.")
                new_score = computer_score.get()
                new_score += 1
                computer_score.set(new_score)

    rps_window = Toplevel()
    rps_widow.title ("Rock, Paper, Scissors")

    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()
    #hola