import pygame
import numpy as np
import random
import time


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
    global BLACK,WHITE,GREEN,RED,BLUE,GREEN_C
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN_C = (0, 255, 255)

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
def find_neighbours_rdfs(x,y):
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

def draw_path(x,y):
    pygame.draw.rect(screen, RED,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()
def del_path(x,y):
    pygame.draw.rect(screen, WHITE, (margin + y * (width + margin), margin + x * (height + margin), width, height))
    pygame.display.flip()


def find_frontier_wilsons(inputarg):
    x,y=inputarg
    f = set()
    if x >= 1 :
        f.add((x - 1, y))
    if x < dims[0] - 1 :
        f.add((x + 1, y))
    if y >= 1 :
        f.add((x, y - 1))
    if y < dims[1] - 1:
        f.add((x, y + 1))
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
    time.sleep(0.01)
    for row in range(dims[0]):
        for column in range(dims[1]):
            time.sleep(0.01)
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

def Prym():
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

def rDFS():
    Queue = []
    Queue.append((start_x, start_y))
    while Queue:
        time.sleep(0.005)
        h,i= tuple(Queue[-1])
        nb_s = find_neighbours_rdfs(h,i)
        nx,ny=tuple(Queue[-1])
        if nb_s:
            x,y = random.choice(tuple(nb_s))
            Queue.append((x,y))
            grid[x][y] = 1
            debuild_walls(x,y,nx,ny)
            draw_dirs(x, y, nx, ny)
        else:
            Queue.pop()
        pygame.display.flip()


def Sidewinder():
    dir=[0,1]#0 is west, 1 is north
    for el in range(dims[1]-1):
        debuild_walls(el+1,0,el,0)
        draw_dirs(el+1,0,el,0)
        pygame.display.flip()
    for row in range(1,dims[0]):

        run=list()
        for column in range(0,dims[1]):
            run.append((column,row))
            walk_dir=random.choice(dir)
            if column==dims[1]-1:
                walk_dir=1

            if walk_dir==1:
                cell=random.choice(run)
                run=list()
                debuild_walls(cell[0],cell[1],cell[0],cell[1]-1)
                draw_dirs(cell[0],cell[1],cell[0],cell[1]-1)
                pygame.display.flip()
                pass
            elif column<dims[1]:
                debuild_walls(column+1,row,column,row)
                draw_dirs(column+1,row,column,row)
                pygame.display.flip()


def Wilsons():
    unused_cell_list = []
    for x in range(dims[0]):
        for y in range(dims[1]):
            unused_cell_list.append((x,y))
    for row in range(dims[0]):
        for column in range(dims[1]):
            recolor = WHITE
            if grid[row][column] != 0:
                if grid[row][column] == 1:
                    recolor = GREEN

            pygame.draw.rect(screen, recolor,
                             (margin + column * (width + margin), margin + row * (height + margin), width, height))

    pygame.display.flip()
    unused_cell_list.remove((start_x,start_y))
    path=[]
    while unused_cell_list:
        next_cell=random.choice(tuple(unused_cell_list))
        path.append((next_cell))
        while True:
            f_s=find_frontier_wilsons(next_cell)
            if path and path[-1] in f_s:
                f_s.remove(path[-1])
            next_cell=random.choice(tuple(f_s))
            path.append(next_cell)
            x, y = next_cell
            draw_path(x,y)


            if next_cell in path[:-1]:
                deleted_path=path[path.index(next_cell)+1:]
                path=path[:path.index(next_cell)+1]
                for id,ce in enumerate(deleted_path[:-1]):
                    c1,c2=ce
                    del_path(c1,c2)


            if grid[x][y]==1:
                for idx, cel in enumerate(path[:-1]):
                    time.sleep(0.01)
                    el,el2=cel
                    grid[el][el2]=1
                    unused_cell_list.remove((el,el2))
                    nx,ny=path[idx + 1]
                    debuild_walls(el,el2, nx, ny)
                    draw_dirs(el,el2, nx, ny)
                    pygame.display.flip()

                path=[]
                break

#####
def find_way(cell):
    way=[]
    while True:
        way.append(cell)
        cell=mapping[cell]
        if cell==start_cell:
            way.append(start_cell)
            break
    return way

def draw_current(x,y):
    pygame.draw.rect(screen, GREEN_C,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()
def draw_frontier(x,y):
    pygame.draw.rect(screen, BLUE,(margin + y * (width + margin), margin + x * (height + margin), width , height))
    pygame.display.flip()
#####
def BFS():
    global mapping, way, start_cell, end_cell
    start_cell=(0,0)
    end_cell=(dims[0]-1,dims[1]-1)
    frontier=[]
    explored=[]
    frontier.append(start_cell)
    explored.append(start_cell)
    mapping={}
    while frontier:
        time.sleep(0.01)
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


def DFS():
    global mapping, way,start_cell, end_cell
    start_cell=(0,0)
    end_cell=(dims[0]-1,dims[1]-1)
    frontier=[]
    explored=[]
    frontier.append(start_cell)
    explored.append(start_cell)
    mapping={}
    while frontier:
        time.sleep(0.01)
        current=frontier.pop()
        cx,cy=current
        draw_current(cx, cy)

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
                fx, fy = next_cell
                draw_frontier(fx, fy)
                explored.append(next_cell)
                mapping[next_cell] = (cx, cy)


def weg():
    for id, el in enumerate(way[:-1]):
        time.sleep(0.01)
        x,y=el
        nx,ny=way[id+1]
        draw_sol(x,y,nx,ny)
        pygame.display.flip()




#####


init(10,10)
Binary_Tree()
#HaK()
#Kruskal()
#Prym()
#rDFS()
#Sidewinder()
#Wilsons()
#BFS()
#DFS()
weg()


'''
done = False
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)

pygame.quit()'''
