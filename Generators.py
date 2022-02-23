import pygame
import numpy as np
import random
import time

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


def find_frontier_bt(x, y):
    f = set()
    if x < dims[0] - 1 and grid[x + 1][y] == 0:
        f.add((x + 1, y))
    if y < dims[1] - 1 and grid[x][y + 1] == 0:
        f.add((x, y + 1))
    return f


def init_pygame():
    global screen,grid,start_x,start_y
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    pygame.display.set_caption("My Game")
    grid = np.zeros((dims[0], dims[1]))
    start_x = np.random.randint(grid.shape[0])
    start_y = np.random.randint(grid.shape[1])
    grid[start_x][start_y] = 1
    global WallGrid
    WallGrid = np.full([dims[0], dims[1]], '', dtype=object)


def init_colors():
    global BLACK,WHITE,GREEN,RED,BLUE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

def build_grid(dims):
    for row in range(dims[0]):
        for column in range(dims[1]):
            recolor = WHITE
            pygame.draw.rect(screen, recolor,
                             (margin + column * (width + margin), margin + row * (height + margin), width, height))
    pygame.display.flip()

def debuild_walls(x,y,nx,ny): #nx=row, ny=column
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

def find_frontier_prym(x, y):
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


def init(rows,columns):
    global dims,size,width,height,margin
    width = 10
    height = 10
    margin = 3
    dims = [rows,columns]  # 6 rows, 4 columns
    size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)
    init_colors()
    init_pygame()
    build_grid(dims)



def Binary_Tree():
    time.sleep(1)
    for row in range(dims[0]):
        for column in range(dims[1]):
            f=find_frontier_bt(row,column)
            if f:
                x,y=random.choice(tuple(f))
                debuild_walls(x,y,row,column)
                pygame.display.flip()
                draw_dirs(x, y, row, column)

def HaK():
    hunt=True
    grid[start_x][start_y] = 1
    fr = find_frontier(start_x, start_y)
    while hunt:
        time.sleep(0.01)
        try:
            nx,ny=x,y
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


def Kruskal():
    walls1 = []
    for x in range(dims[0] - 1):
        for y in range(dims[1]):
            walls1 += [(x, y, x + 1, y)]
    walls2 = []
    for x in range(dims[0]):
        for y in range(dims[1] - 1):
            walls2 += [(x, y, x, y + 1)]

    walls = walls1 + walls2
    random.shuffle(walls)
    walls2 = walls
    cell_set_list = []
    for x in range(dims[0]):
        for y in range(dims[1]):
            cell_set_list += [{(x, y)}]

    for wall in walls2:
        s1 = None
        s2 = None
        c1 = wall[:2]
        c2 = wall[2:]
        for set in cell_set_list:
            if c1 in set:
                s1 = set
            if c2 in set:
                s2 = set

        if s1 != s2:
            cell_set_list.remove(s1)
            cell_set_list.remove(s2)
            cell_set_list.append(s1.union(s2))
            debuild_walls(c1[0],c1[1],c2[0],c2[1])
            pygame.display.flip()
            draw_dirs(c1[0],c1[1],c2[0],c2[1])

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
            draw_dirs(x, y, nx, ny)

        fr = find_frontier(x, y)
        for el in fr:
            Wall_set.add(el)
        pygame.display.flip()



init(10,10)
#Binary_Tree()
#HaK()
#Kruskal()
Prym(start_x,start_y)


done = False
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)

pygame.quit()
