def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
       turn_right()
    if wall_in_front():
       turn_left()
    #else:
    #   jump1()
    else:
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
