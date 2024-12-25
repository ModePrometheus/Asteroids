import pygame
from constants import *
from player import Player


def main():
    # initialization before game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_limit = pygame.time.Clock()
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    #--------
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        # limit framerate to 60 fps
        dt = frame_limit.tick(60) / 1000
        


if __name__ == "__main__":
    main()
