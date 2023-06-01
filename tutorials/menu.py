import pygame
import buttons_class

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Menu Demo")

fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 24)

menu_page = False


def draw_menu():
    menu_button1 = buttons_class.Button(400, 100, "Button 1", True)
    menu_button2 = buttons_class.Button(400, 200, "Button 2", True)
    menu_button3 = buttons_class.Button(400, 300, "Button 3", True)
    menu_back = buttons_class.Button(400, 400, "Back", True)
    if menu_back.check_click():
        return False
    return True


def draw_main():
    the_menu_button = buttons_class.Button(400, 300, "Menu", True)
    if the_menu_button.check_click():
        return True
    return False


running = True
while running:
    window.fill('light blue')
    timer.tick(fps)

    if menu_page:
        menu_page = draw_menu()
    else:
        menu_page = draw_main()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
