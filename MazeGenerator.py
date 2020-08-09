import pygame
import random
import sys
sys.setrecursionlimit(32000)

width = 701
height = 701
size = (width, height)
squares = 50
speed = 150
boxes = []
current = [(0,0)]
visited = [(0,0)]
w = int(width/squares)
h = int(height/squares)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
RADIUS = int(w/4)
making = True
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Maze generator")
screen = pygame.display.set_mode(size)

class Box:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def box(self):
        #TOP
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x + w, self.y), 1)
        #RIGHT
        pygame.draw.line(screen, WHITE, (self.x + w, self.y), (self.x + w, self.y + w), 1)
        #BOTTOM
        pygame.draw.line(screen, WHITE, (self.x, self.y + w), (self.x + w, self.y + w), 1)
        #LEFT
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + w), 1)

def render_boxes():
    for i in range(squares):
        for j in range(squares):
            box = Box(i*w, j*h)
            box.box()
            boxes.append((i*w, j*h))
    pygame.display.update()

def currentCell(top=False, right=False, bottom=False, left=False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if len(current) != 0:
        cell = current[-1]

        if top:
            pygame.draw.rect(screen, PURPLE, (cell[0]*w+1, cell[1]*h+1, w-1, h))
        elif right:
            pygame.draw.rect(screen, PURPLE, (cell[0]*w, cell[1]*h+1, w, h-1))
        elif bottom:
            pygame.draw.rect(screen, PURPLE, (cell[0]*w+1, cell[1]*h-1, w-1, h+1))
        elif left:
            pygame.draw.rect(screen, PURPLE, (cell[0]*w+1, cell[1]*h+1, w+1, h-1))
        else:
            pygame.draw.rect(screen, PURPLE, (cell[0]*w+1, cell[1]*h+1, w-1, h-1))
        pygame.draw.circle(screen, GREEN, (int(w/2), int(h/2)), RADIUS)
        pygame.display.update()
        clock.tick(speed)

        findNeighbors(cell)
    else:
        pygame.draw.circle(screen, RED, (w*squares - int(w/2), h*squares - int(h/2)), RADIUS)
        pygame.display.update()

def findNeighbors(last):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    x = last[0]
    y = last[1]
    neighbors = []

    top = (x, y-1)
    right = (x+1, y)
    bottom = (x, y+1)
    left = (x-1, y)

    def updateList(value):
        if value[0] >= 0 and value[0] < squares and value[1] >= 0 and value[1] < squares and not value in visited:
            neighbors.append(value)

    updateList(top)
    updateList(right)
    updateList(bottom)
    updateList(left)

    if len(neighbors) != 0:
        rand = random.choice(neighbors)
        current.append(rand)
        visited.append(rand)
        if rand == top:
            currentCell(True)
        elif rand == right:
            currentCell(False, True)
        elif rand == bottom:
            currentCell(False, False, True)
        elif rand == left:
            currentCell(False, False, False, True)

    else:
        current.pop()
        currentCell()

render_boxes()
currentCell()

while making:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
