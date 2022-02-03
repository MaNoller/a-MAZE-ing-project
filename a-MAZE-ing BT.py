import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [50,50]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def find_frontier(x, y):
    f = set()
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        f.add((x + 1, y))
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        f.add((x, y + 1))
    return f

def debuild_walls(x,y,nx,ny):
    #print(x,y,nx,ny)
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



pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption("My Game")

grid = np.zeros((dims[0], dims[1]))
start_x = np.random.randint(grid.shape[0])
start_y = np.random.randint(grid.shape[1])

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


##################
for row in range(dims[0]):
    for column in range(dims[1]):
        f=find_frontier(column,row)
        if f:
            x,y=random.choice(tuple(f))
            debuild_walls(x,y,column,row)
            pygame.display.flip()

###################


done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            gridpos_x = x // (width + margin)  #
            gridpos_y = y // (height + margin)
            grid[gridpos_x][gridpos_y] = 1


    clock.tick(60)

pygame.quit()
