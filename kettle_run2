# KettleRun2: a more challenging game with randomised terrain
# Guide your ship to home port and put the kettle on.
# Can you do the Kettle Run in less than 12 parsecs?

from microbit import *
import random
from music import play, NYAN, POWER_UP, FUNERAL, JUMP_UP, JUMP_DOWN

# edit terrain blocks to make game harder

teacup1 = Image("00000:"
                "99999:"
                "99909:"
                "99999:"
                "99900")

teacup2 = Image("05000:"
                "99999:"
                "99909:"
                "99999:"
                "99900")
                
teacup3 = Image("00500:"
                "99999:"
                "99909:"
                "99999:"
                "99900")

def teacup_animate(times):
    for x in range(times):
        display.show(teacup1)
        sleep(500)
        display.show(teacup2)
        sleep(500)
        display.show(teacup3)
        sleep(500)

def build_terrain(length):
    canyon_lines=["00000:00005:00055:00555:00055:00005:",
    "50000:55000:55500:55550:55000:",
    "50005:55005:50055:50005:00005:",
    "00055:00555:00005:55000:55005:50005:"]
    terrainString = "00000:00000:00000:00000:"
    for i in range(length):
        z = random.randint(0,3)
        terrainString = terrainString + canyon_lines[z]
    terrainString = terrainString + "50005:55055"   
    terrainImage = Image(terrainString)
    return terrainImage

def game_run():
    global level
    global crash
    global speed
    terrain = build_terrain(2+(level*2))
    image_height = terrain.height()    
    ship_height = 4
    for i in range(image_height):
        if button_a.was_pressed():
            play(JUMP_UP, wait=False)
            ship_height -= 1
            if ship_height < 0:
                ship_height = 0
        if button_b.was_pressed():
            play(JUMP_DOWN, wait=False)
            ship_height += 1
            if ship_height > 4:
                ship_height = 4
        if terrain.get_pixel(ship_height, 0) == 5:
            crash = True
            break
        terrain.set_pixel(ship_height, 0, 9)
        display.show(terrain)
        sleep(speed)
        terrain = terrain.shift_up(1)

speed = 500
crash = False
won = False
level = 1

display.scroll('Kettle Run')

while level < 6:         # increase this number to add more levels
    display.show(str(level))
    sleep(1000)
    game_run()
    if crash:
        play(FUNERAL, wait=False)
        break
    else:
        play(POWER_UP, wait=False)
        teacup_animate(2)
        display.scroll('Tea up!')
        level += 1
        speed -= 20       # increase this number to speed up more on each level

if not crash:        
    play(NYAN, wait=False)
    display.show('YOU WIN')
    while True:
        display.scroll('Press reset to play again')
else:
    display.show('GAME OVER')
    sleep(1000)
    while True:
        display.scroll('Press reset to play again')
