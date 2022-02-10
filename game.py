import pygame
from Team import *

HEIGHT, WIDTH = 800, 1200
S_HEIGHT, S_WIDTH = 6, 6
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIBG")
FLOOR = (209, 196, 75)
RED = (255, 0, 0)
team0 = Team(0)
team0.members = [Soldier.mock_soldier(0),Soldier.mock_soldier(0),Soldier.mock_soldier(0),Soldier.mock_soldier(0)]
team1 = Team(1)
team1.members = [Soldier.mock_soldier(1),Soldier.mock_soldier(1),Soldier.mock_soldier(1),Soldier.mock_soldier(1)]
teams = [team0, team1]


def draw_soldier(pos: tuple[int, int], color: tuple[int, int, int]):
    aux = pygame.rect.Rect(pos[0] - S_WIDTH/2, pos[1] - S_HEIGHT/2, S_WIDTH, S_HEIGHT)
    pygame.draw.rect(WIN, color, aux)


def draw_team(team: Team):
    for i, soldier in enumerate(team.members):
        print(soldier.pos)
        draw_soldier(soldier.pos, (i * 10 + 50, i * 30, i * 20))


def draw_window():
    WIN.fill(FLOOR)
    for team in teams:
        draw_team(team)
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
