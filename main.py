import pygame
from os.path import join
from random import randint
from constants import *
from player import *

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
    
    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)

    # importing an image
    # player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
    # player_rect = player_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    # player_direction = pygame.math.Vector2()
    
    stars_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
    star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(40)]
    
    meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT /2))
    
    laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
    laser_rect = laser_surface.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))                                 
            
    while running:
        dt = clock.tick() / 1000
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # input
        # keys = pygame.key.get_pressed()
        # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        # player_direction = player_direction.normalize() if player_direction else player_direction
        # player_rect.center += player_direction * PLAYER_SPEED * dt
        
        # laser
        # recent_keys = pygame.key.get_just_pressed()
        # if recent_keys[pygame.K_SPACE]:
        #     print('fired laser')
            
        all_sprites.update()
 
        # draw the game
        display_surface.fill('black')
        for pos in star_positions:
            display_surface.blit(stars_surface, pos)
            
        display_surface.blit(meteor_surface, meteor_rect)
        display_surface.blit(laser_surface, laser_rect)           
        # display_surface.blit(player_surface, player_rect)
        all_sprites.draw(display_surface)
        
        
        pygame.display.flip()



    pygame.quit()
    
if __name__ == "__main__":
    main()