# ClickDots.py by Louisa
import pygame
pygame.init()
screen = pygame.display.set_mode([1200,1000])
pygame.display.set_caption("Click and drag to draw")
keep_going = True
PINK = (255,192,203)
radius = 15
mousedown = False
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, PINK, spot, radius)
    pygame.display.update()

pygame.quit()

