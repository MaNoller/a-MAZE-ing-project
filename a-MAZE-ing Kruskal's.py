import random
width, height =4, 4

walls1=[]
for x in range(width-1):
    for y in range(height):
        walls1+=[(x,y,x+1,y)]
walls2=[]
for x in range(width):
    for y in range(height-1):
        walls2+=[(x,y,x,y+1)]

walls=walls1+walls2
random.shuffle(walls)
walls2=walls
cell_set_list=[]
for x in range(width):
    for y in range(height):
        cell_set_list+=[set([(x,y)])]


for wall in walls2:
    s1=None
    s2=None
    c1=wall[:2]
    c2=wall[2:]
    for set in cell_set_list:
        if c1 in set:
            s1=set
        if c2 in set:
            s2=set
    
    if s1!=s2:
        cell_set_list.remove(s1)
        cell_set_list.remove(s2)
        cell_set_list.append(s1.union(s2))
        walls2.remove(wall)
    
