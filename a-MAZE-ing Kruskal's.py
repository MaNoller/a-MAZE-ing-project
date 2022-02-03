import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [50,50]
# print('dims1:' ,dims[1])
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption("My Game")
# grid=[[1 for x in range(10)]for y in range(10)]

grid = np.zeros((dims[0], dims[1]))
start_x = np.random.randint(grid.shape[0])
start_y = np.random.randint(grid.shape[1])
grid[start_x][start_y] = 1


def debuild_walls(x,y,nx,ny):
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, GREEN,
                             (margin + nx * (width + margin), margin + y * (height + margin), 2 * width + margin,
                              height))
        else:
            pygame.draw.rect(screen, GREEN,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), 2 * width + margin, height))

    else:
        if y > ny:
            pygame.draw.rect(screen, GREEN,
                             (margin + x * (width + margin), margin + ny * (height + margin), width,
                              2 * height + margin))
        else:
            pygame.draw.rect(screen, GREEN,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), width, 2 * height + margin))


recolor = WHITE

for row in range(dims[0]):
    for column in range(dims[1]):
        recolor = WHITE
        if grid[column][row] != 0:
            if grid[column][row] == 1:
                recolor = GREEN
            elif grid[column][row] == 2:
                recolor = RED
            else:
                recolor = BLUE
        pygame.draw.rect(screen, recolor,
                         (margin + column * (width + margin), margin + row * (height + margin), width, height))

pygame.display.flip()



done = False

clock = pygame.time.Clock()




walls1 = []
for x in range(dims[0] - 1):
    for y in range(dims[1]):
        walls1 += [(x, y, x + 1, y)]
walls2 = []
for x in range(dims[0]):
    for y in range(dims[1] - 1):
        walls2 += [(x, y, x, y + 1)]

walls = walls1 + walls2
random.shuffle(walls)
walls2 = walls
cell_set_list = []
for x in range(dims[0]):
    for y in range(dims[1]):
        cell_set_list += [set([(x, y)])]

for wall in walls2:
    s1 = None
    s2 = None
    c1 = wall[:2]
    c2 = wall[2:]
    for set in cell_set_list:
        if c1 in set:
            s1 = set
        if c2 in set:
            s2 = set

    if s1 != s2:
        cell_set_list.remove(s1)
        cell_set_list.remove(s2)
        cell_set_list.append(s1.union(s2))
        debuild_walls(c1[0],c1[1],c2[0],c2[1])
        pygame.display.flip()


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Go ahead and update the screen with what we've drawn.


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
