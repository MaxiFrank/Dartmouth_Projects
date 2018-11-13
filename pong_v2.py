# Maxine Liu
# 9/30/2018
# COSC 1
# Game of pong to be played in Python.
# Paddles are controlled by keys "a", "z", "k", and "m"
# a moves the left paddle up
# z moves the left paddle
# k moves the right paddle up
# m moves the right paddle down
# q quits the game and closes the window
# space key initiates the game
# Could not figure out how to reset the game as I am already using the space key to start the game. I tried to turn
# game_stops into a Boolean and reuse the space key when games_stops and pressed_space are both true. But that didn't
# quite work.


from cs1lib import *

#   define global variables concerning paddle and window dimensions, in addition to speed at which the ball will be
#   moving during the game.
PADDLE_LENGTH = 80
PADDLE_WIDTH = 20
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_SPEED = 10  # type: int # rate at which the location of the paddle moves up and down
x_SPEED = 6     # type: int # rate at which the location of the ball moves left and right
y_SPEED = 6     # type: int # rate at which the location of the ball moves up and down

# Initialize the state variables.
left_paddle_x = 0  # x location of left paddle
left_paddle_y = 0  # Y location of left paddle
right_paddle_x = 380  # x location of right paddle
right_paddle_y = 320  # y location of right paddle

ball_center_x = 200   # x location of ball
ball_center_y = 200   # y location of ball
ball_radius = 10      # radius of ball

pressed_a = False  # is 'a' key currently pressed?
pressed_z = False  # is 'z' key currently pressed?
pressed_k = False  # is 'k' key currently pressed?
pressed_m = False  # is 'm' key currently pressed?
pressed_space = False   # is space key currently pressed?
pressed_q = False   # is the 'q' key currently pressed?

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


# If "a", "z", "k", "m", space or "q" is pressed, record that it was pressed.

def key_down(key):
    global pressed_a, pressed_z, pressed_k, pressed_m, pressed_space, pressed_q
    if key == "a":
        pressed_a = True
    elif key == "z":
        pressed_z = True
    elif key == "k":
        pressed_k = True
    elif key == "m":
        pressed_m = True
    elif key == " ":
        pressed_space = True
    elif key == "q":
        pressed_q = True



# If "a", "z", "k", or "m" is pressed, record that it was released.

def key_up(key):
    global pressed_a, pressed_z, pressed_k, pressed_m, pressed_space

    if key == "a":
        pressed_a = False
    elif key == "z":
        pressed_z = False
    elif key == "k":
        pressed_k = False
    elif key == "m":
        pressed_m = False

#   move the paddles up and down. I unfortunately can't figure out how to make the left and right paddles move
#   at the same time. Would appreciate feedback on how to correct it.
def move_paddles():
    global left_paddle_x, right_paddle_x, left_paddle_y, right_paddle_y

    #  if "a" is pressed, move the left paddle up
    if pressed_a:
        if left_paddle_y > 0:
            left_paddle_y -= PADDLE_SPEED
    #  if "z" is pressed, move the left paddle down
    if pressed_z:
        if left_paddle_y < 320:
            left_paddle_y += PADDLE_SPEED
    #  if "k" is pressed, move the right paddle up
    if pressed_k:
        if right_paddle_y > 0:
            right_paddle_y -= PADDLE_SPEED
    #  if "m" is pressed, move the right paddle down
    if pressed_m:
        if right_paddle_y < 320:
            right_paddle_y += PADDLE_SPEED

# draw the ball
def draw_ball():
    set_fill_color(0, 0, 1)   # set fill color to yellow
    draw_circle(ball_center_x, ball_center_y, ball_radius)

# function that moves that ball if it's called
def move_ball():
    global ball_center_x, ball_center_y
    if pressed_space:                   # ball movement is initiated through the pressing of space bar
        ball_center_x += x_SPEED
        ball_center_y += y_SPEED

# function for stopping the game and rending the ball motionless.
def game_stops():
    global x_SPEED, y_SPEED
    y_SPEED = 0
    x_SPEED = 0
    enable_stroke()
    set_stroke_color(0, 0, 0)
    draw_text("GAME OVER", 150, 200)

# function to instruct the ball to bounce when it hits the horizontal (top and bottom) walls.
def contact_horizontal_wall():
    global y_SPEED
    if ball_center_y - ball_radius < 0:
        y_SPEED = - y_SPEED
    if ball_center_y + ball_radius > 400:
        y_SPEED = - y_SPEED

# function to instruct the ball to bounce when it hits the vertical (left and right) walls.
def contact_vertical_wall():
    global x_SPEED
    if ball_center_x - ball_radius < 0:
        game_stops()
    if ball_center_x + ball_radius > 400:
        game_stops()

# In the situation where the ball hits the paddle and not the vertical wall. The game continues.
def contact_paddle():
    global x_SPEED

    if ball_center_x - ball_radius < PADDLE_WIDTH:
        if (ball_center_y > left_paddle_y) and (ball_center_y < left_paddle_y + PADDLE_LENGTH):
            x_SPEED = - x_SPEED
    if ball_center_x + ball_radius > 400 - PADDLE_WIDTH:
        if (ball_center_y > right_paddle_y) and (ball_center_y < right_paddle_y + PADDLE_LENGTH):
            x_SPEED = - x_SPEED

# function to quit the game and close the window.
def quit_game():
    if pressed_q:
        cs1_quit()

# function set up for the purpose of being called by start_graphics
def play_game():

    clear()
    # draw the yellow background
    set_fill_color(1, .8, 0)
    draw_rectangle(0, 0, 400, 400)
    #  draw the paddles
    draw_paddles()

    #  move the paddles
    move_paddles()

    #   draw the ball
    draw_ball()

    #   move the ball
    move_ball()

    #   contact vertical wall
    contact_vertical_wall()

    #   contact horizontal wall
    contact_horizontal_wall()

    #   contact horizontal wall
    contact_paddle()

    #   contact horizontal wall
    quit_game()

start_graphics(play_game, title = "Pong", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate = 50, key_press=key_down, key_release=key_up)

