import pygame
import numpy as np

width=10
height=10
margin=3
dims=[50,50]
print('dims1:' ,dims[1])
size = (dims[1]*(width+margin)+margin, dims[0]*(height+margin)+margin)


def find_frontier(x,y):
    f=set()
    if x>= 1:
        f.add((x-1,y))
    if x < width -1:
        f.add(x+1,y)
    if y>1 :
        f.add(x,y-1)
    if y<height-1:
        f.add(x,y+1)
    return f

def find_neighbourgs(x,y):
    n=set()
    if x>= 1:
        n.add((x-1,y))
    if x < width -1:
        n.add(x+1,y)
    if y>1 :
        n.add(x,y-1)
    if y<height-1:
        n.add(x,y+1)
    return n


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()



screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
#grid=[[1 for x in range(10)]for y in range(10)]

grid=np.zeros((dims[0],dims[1]))
start_x=np.random.randint(grid.shape[0])
start_y=np.random.randint(grid.shape[1])
grid[start_x][start_y]=2



done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            gridpos_x=x//(width+margin)#
            gridpos_y=y//(height+margin)
            grid[gridpos_y][gridpos_x]=1




    recolor=WHITE
    screen.fill(BLACK)
    for row in range(dims[0]):
        for column in range(dims[1]):
            recolor=WHITE
            if grid[row][column]!=0:
                recolor=GREEN
            pygame.draw.rect(screen, recolor, (margin+column*(width+margin), margin+row*(height+margin), width, height))
    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

