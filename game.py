import pygame
from Soldier import *

HEIGHT, WIDTH = 600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
sniper = Sniper()
ammo_pack = AmmoPack()
test_inv = {ammo_pack.name: 3}
team1 = [Soldier(test_inv, sniper, 1)]


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
