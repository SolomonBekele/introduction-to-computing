from cs1robots import *
load_world('prob19.wld')
hubo=Robot(orientation='N')
hubo.set_pause(0.02)
def turn_right():
    for i in range(3):
        hubo.turn_left()
def turn_down():
    for i in range(2):
        hubo.turn_left()
def collect_beepers():
    while hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
def add_beepers():
    turn_down()
    while hubo.front_is_clear():
        hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
for i in range(9):
    collect_beepers()
    add_beepers()
collect_beepers()
turn_down()
while hubo.front_is_clear():
    hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()
   
turn_right()
while hubo.front_is_clear():
    hubo.move()
turn_down()
