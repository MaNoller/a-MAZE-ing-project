import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [4,4]
# print('dims1:' ,dims[1])
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
# grid=[[1 for x in range(10)]for y in range(10)]

grid = np.zeros((dims[0], dims[1]))


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

done = False

clock = pygame.time.Clock()

dir=[0,1]#0 is west, 1 is north
for el in range(dims[1]-1):
    debuild_walls(el+1,0,el,0)
    draw_dirs(el+1,0,el,0)
    pygame.display.flip()
for row in range(1,dims[0]):

    run=list()
    for column in range(0,dims[1]):
        #print(row,column)
        run.append((column,row))
        #print(run)
        walk_dir=random.choice(dir)
        if column==dims[1]-1:
            walk_dir=1

        if walk_dir==1:
            #print(row,column)
            cell=random.choice(run)#
            run=list()
            debuild_walls(cell[0],cell[1],cell[0],cell[1]-1)
            draw_dirs(cell[0],cell[1],cell[0],cell[1]-1)
            pygame.display.flip()
            pass
        elif column<dims[1]:
            debuild_walls(column+1,row,column,row)
            draw_dirs(column+1,row,column,row)
            pygame.display.flip()








while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    clock.tick(60)


pygame.quit()
