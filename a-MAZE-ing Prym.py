import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [50, 50]
# print('dims1:' ,dims[1])
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)


# wall=0, Maze=1,frontier=2,neighbour=3

def find_frontier(x, y):
    # print('infindfront:',x,y,grid[x-1][y],grid[x+1][y],grid[x][y-1],grid[x][y+1])
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
    # print('set=',f)
    return f


def find_neighbours(x, y):
    n = set()
    # print('nb',grid[x-1][y],grid[x+1][y],grid[x][y-1],grid[x][y+1])
    if x >= 1 and grid[x - 1][y] == 1:
        n.add((x - 1, y))
        # grid[x - 1][y] =3
    if x < dims[0] - 1 and grid[x + 1][y] == 1:
        n.add((x + 1, y))
        # grid[x + 1][y] =3
    if y >= 1 and grid[x][y - 1] == 1:
        n.add((x, y - 1))
        # grid[x][y - 1] =3
    if y < dims[1] - 1 and grid[x][y + 1] == 1:
        n.add((x, y + 1))
        # grid[x][y + 1] =3
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
        # print('jo', Wall_set)
        x, y = random.choice(tuple(Wall_set))
        Wall_set.remove((x, y))
        grid[x][y] = 1
        # print(grid)
        # print('xy=',x,y)
        nb_set = find_neighbours(x, y)
        # print('nbset',nb_set)
        if nb_set:
            nx, ny = random.choice(tuple(nb_set))
            # print('drin')
            grid[nx][ny] = 1
            debuild_walls(x, y, nx, ny)

        # print('nxny=',nx,ny)
        fr = find_frontier(x, y)
        # print('a',fr)
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
# grid=[[1 for x in range(10)]for y in range(10)]

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
    # Wall_Set=set()
    # Start_Frontier=find_frontier(start_x,start_y)
    '''
    for el in Start_Frontier:
        Wall_Set.add(el)
    while Wall_Set:
        x,y=random.choice(tuple(Wall_Set))
        Wall_Set.remove((x,y))
        nb_set= find_neighbours(x,y)

    '''


    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
