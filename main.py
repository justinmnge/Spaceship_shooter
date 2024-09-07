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
    x = 590
    
    # importing an image
    player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
    player_rect = player_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    player_direction = 1
    
    stars_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
    
    meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT /2))
    
    laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
    laser_rect = laser_surface.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))                                  
            
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw the game
        display_surface.fill('black')
        for pos in star_positions:
            display_surface.blit(stars_surface, pos)
            
        display_surface.blit(meteor_surface, meteor_rect)
        display_surface.blit(laser_surface, laser_rect)            
        
        # player movement
        player_rect.x += player_direction * 2
        if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
            player_direction *= -1
        display_surface.blit(player_surface, player_rect)
        
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()