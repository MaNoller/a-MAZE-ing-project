import pygame
import numpy as np
import random
import time


def find_frontier(inputarg):
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

width = 10
height = 10
margin = 3
dims = [50,50]
size = (dims[1] * (width + margin) + margin, dims[0] * (height + margin) + margin)


def debuild_walls(x,y,nx,ny):
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, GREEN,
                             (margin + nx * (width + margin), margin + y * (height + margin), 2 * width + margin,
                              height))
        else:
            pygame.draw.rect(screen, GREEN,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), 2 * width + margin, height))

    else:
        if y > ny:
            pygame.draw.rect(screen, GREEN,
                             (margin + x * (width + margin), margin + ny * (height + margin), width,
                              2 * height + margin))
        else:
            pygame.draw.rect(screen, GREEN,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), width, 2 * height + margin))


def debuild_path(x,y,nx,ny):
    if x != nx:
        if x > nx:
            pygame.draw.rect(screen, WHITE,
                             (margin + nx * (width + margin), margin + y * (height + margin), 2 * width + margin,
                              height))
            pygame.draw.rect(screen, BLACK,
                             (margin +width+ nx * (width + margin), margin + y * (height + margin),  margin,
                              height))
        else:
            pygame.draw.rect(screen, WHITE,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), 2 * width + margin, height))
            pygame.draw.rect(screen, BLACK,
                     (margin + width + x * (width + margin), margin + y * (height + margin), margin,
                      height))
    else:
        if y > ny:
            pygame.draw.rect(screen, WHITE,
                             (margin + x * (width + margin), margin + ny * (height + margin), width,
                              2 * height + margin))
            pygame.draw.rect(screen, BLACK,
                             (margin + x * (width + margin), margin +height+ ny * (height + margin), width,
                              margin))

        else:
            pygame.draw.rect(screen, WHITE,
                             (
                             margin + x * (width + margin), margin + y * (height + margin), width, 2 * height + margin))
            pygame.draw.rect(screen, BLACK,
                             (margin + x * (width + margin), margin + height + y * (height + margin), width,
                              margin))




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


unused_cell_list = []
for x in range(dims[0]):
    for y in range(dims[1]):
        unused_cell_list.append((x,y))

unused_cell_list.remove((start_x,start_y))

#init
path=[]


while unused_cell_list:
    #Initiere random Anfang, nachdem path geleert wurde
    next_cell=random.choice(tuple(unused_cell_list))
    path.append((next_cell)) #El in Path einfügen als erstes Element
    ##Loop until ein teil des Mazes erreicht wird
    while True:

        f_s=find_frontier(next_cell) #Finde angrenzende Elemente, die nicht direkt davor besucht wurden
        if path and path[-1] in f_s:
            f_s.remove(path[-1]) #Falls direkt davor besucht, nicht in diese Richtung gehen
        next_cell=random.choice(tuple(f_s)) #Zufällige erlaubte Richtung

        path.append(next_cell)  #
        #print(path)

        if next_cell in path[:-1]:  #Falls die nächste zufällige Zelle bereits im Path liegt:
            deleted_path=path[path.index(next_cell)+1:]
            path=path[:path.index(next_cell)+1] # Den loop entfernen ##sollte jetzt richtig sein
            for id,ce in enumerate(deleted_path[:-1]):
                c1,c2=ce
                cx,cy=deleted_path[id+1]
                #debuild_path(c1,c2, cy,cy)
            pygame.display.flip()



        x,y=next_cell
        #break
        if grid[x][y]==1:   #Falls die neue Zelle Teil des Maze ist:
            #for el,el2 in path[:-1]:
            for idx, cel in enumerate(path[:-1]):
                time.sleep(0.01)
                el,el2=cel
                grid[el][el2]=1  #Els in Path ins Maze setzen
                unused_cell_list.remove((el,el2)) #Els aus der Liate der verfügbaren Startpunkte entfernen
                ###Labyrinth zeichnen wäre noch ne gute Idee
                nx,ny=path[idx + 1]
                debuild_walls(el,el2, nx, ny)


                #debuild_walls(x, y, nx, ny)
                pygame.display.flip()

            path=[]     #Path leeren
            break


        #break
    #unused_cell_list = []


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
