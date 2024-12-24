import pygame
from constants import *


def main():
    # initialization before game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_limit = pygame.time.Clock()
    dt = 0
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        # limit framerate to 60 fps
        dt = frame_limit.tick(60) / 1000
        


if __name__ == "__main__":
    main()
