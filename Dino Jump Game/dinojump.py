"""
Ethan Dahlby (ed6tf), PA 18: dinojump.py
This program is a copy of Google's dinosaur game. When you press the Space button, it makes the dinosaur jump. You have
to jump over cacti, and your score increases by one when you do. If you hit a cactus, you get a game over, and have to
press space to restart. The cacti speed up as your score increases, and every 20 points, the theme changes from day to
night. One problem that you might see is that sometimes when you jump over a cactus, the score fails to increase. This
will probably happen more at higher speeds. Also, while each cactus is jumpable, the cacti might spawn in a position
that makes jumping over all of them impossible.
"""

import pygame
import gamebox  # Made by Luther Tychonievich
import random
camera = gamebox.Camera(800, 600)

score = 0

spacing = random.randint(800, 1200)  # This randomly determines the position of the cacti
ground = gamebox.from_color(800, 600, "black", 1600, 200)
dino = gamebox.from_color(200, 300, "red", 25, 25)
cactus1 = gamebox.from_color(spacing, 300, "green", 10, random.randint(30,60))  # The cacti are random heights
cactus2 = gamebox.from_color(spacing + random.randint(150, 300), 300, "green", 10, random.randint(30,60))
cactus3 = gamebox.from_color(spacing + random.randint(450, 600), 300, "green", 10, random.randint(30,60))

objects = [dino, cactus1, cactus2, cactus3]
cacti = [cactus1, cactus2, cactus3]
game_over = False
night = False
changed_night = False

def tick(keys):
    """
    This is the main function of the program, which details the continuous actions of the objects.
    :param keys: The keys the user presses.
    :return: Nothing.
    """
    global objects
    global game_over
    global score
    global night
    global changed_night

    if pygame.K_SPACE in keys and game_over == False:
        if dino.y == 487.5 or dino.y == 488.5:
            dino.speedy = -15  # If the dino is on the ground, the game is running, and space is pressed, the dino jumps

    for object in objects:
        if object.touches(ground):  # Ground collision
            object.move_to_stop_overlapping(ground)
        if object.y > 487.5:
            object.y = 487.5
        object.speedy += 1  # Gravity
        object.y += object.speedy

    # If the cacti move off screen to the left, reposition them on the other side of the screen out of frame of the
    # camera
    if cactus1.x < 0:
        cactus1.x = random.randint(800, 850)
    if cactus2.x < 0:
        cactus2.x = random.randint(800, 850) + random.randint(200, 350)
    if cactus3.x < 0:
        cactus3.x = random.randint(800, 850) + random.randint(550, 700)

    if dino.x + 15 > cactus1.x > dino.x + 10 and dino.touches(cactus1) == False:  # If the dino jumps over the cactus
        score += 1
        changed_night = False
    if dino.x + 15 > cactus2.x > dino.x + 10 and dino.touches(cactus2) == False:
        score += 1
        changed_night = False
    if dino.x + 15 > cactus3.x > dino.x + 10 and dino.touches(cactus3) == False:
        score += 1
        changed_night = False

    for cactus in cacti:
        cactus.x -= 5 + (score/10)
        # The cacti move left to simulate the dinosaur running. As the score increases, they speed up.
        if dino.touches(cactus):
            game_over = True
        if game_over:
            dino.y = 999
            cactus.x = 999

    score_display = gamebox.from_text(100, 100, str(score), 100, "black")

    if pygame.K_SPACE in keys and game_over == True:  # Press space to start a new game
        game_over = False
        score = 0
        night = False
        changed_night = False
        dino.y = 300
        dino.speedy = 0
        cactus1.x = random.randint(800, 850)
        cactus2.x = random.randint(800, 850) + random.randint(100, 150)
        cactus3.x = random.randint(800, 850) + random.randint(250, 400)

    if score > 0 and score % 20 == 0 and not night and not changed_night:
        # Every 20 points, day switches to night and vice versa
        night = True
        changed_night = True
    elif score > 0 and score % 20 == 0 and night and not changed_night:
        night = False
        changed_night = True

    if night:
        camera.clear("blue")
    else:
        camera.clear("white")

    camera.draw(ground)
    camera.draw(dino)
    camera.draw(cactus1)
    camera.draw(cactus2)
    camera.draw(cactus3)
    camera.draw(score_display)
    camera.display()

TICKS_PER_SECOND = 60  # This tick function runs 60 times per second

gamebox.timer_loop(TICKS_PER_SECOND, tick)
