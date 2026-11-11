#%% Functions and Variables

# grid Boundries
x_min = 0
x_max = 10
x_len = x_max - x_min + 1

y_min = 0
y_max = 10
y_len = y_max - y_min + 1


# Obsticals and Destination
obstacle_list = [[4, 6], [2, 3], [8, 1]]
destination = [10,10]

position = [0,0]

#%% Functions

# Plotting Function
def plot_grid(shown_position):
    for column in range(y_len):
        for row in range(x_len):
            if row == shown_position[0] and column == shown_position[1]:
                print("R", end=" ")
            elif any(coord == [row, column] for coord in obstacle_list):
                print("O", end=" ")
            elif [row, column] == destination:
                print("D", end=" ")
            else:
                print(".", end=" ")
            
        print()


# Movement Function
def movement_func(position, m, n):
    if isinstance(position, list) and len(position) == 2:
        if isinstance(position[0], int) and isinstance(position[1], int):
            if isinstance(m, int) and isinstance(n, int):
                if y_min <= position[0] + m <= y_max and x_min <= position[1] + n <= x_max:  
                    if any(coord == [position[0] + m, position[1] + n] for coord in obstacle_list):
                        print("Robot would hit obsical. Try Again")
                        print("position is still: ", position)
                        return position, False
                    else:
                        position[0] += m
                        position[1] += n
                        if position == destination:
                            return position, True
                        else:
                            print("new position is: ", position)
                            return position, True
                else:
                    print("robot would be out of boundaries, Try again")
                    print("position is still: ", position)
                    return position, False
            else:
                print("add correct numerical values for movement, Try again")
                print("position is still: ", position)
                return position, False
        else:
            print("input valid position, Try again")
            print("position is still: ", position)
            return position, False
    else:
        print("add the correct amount of numerical values for position, Try again")
        print("position is still: ", position)
        return position, False


# Robot Movement and Grid Update
def move_rob(m, n):
    new_position, state = movement_func(position, m, n)
    if state == True:
        if new_position == destination:
            print("WOOOOOOOO, Well done. You reached the destination")
        else:
            return 


# User Input Function
def get_user_inputs():
    direction = ""
    plot_grid(position)
    print("Awaiting Input, press either(w,a,s,d,q)")
    while direction != "q":
        direction = input("which direction? ")
        if direction == "q":
            break
        elif direction not in ("a","w","s","d"):
            print("Input Invalid")
        else:
            if direction == "w":
                move_rob(0,-1)
                if position == destination:
                    return
                else: plot_grid(position)
            elif direction == "a":
                move_rob(-1,0)
                if position == destination:
                    return
                else: 
                    plot_grid(position)
            elif direction == "s":
                move_rob(0,1)
                if position == destination:
                    return
                else:
                    plot_grid(position)
            elif direction == "d":
                move_rob(1,0)
                if position == destination:
                    return
                else:
                    plot_grid(position)
    print("Program Stopped")

# %% 

get_user_inputs()

#%% Testing


# movement testing
assert movement_func([5,5], 2, 1) == ([7, 6], True)
assert movement_func([7, 6], -3, 2) == ([4, 8], True)
assert movement_func([4, 8], 7, 0) == ([4, 8], False)
assert movement_func([4, 8], 0, -8) == ([4, 0], True)

print("All movement tests passed!")

# Obstical and Movement Testing
obstacle_list = [[4, 6], [2, 3], [8, 1]]
assert movement_func([5, 5], 2, 1) == ([7, 6], True)
assert movement_func([0, 0], 4, 6) == ([0, 0], False)
assert movement_func([7, 2], -5, 1) == ([7, 2], False)

print("All Obsticles tests passed!")

# Boundary Testing

x_min = 0
x_max = 10
y_min = 0
y_max = 10
assert movement_func([9, 5], 1, 5) == ([10, 10], True)
assert movement_func([3, 6], -12, 3) == ([3, 6], False)
assert movement_func([7, 2], 1, 404) == ([7, 2], False)

print("All Boundaries tests passed!")

    
# %%
