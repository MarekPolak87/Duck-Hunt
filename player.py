import ducks, main
from tkinter import *
from tkinter import messagebox

class PLAYER:
    def __init__(self) :
        self.score = 0
        self.flock = []

    def creating_flock(self) :
        for d in range(1, 8) :
            duck = ducks.DUCK()
            self.flock.append(duck)


    def active_duck(self) :
        try:
            active_duck = self.flock[0]
        except:
            messagebox.showinfo("GAME OVER")
        else:
            return active_duck



    def removing_duck_from_flock(self):
        del self.flock[0]


#
# #
# Polovnik = PLAYER()
# Polovnik.creating_flock()
#
# print(Polovnik.flock)
# print(len(Polovnik.flock))
# print(Polovnik.active_duck())
# Polovnik.removing_duck_from_flock()
#
# print(Polovnik.flock)
# print(len(Polovnik.flock))
# print(Polovnik.active_duck())
# Polovnik.removing_duck_from_flock()
#
# print(Polovnik.flock)
# print(len(Polovnik.flock))
# print(Polovnik.active_duck())
# Polovnik.removing_duck_from_flock()
#
# print(Polovnik.flock)
# print(len(Polovnik.flock))
# print(Polovnik.active_duck())
# Polovnik.removing_duck_from_flock()

# for i in Polovnik.flock:
#     print(Polovnik.flock)