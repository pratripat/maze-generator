import pygame, sys
from grid import Grid

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Maze Generator')

rows = cols = 40
res = screen.get_height()//rows

def main():
    grid = Grid(rows, cols, res)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((211,211,211))
        grid.update()
        grid.render(screen)
        pygame.display.update()

main()
