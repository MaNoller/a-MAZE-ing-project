import pygame
import numpy as np
import random
import time

width = 10
height = 10
margin = 3
dims = [50, 50]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)

class Node:
    def __init__(self,data):
        self.left=None
        self.middle=None
        self.right=None
        self.value=data
        self.a, self.b = data
        grid[self.a][self.b]=1

    def find_neighbour(self):
        print(self.a,self.b)


#grid position is the data of node

#find set of unvisited neighbours

#choose random neighbour

#visit neighbour

#at end go back to last node with unvisited neighbours







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

root=Node((start_x,start_y))
root.find_neighbour()


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
