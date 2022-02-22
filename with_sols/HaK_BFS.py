import pygame
import numpy as np
import random
import time




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREEN_C = (0, 255, 255)
GREEN_F = (0, 255, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

width = 10
height = 10
margin = 3
dims = [10,10]
start_cell=(0,0)
end_cell=(dims[0],dims[1])
#print('s is', start_cell, end_cell)
frontier=[]
explored=[]
frontier.append(start_cell)
explored.append(start_cell)
while frontier:
    current=frontier.pop(0)
    if current==end_cell:
        break




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
    #print(WallGrid)

def find_way(cell):
    way=[]
    while True:
        way.append(cell)
        cell=mapping[cell]
        if cell==start_cell:
            way.append(start_cell)
            break
    return way

def draw_sol(x,y,nx,ny): #nx=row, ny=column
    #print(x,y,nx,ny)
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, RED,
                             ( margin + y * (width + margin), margin + nx * (height + margin),width,
                              2*height+margin))
        else:
            pygame.draw.rect(screen, RED,
                             (margin + y * (width + margin),margin + x * (height + margin),   width,
                              2*height+margin))

    else:
        if y > ny:
            pygame.draw.rect(screen, RED,
                             ( margin + ny * (width + margin),margin + x * (height + margin), 2*width+margin,
                              height))
        else:
            pygame.draw.rect(screen, RED,
                             (margin + y * (width + margin),margin + x * (height + margin),  2*width+margin,
                              height))





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

def find_frontier(x, y):
    f = set()
    if x >= 1 and grid[x - 1][y] == 0:
        f.add((x - 1, y))
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        f.add((x + 1, y))
    if y >= 1 and grid[x][y - 1] == 0:
        f.add((x, y - 1))
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        f.add((x, y + 1))
    return f

def find_hunt():
    #print('angang')
    for row in range(dims[0]):
        for column in range(dims[1]):
            if grid[row][column]==0:
                nb_set= find_neighbours(row,column)
                if nb_set:
                    nx, ny = random.choice(tuple(nb_set))
                    x,y=row,column
                    return x,y,nx,ny

def draw_path(x,y):
    pygame.draw.rect(screen, RED,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()
def draw_current(x,y):
    pygame.draw.rect(screen, GREEN_C,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()
def draw_frontier(x,y):
    pygame.draw.rect(screen, BLUE,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()

grid = np.zeros((dims[0], dims[1]))
start_x = np.random.randint(grid.shape[0])
start_y = np.random.randint(grid.shape[1])
grid[start_x][start_y] = 1
last_cell=(start_x,start_y)
fr = find_frontier(start_x, start_y)


pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption("My Game")
# grid=[[1 for x in range(10)]for y in range(10)]


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


hunt=True
while hunt:
    time.sleep(0.01)
    try:
        nx,ny=x,y
        #print(fr)
        x,y=random.choice(tuple(fr))
        grid[x][y]=1
        debuild_walls(x, y, nx, ny)
        draw_dirs(x, y, nx,ny)
        pygame.display.flip()
        fr=find_frontier(x,y)
    except:
        out=find_hunt()
        if not out:
            break
        else:
            x,y,nx,ny=out
            debuild_walls(x, y, nx, ny)
            draw_dirs(x, y, nx,ny)
            pygame.display.flip()
            grid[x][y]=1
            fr = find_frontier(x, y)


start_cell=(0,0)
end_cell=(dims[0]-1,dims[1]-1)
frontier=[]
explored=[]
frontier.append(start_cell)
explored.append(start_cell)
mapping={}
while frontier:
    time.sleep(0.1)
    current=frontier.pop(0)
    cx,cy=current
    draw_current(cx,cy)

    if current==end_cell:
        way=find_way(end_cell)
        break
    for el in WallGrid[cx][cy]:
        time.sleep(0.05)
        if el=='D':
            next_cell=(cx+1,cy)
        if el== 'U':
            next_cell=(cx-1,cy)
        if el=='R':
            next_cell=(cx,cy+1)
        if el=='L':
            next_cell=(cx,cy-1)
        if next_cell not in explored:
            frontier.append(next_cell)
            fx,fy=next_cell
            draw_frontier(fx,fy)
            explored.append(next_cell)
            mapping[next_cell] = (cx, cy)



for id, el in enumerate(way[:-1]):
    time.sleep(0.01)
    x,y=el
    nx,ny=way[id+1]
    draw_sol(x,y,nx,ny)
    pygame.display.flip()


done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    clock.tick(60)

# Close the window and quit.
pygame.quit()
