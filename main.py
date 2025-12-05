import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    # initialize screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # initialize player object
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    # runing checks, prints version, screen size
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # new clock
    clock = pygame.time.Clock()
    dt = 0

    # game loop, runs forever right now
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = (clock.tick(60))/1000
        # print(dt)
    
    


if __name__ == "__main__":
    main()
