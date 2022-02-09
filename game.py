import pygame
from Team import *

HEIGHT, WIDTH = 600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

team1 = [Soldier.mock_soldier()]


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
