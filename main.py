import random, time
# import player
import pygame,ducks
import sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

playing = True

class PLAYER:
    def __init__(self) :
        self.score = 0
        self.flock = []

    def creating_flock(self) :
        for d in range(1, 11) :
            duck = ducks.DUCK()
            self.flock.append(duck)


    def active_duck(self) :
        for i in self.flock:
            if i.status == 1:
                i.status = 2
                active_duck = self.flock[self.flock.index(i)]
                return active_duck
            elif i.status == 2:
                active_duck = self.flock[self.flock.index(i)]
                return active_duck
            else:
                continue

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1152,648))
pygame.display.set_caption('Polovnik Maxos')
bg = pygame.image.load("images/background_base_day_summer.png").convert()
pygame.mouse.set_visible(1)
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR )
player = PLAYER()
player.creating_flock()
ammu = len(player.flock) + 3
to_the_left = True

while playing:
    pygame.display.update()
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.blit(bg,[0,0])
    clock.tick(9)
    player.active_duck()
    accuracy = 100
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 30)
    shots = 0
    hidden = 0
    missed = 0
    for i in player.flock:
        if i.status == 1:
            hidden += 1
        elif i.status == 3:
            shots += 1
        elif i.status == 4:
            missed += 1


    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONUP:
            if ammu > 0:
                position_x = pygame.mouse.get_pos()[0]
                position_y = pygame.mouse.get_pos()[1]
                ammu -= 1
                if position_x in range(player.active_duck().starting_position["x"] - accuracy, player.active_duck().starting_position["x"] + accuracy) and position_y in range(player.active_duck().starting_position["y"] - int(accuracy * 1.5), player.active_duck().starting_position["y"] + int(accuracy * 1.5)):
                    player.active_duck().status = 3
                    if len(player.flock) == 0:
                        playing = False
                    pygame.MOUSEBUTTONDOWN

                else:
                    pygame.MOUSEBUTTONDOWN
                    continue
            else:
                continue
    max_x = 1152
    max_y = 648
    final_score = int((shots/len(player.flock)*100)+ammu)
    try :
        player.active_duck().starting_position["x"]
    except :
        score = myfont.render(f"Zastrelené kačice: {shots}", True, (255, 255, 0))
        screen.blit(score, (15, 10))

        ammu1 = myfont.render(f"Munícia: {ammu}", True, (255, 255, 0))
        screen.blit(ammu1, (15, 40))

        hidden1 = myfont.render(f"Kačice v kríkoch: {hidden}", True, (255, 255, 0))
        screen.blit(hidden1, (15, 70))

        missed1 = myfont.render(f"Uletené kačice: {missed}", True, (255, 255, 0))
        screen.blit(missed1, (15, 100))
        messagebox.showinfo(message=f"Maxoš vyplašil {len(player.flock)} kacic\nZastrelil si {shots}\n"
                                    f"Ušetrené náboje: {ammu}\nTvoje konečné Skóre je: {final_score}",
                            title="Výsledky lovu"
                            )
        playing = False
    else :
        # the more negative numbers in list, the more the duck changes direction
        movement = [25, 25, 25, 25, 25, 25, 25, 25, 25]
        if not to_the_left :
            if random.randint(1, 2) % 2 :
                if player.active_duck().starting_position["x"] < max_x and player.active_duck().starting_position[
                    "y"] > -100 and playing :
                    screen.blit(player.active_duck().move1, dest=[player.active_duck().starting_position["x"],
                                                                  player.active_duck().starting_position["y"]])
                    new_direction = random.choice(movement)
                    player.active_duck().starting_position["x"] += new_direction
                    player.active_duck().starting_position["y"] += -25
                    if new_direction == 25 :
                        to_the_left = False
                    else :
                        to_the_left = True
                else :
                    player.active_duck().status = 4
                    player.active_duck()
            else :
                if player.active_duck().starting_position["x"] < max_x and player.active_duck().starting_position[
                    "y"] > -100 and playing :
                    screen.blit(player.active_duck().move2, dest=[player.active_duck().starting_position["x"],
                                                                  player.active_duck().starting_position["y"]])
                    new_direction = random.choice(movement)
                    player.active_duck().starting_position["x"] += new_direction
                    player.active_duck().starting_position["y"] += -25
                    if new_direction == 25 :
                        to_the_left = False
                    else :
                        to_the_left = True
                else :
                    player.active_duck().status = 4
                    player.active_duck()
        else :
            if random.randint(1, 2) % 2 :
                if player.active_duck().starting_position["x"] < max_x and player.active_duck().starting_position[
                    "y"] > -100 and playing :
                    screen.blit(player.active_duck().move3, dest=[player.active_duck().starting_position["x"],
                                                                  player.active_duck().starting_position["y"]])
                    new_direction = random.choice(movement)
                    player.active_duck().starting_position["x"] += new_direction
                    player.active_duck().starting_position["y"] += -25
                    if new_direction == 25 :
                        to_the_left = False
                    else :
                        to_the_left = True
                else :
                    player.active_duck().status = 4
                    player.active_duck()
            else :
                if player.active_duck().starting_position["x"] < max_x and player.active_duck().starting_position[
                    "y"] > -100 and playing :
                    screen.blit(player.active_duck().move4, dest=[player.active_duck().starting_position["x"],
                                                                  player.active_duck().starting_position["y"]])
                    new_direction = random.choice(movement)
                    player.active_duck().starting_position["x"] += new_direction
                    player.active_duck().starting_position["y"] += -25
                    if new_direction == 25 :
                        to_the_left = False
                    else :
                        to_the_left = True
                else:
                    player.active_duck().status = 4
                    player.active_duck()
    score = myfont.render(f"Zastrelené kačice: {shots}", True, (255, 255, 0))
    screen.blit(score, (15, 10))

    ammu1 = myfont.render(f"Munícia: {ammu}", True, (255, 255, 0))
    screen.blit(ammu1, (15, 40))

    hidden1 = myfont.render(f"Kačice v kríkoch: {hidden}", True, (255, 255, 0))
    screen.blit(hidden1, (15, 70))

    missed1 = myfont.render(f"Uletené kačice: {missed}", True, (255, 255, 0))
    screen.blit(missed1, (15, 100))
pygame.quit()