import pygame
from constants import *

def main():
    pygame.init()
   
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.fill("black")
        
        pygame.display.flip()
        
        clock.tick(60)


if __name__ == "__main__":
    main()