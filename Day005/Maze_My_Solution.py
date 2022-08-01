while not at_goal():
    if right_is_clear():
       turn_right()
    if wall_in_front():
       turn_left()
    #else:
    #   jump1()
    else:
        move()