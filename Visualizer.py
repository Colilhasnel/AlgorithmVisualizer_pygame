import pygame
import buttons_class

pygame.init()

window = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
pygame.display.set_caption("Algorithm Visualizer")

fps = 60
timer = pygame.time.Clock()
font1 = pygame.font.Font('freesansbold.ttf', 18)


def menu(do_open):
    menu_button = pygame.Rect(0, 0, 40, 46)
    pygame.draw.rect(window, 'white', menu_button, 2, 10)
    pygame.draw.rect(window, 'white', pygame.Rect(10, 11, 20, 2), border_radius=1)
    pygame.draw.rect(window, 'white', pygame.Rect(10, 22, 20, 2), border_radius=1)
    pygame.draw.rect(window, 'white', pygame.Rect(10, 33, 20, 2), border_radius=1)

    if do_open:
        pass
    else:
        pass


running = True
while running:
    window.fill('black')
    timer.tick(fps)

    menu(True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
