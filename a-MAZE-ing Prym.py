import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [50, 50]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)


# wall=0, Maze=1,frontier=2

def find_frontier(x, y):
    f = set()
    if x >= 1 and grid[x - 1][y] == 0:
        f.add((x - 1, y))
        grid[x - 1][y] = 2
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        f.add((x + 1, y))
        grid[x + 1][y] = 2
    if y >= 1 and grid[x][y - 1] == 0:
        f.add((x, y - 1))
        grid[x][y - 1] = 2
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        f.add((x, y + 1))
        grid[x][y + 1] = 2
    return f


def find_neighbours(x, y):
    n = set()
    if x >= 1 and grid[x - 1][y] == 1:
        n.add((x - 1, y))
    if x < dims[0] - 1 and grid[x + 1][y] == 1:
        n.add((x + 1, y))
    if y >= 1 and grid[x][y - 1] == 1:
        n.add((x, y - 1))
    if y < dims[1] - 1 and grid[x][y + 1] == 1:
        n.add((x, y + 1))
    return n

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


def Prym(start_x,start_y):
    Wall_set = set()
    fr = find_frontier(start_x, start_y)
    for el in fr:
        Wall_set.add(el)
    while Wall_set:
        time.sleep(0.002)
        x, y = random.choice(tuple(Wall_set))
        Wall_set.remove((x, y))
        grid[x][y] = 1
        nb_set = find_neighbours(x, y)
        if nb_set:
            nx, ny = random.choice(tuple(nb_set))
            grid[nx][ny] = 1
            debuild_walls(x, y, nx, ny)

        fr = find_frontier(x, y)
        for el in fr:
            Wall_set.add(el)
        pygame.display.flip()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption("My Game")

grid = np.zeros((dims[0], dims[1]))
start_x = np.random.randint(grid.shape[0])
start_y = np.random.randint(grid.shape[1])
grid[start_x][start_y] = 1


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


Prym(start_x,start_y)
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
            find_frontier(gridpos_x, gridpos_y)
            find_neighbours(gridpos_x, gridpos_y)
    clock.tick(60)

pygame.quit()
