import pygame
from os.path import join
from random import randint
from constants import *


# general setup
def main():
    pygame.init()
   
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Spaceship shooter")
    clock = pygame.time.Clock()
    running = True
    
    # plain surface
    surf = pygame.Surface((100, 200))
    surf.fill('grey')
    x = 100
    
    # importing an image
    player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
    stars_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
            
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw the game
        display_surface.fill('black')
        for pos in star_positions:
            display_surface.blit(stars_surface, pos)
        x += 1.2
        display_surface.blit(player_surface, (x, 460))
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()