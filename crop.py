import Image
import glob
import os

DOWN = (0, 1)
LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def crop(filename):
    image = Image.open(filename)
    pix = image.load()
    initial_right = find_initial_right(pix, image.size[0], image.size[1])
    point = initial_right
    direction = (0, 1)
    top = right = bottom = left = 0
    while 1:
        next = point_move(point, direction)
        next_colour = pix[next[0], next[1]]
        if next_colour == BLACK:
            point = next
        elif next_colour == WHITE:
            direction = turn_clockwise(direction)
            if direction == LEFT:
                right, bottom = point
            elif direction == RIGHT:
                left, top = point
                break
    image = image.crop((left + 1, top + 1, right, bottom))
    image.save('cropped/' + os.path.basename(filename))

def find_initial_right(pix, width, height):
    x = width - 1
    y = height / 2
    while pix[x, y] == WHITE:
        x -= 1
    return (x, y)

def point_move(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])

def turn_clockwise(direction):
    if direction == DOWN:
        return LEFT
    if direction == LEFT:
        return UP
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN

if __name__ == '__main__':
    filenames = glob.glob('screenshots/*.bmp')
    for filename in filenames:
        crop(filename)
