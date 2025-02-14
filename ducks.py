import random
import random as rd
import pygame
colors = ["black"]
directions = ["right"]
duck_status = {1: "hidden", 2 : "flying", 3 : "dead", 4 : "flown"}




class DUCK:
    def __init__(self):
        self.color = rd.choice(colors)
        self.direction = rd.choice(directions)
        self.starting_position = {"x" : random.randint(50,850), "y" : 450}
        self.move1 = pygame.image.load(f"images/duck.gif")
        self.move2 = pygame.image.load(f"images/nova.gif")
        self.move3 = pygame.image.load(f"images/duck_left.gif")
        self.move4 = pygame.image.load(f"images/nova_left.gif")
        self.move5 = pygame.image.load(f"images/Maxos2.gif")
        self.status = 1


# duck= DUCK()
# print(duck.starting_position)












