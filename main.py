import pygame
from os.path import join
from random import randint
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()

    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * PLAYER_SPEED * dt
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fired laser')  

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)))        
        
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
    star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
    for i in range(40):
        Star(all_sprites, star_surface)
    player = Player(all_sprites)
    
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
            
        all_sprites.update(dt)
 
        # draw the game
        display_surface.fill('black')                   
        all_sprites.draw(display_surface)
                
        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()