import pygame
from Team import *

HEIGHT, WIDTH = 600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIBG")
FLOOR = (209, 196, 75)
team0 = Team(0)
team0.members = [Soldier.mock_soldier(0)]


def draw_window():
    WIN.fill(FLOOR)
    rect = pygame.draw.rect(WIN, (255, 0, 0), )
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
