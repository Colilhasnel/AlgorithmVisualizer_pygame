import pygame
import buttons_class

pygame.init()

window = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
pygame.display.set_caption("Algorithm Visualizer")

fps = 60
timer = pygame.time.Clock()
font1 = pygame.font.Font('freesansbold.ttf', 18)


class Select_Algorithm:
    def __init__(self, number, text):
        self.select_button = buttons_class.Button(
            0, number*36, text, False, True)
        self.select_button.width = 200
        self.select_button.height = 36
        self.select_button.margin = 10
        self.select_button.button_rect = pygame.Rect(
            self.select_button.x_pos, self.select_button.y_pos, self.select_button.width, self.select_button.height)
        self.select_button.Draw()


def main():
    menu_button = buttons_class.Button(0, 1, "", False, True)
    menu_button.button_rect = pygame.Rect(0, 1, 40, 34)
    pygame.draw.rect(window, 'white', menu_button.button_rect, 2, 10)
    pygame.draw.rect(window, 'white', pygame.Rect(
        5, 10, 30, 4), border_radius=3)
    pygame.draw.rect(window, 'white', pygame.Rect(
        5, 16, 30, 4), border_radius=3)
    pygame.draw.rect(window, 'white', pygame.Rect(
        5, 22, 30, 4), border_radius=3)
    heading = font1.render("Menu", True, 'white')
    window.blit(heading, (47, 9))
    if menu_button.check_click():
        return True
    return False


def menu():
    menu_button = buttons_class.Button(158, 1, "", False, True)
    menu_button.button_rect = pygame.Rect(158, 1, 40, 34)
    pygame.draw.rect(window, 'white', menu_button.button_rect, 2, 10)
    pygame.draw.line(window, 'white', (166, 9), (190,27), 3)
    pygame.draw.line(window, 'white', (190, 9), (166, 27), 3)
    pygame.draw.rect(window, 'white', pygame.Rect(0, 1, 156, 34), 2, 3)
    heading = font1.render("Select Algorithm", True, 'white')
    window.blit(heading, (4, 9))
    bubble_sort_button = Select_Algorithm(1, "Bubble Sort")
    insertion_sort_button = Select_Algorithm(2, "Insertion Sort")
    merge_sort_button = Select_Algorithm(3, "Merge Sort")
    quick_sort_button = Select_Algorithm(4, "Quick Sort")
    if menu_button.check_click():
        return False
    return True


open_menu = False
running = True
while running:
    window.fill('black')
    timer.tick(fps)

    if open_menu:
        open_menu = menu()
    else:
        open_menu = main()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
