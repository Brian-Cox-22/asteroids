import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    # initialize screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # new clock
    clock = pygame.time.Clock()

    # Makes group vars
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Player.containers = (updatable, drawable)


    # initialize player object
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    # asteroid field object
    asteroid_field = AsteroidField()
    
    # runing checks, prints version, screen size
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    dt = 0

    

    # game loop, runs forever right now
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")
        
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60))/1000
    
    


if __name__ == "__main__":
    main()
