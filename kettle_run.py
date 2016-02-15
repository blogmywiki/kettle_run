# Kettle Run - a slalom-type MicroBit game by Giles Booth @blogmywiki
# Guide your ship to home port and put the kettle on.
# Can you do the Kettle Run in less than 12 parsecs?

from microbit import *
from music import play, NYAN, POWER_UP, FUNERAL, JUMP_UP, JUMP_DOWN

# edit terrain to make game harder
# add lines etc. & the code should cope

def game_run():
    terrain = Image("00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00000:"
                    "00005:"
                    "00055:"
                    "05555:"
                    "00555:"
                    "00055:"
                    "00005:"
                    "00055:"
                    "05555:"
                    "00555:"
                    "00055:"
                    "00005:"
                    "50005:"
                    "00055:"
                    "50000:"
                    "55000:"
                    "55500:"
                    "55000:"
                    "50000:"
                    "00000:"
                    "00005:"
                    "00055:"
                    "00005:"
                    "00055:"
                    "00555:"
                    "00055:"
                    "55055")
    image_height = terrain.height()    
    ship_height = 4
    global crash
    global speed
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
        display.scroll('CRASH!')
        break
    else:
        play(POWER_UP, wait=False)
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
