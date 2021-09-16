"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.

"""

from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(0, 0)
pacman = vector(-20, -100)

"""
b = blinky
p = pinky
i = inky
c = clyde
"""
ghosts = [
    [vector(-180, 160), vector(5, 0), 'c'],
    [vector(-180, -180), vector(0, 5), 'c'],
    [vector(140, 160), vector(0, -5), 'b'],
    [vector(140, -180), vector(-5, 0), 'p'],
    [vector(-20, 0), vector(-5, 0), 'i']
]

tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    """
    Draws a square using path at (x, y)
    """
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """
    Return offset of point in tiles.
    """
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """
    Return True if point is valid in tiles.
    """
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """
    Draw world using path.
    """
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """
    Move pacman and all ghosts.
    """
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    # Update pacman on the map!
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course, target, color in get_ghosts():
        if valid(point + course):  # If next step is valid:
            point.move(course)  # Move ghost.
        else:  # Else:
            # Get this ghost valid courses
            valid_courses = valid_new_ghost_courses(point, course)
            # Get this ghost valid next-steps
            valid_points = [point + v_course for v_course in valid_courses]
            # Get euclidean distance to all targets
            distances = [distance(target, v_point) for v_point in valid_points]
            # Gets the course that has the minimum euclidean distance to target
            plan = valid_courses[distances.index(min(distances))]
            course.x = plan.x
            course.y = plan.y
        up()
        # Update ghost on the map!
        goto(point.x + 10, point.y + 10)
        dot(20, color)

    update()

    for point, course, name in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def get_ghosts():
    """
    Returns a list of lists
    Returns [point, course, target, color] for each ghost.
    """

    """
    b = blinky
    p = pinky
    i = inky
    c = clyde
    """
    for point, course, name in ghosts:
        target = vector(0, 0)
        color = "red"
        if name == 'b':
            # Blinky's target is always pacman.
            target = pacman
            color = "red"
        elif name == 'p':
            # Pinky's target is 4 spaces ahead of pacman.
            target = pacman + (4 * aim)
            color = "pink"
        elif name == 'i':
            # Inky's target is the mirror of Bliny on the reference point.
            # Reference point is 2 spaces ahead of pacman.
            reference = pacman + (2 * aim)  # Set reference point 2 spaces ahead of pacman.
            blinky_to_ref = reference - ghosts[2][0]  # Get the vector from blinky to the reference point.
            target = reference + blinky_to_ref  # The mirrored Blinky is the reference + Blinky's vector.
            color = "cyan"
        elif name == 'c':
            # Clyde's target is:
            # pacman if his euclidean distance is <= 8.
            # (0, 0) if his euclidean distance is > 8.
            target = pacman if distance(pacman, course) <= 8 else vector(0, 0)
            color = "orange"
        yield [point, course, target, color]  # yield this ghost.


def distance(v1, v2):
    """
    Returns the euclidean distance between two vectors
    sqrt((x1 - x2)^2 + (y1 - y2)^2)
    """
    return ((v1.x - v2.x)**2 + (v1.y - v2.y)**2)**(1/2)


def valid_new_ghost_courses(point, course):
    """
    Returns all valid courses for a ghost.
    A valid course is one that:
    1. Moves the ghost in one of the 4 valid directions (right, left, up, down)
    2. Is valid for the current board (doesn't produce any collisions with walls)
    3. Is not a 180° turn.
    """
    options = [
        vector(5, 0),
        vector(-5, 0),
        vector(0, 5),
        vector(0, -5),
    ]
    v_options = []
    for option in options:
        if course != -option and valid(point + option):
            v_options.append(option)
    return v_options


def change(x, y):
    """
    Change pacman aim if valid.
    """
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(180, 180)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
