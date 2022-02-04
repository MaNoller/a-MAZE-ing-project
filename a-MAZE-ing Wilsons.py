import numpy as np
import random

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

width = 10
height = 10
margin = 3
dims = [5,5]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)
grid = np.zeros((dims[0], dims[1]))
start_x = np.random.randint(grid.shape[0])
start_y = np.random.randint(grid.shape[1])
grid[start_x][start_y] = 1


#init
path=[]
start_x_w=np.random.randint(grid.shape[0])
start_y_w=np.random.randint(grid.shape[1])
next_cell=(start_y_w,start_y_w)
path.append((start_y_w,start_y_w))
f_s=find_frontier(path[-1][0],path[-1][1])
try:
    f_s.remove(path[-1])  #damit geht es nicht direkt zurück (nice)
except:
    pass
next_cell=random.choice(tuple(f_s))
if next_cell in path:
    path=path[:path.index(next_cell)]






    



