import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [6,4] #6 rows, 4 columns
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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


def find_frontier(x, y):
    f = set()
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        f.add((x + 1, y))
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        f.add((x, y + 1))
    return f

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
        if grid[row][column] != 0:
            if grid[row][column] == 1:
                recolor = GREEN
            elif grid[row][column] == 2:
                recolor = RED
            else:
                recolor = BLUE
        pygame.draw.rect(screen, recolor,
                         (margin + column * (width + margin), margin + row * (height + margin), width, height))


pygame.display.flip()


##################
for row in range(dims[0]):
    for column in range(dims[1]):
        f=find_frontier(row,column)
        if f:
            x,y=random.choice(tuple(f))
            debuild_walls(x,y,row,column)
            pygame.display.flip()
            draw_dirs(x, y, row, column)

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
