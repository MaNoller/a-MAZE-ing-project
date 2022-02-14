import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [4,4]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)

WallGrid=np.full([dims[0], dims[1]],'', dtype=object)


def draw_dirs(x,y,nx,ny):

    if x!=nx:
        if x>nx:
            WallGrid[x][y]+=('U')
            WallGrid[nx][y]+=('D')
        else:
            WallGrid[x][y]+=('D')
            WallGrid[nx][y]+=('U')

    else:
        if y<ny:
            WallGrid[x][y]+=('R')
            WallGrid[x][ny]+=('L')
        else:
            WallGrid[x][y]+=('L')
            WallGrid[x][ny]+=('R')
    print(WallGrid)


def find_neighbours(data):
    x, y = tuple(data)
    n = set()
    if x >= 1 and grid[x - 1][y] == 0:
        n.add((x - 1, y))
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        n.add((x + 1, y))
    if y >= 1 and grid[x][y - 1] == 0:
        n.add((x, y - 1))
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        n.add((x, y + 1))
    return n

def debuild_walls(x,y,nx,ny): #nx=row, ny=column
    #print(x,y,nx,ny)
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, GREEN,
                             ( margin + y * (width + margin), margin + nx * (height + margin),width,
                              2*height+margin))
        else:
            pygame.draw.rect(screen, GREEN,
                             (margin + y * (width + margin),margin + x * (height + margin),   width,
                              2*height+margin))

    else:
        if y > ny:
            pygame.draw.rect(screen, GREEN,
                             ( margin + ny * (width + margin),margin + x * (height + margin), 2*width+margin,
                              height))
        else:
            pygame.draw.rect(screen, GREEN,
                             (margin + y * (width + margin),margin + x * (height + margin),  2*width+margin,
                              height))


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



Queue = []
grid = np.zeros((dims[0], dims[1]))
nx = np.random.randint(grid.shape[0])
ny = np.random.randint(grid.shape[1])
grid[nx][ny] = 1
Queue.append((nx, ny))
while Queue:
    time.sleep(0.005)
    nb_s = find_neighbours(Queue[-1])
    nx,ny=tuple(Queue[-1])
    if nb_s:
        x,y = random.choice(tuple(nb_s))
        Queue.append((x,y))
        grid[x][y] = 1
        debuild_walls(x,y,nx,ny)
        draw_dirs(x, y, nx, ny)
    else:
        Queue.pop()

    #nx,ny=x,y  #das hier muss es sein.. b
    pygame.display.flip()

recolor = WHITE

for row in range(dims[0]):
    for column in range(dims[1]):
        recolor = WHITE
        if grid[row][column] != 0:
            if grid[row][column]== 1:
                recolor = GREEN
            elif grid[row][column]== 2:
                recolor = RED
            else:
                recolor = BLUE
        pygame.draw.rect(screen, recolor,
                         (margin + column * (width + margin), margin + row * (height + margin), width, height))


pygame.display.flip()

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
