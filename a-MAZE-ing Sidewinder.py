import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [10,10]
# print('dims1:' ,dims[1])
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)



def debuild_walls(x,y,nx,ny):
    #print(x,y,nx,ny)
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, GREEN,
                             (margin + nx * (width + margin), margin + y * (height + margin), 2 * width + margin,
                              height))
        else:
            #print('aaa', x,width,margin)
            pygame.draw.rect(screen, GREEN,
                             (margin + x * (width + margin), margin + y * (height + margin), 2 * width + margin, height))

    else:
        print(x,y,nx,ny)
        if y > ny:
            print('joo')
            pygame.draw.rect(screen, GREEN,
                             (margin + x * (width + margin), margin + ny * (height + margin), width,
                              2 * height + margin))
        else:
            pygame.draw.rect(screen, GREEN,
                             (margin + x * (width + margin), margin + y * (height + margin), width, 2 * height + margin))




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

done = False

clock = pygame.time.Clock()

dir=[0,1]#0 is west, 1 is north
for el in range(dims[1]-1):
    debuild_walls(el+1,0,el,0)
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
            pygame.display.flip()
            pass
        elif column<dims[1]:
            debuild_walls(column+1,row,column,row)
            pygame.display.flip()








while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    clock.tick(60)


pygame.quit()
