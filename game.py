import pygame
from Soldier import Soldier
from Weapon import *
from Item import *

HEIGHT, WIDTH = 600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
sniper = Sniper()
ammo_pack = AmmoPack()
default_inv = {ammo_pack.name: (1, ammo_pack.weight)}
team1 = [Soldier()]

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
