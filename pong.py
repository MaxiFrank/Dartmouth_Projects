# Maxine Liu
# 9/25/2018
# COSC 1
# Pong script - Wednesday check point assignment. Red paddles are on the left and right side of the screen.
# They are controlled by keys "a", "z", "k", and "m"
# a moves the left paddle up
# z moves the left paddle down
# k moves the right paddle up
# m moves the right paddle down


from cs1lib import *

PADDLE_LENGTH = 80
PADDLE_WIDTH = 20
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
SPEED = 10  # type: int # rate at which the location of the paddle moves up and down

# Initialize the state variables.
left_paddle_x = 0    # x location of left paddle
left_paddle_y = 0    # Y location of left paddle
right_paddle_x = 380    # x location of right paddle
right_paddle_y = 320    # y location of right paddle
pressed_a = False       # is 'a' key currently pressed?
pressed_z = False       # is 'z' key currently pressed?
pressed_k = False       # is 'k' key currently pressed?
pressed_m = False       # is 'm' key currently pressed?


def draw_paddles():
    global left_paddle_x, left_paddle_y, right_paddle_x, right_paddle_y
    # draw paddle on the left
    disable_stroke()
    set_fill_color(1, 0, 0)
    draw_rectangle(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH)

    # draw paddle on the right
    disable_stroke()
    set_fill_color(1, 0, 0)
    draw_rectangle(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH)

# If "a", "z", "k", or "m" is pressed, record that it was pressed.

def key_down(key):
    global pressed_a, pressed_z, pressed_k, pressed_m
    if key == "a":
        pressed_a = True
    elif key == "z":
        pressed_z = True
    elif key == "k":
        pressed_k = True
    elif key == "m":
        pressed_m = True

# If "a", "z", "k", or "m" is pressed, record that it was released.

def key_up(key):
    global pressed_a, pressed_z, pressed_k, pressed_m

    if key == "a":
        pressed_a = False
    elif key == "z":
        pressed_z = False
    elif key == "k":
        pressed_k = False
    elif key == "m":
        pressed_m = False

    # to move the paddles up and down

def move_paddles():
    global left_paddle_x, right_paddle_x, left_paddle_y, right_paddle_y
    clear()
    # draw the yellow background
    set_fill_color(1, .8, 0)
    draw_rectangle(0, 0, 400, 400)

    #  draw the paddles
    draw_paddles()

    #  if "a" is pressed, move the left paddle up
    if pressed_a:
        if left_paddle_y > 0:
            left_paddle_y -= SPEED
    #  if "z" is pressed, move the left paddle down
    if pressed_z:
            if left_paddle_y < 320:
                left_paddle_y += SPEED
    #  if "k" is pressed, move the right paddle up
    if pressed_k:
        if right_paddle_y > 0:
            right_paddle_y -= SPEED
    #  if "m" is pressed, move the right paddle down
    if pressed_m:
        if right_paddle_y < 320:
            right_paddle_y += SPEED


start_graphics(move_paddles, title = "Pong", width = WINDOW_WIDTH, height= WINDOW_HEIGHT, framerate = 50, key_press=key_down, key_release=key_up)


