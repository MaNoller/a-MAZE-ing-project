import Generators
import test
import pygame
import numpy as np
import random
import time


Generators.init(5,5)
Generators.Wilsons()



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
