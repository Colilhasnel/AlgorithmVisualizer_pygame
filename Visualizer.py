import pygame
import random
import buttons_class
import display_algorithms

pygame.init()


class global_information:
    fps = 120
    window_height = 550
    window_width = 1000
    state = "Pause"
    sorted = False
    margins = 5*window_width/100
    selection = "Merge Sort"
    screen = "Main"
    algorithm = None  # selected algorithm function
    algorithm_object = None  # generator object

    def __init__(self, data_len):
        self.window = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Algorithm Visualizer")
        self.timer = pygame.time.Clock()
        self.font1 = pygame.font.Font('freesansbold.ttf', 18)
        self.data_size = data_len
        self.generate_list()

    def generate_list(self):
        self.data_array = random.sample(range(1, 450), self.data_size)
        self.max_height = max(self.data_array)
        self.bar_width = (self.window_width - 2*self.margins) / \
            (2*len(self.data_array)-1)
        self.bar_gap = self.bar_width
        for i, num in enumerate(self.data_array):
            self.data_array[i] = [num, 'white']
        self.sorted = False

    def draw_data(self, j=None):
        if (j == None):
            for index, element in enumerate(self.data_array):
                x = self.margins + index * \
                    (self.bar_width + self.bar_gap)
                y = self.window_height - self.margins - element[0]
                rect = pygame.Rect(x, y, self.bar_width, element[0])
                pygame.draw.rect(self.window, element[1], rect)
        else:
            index = j
            element = self.data_array[j]
            x = self.margins + index * \
                (self.bar_width + self.bar_gap)
            # y = self.window_height - self.margins - 450
            # rect = pygame.Rect(x,y,self.bar_width, 450)
            # pygame.draw.rect(self.window, 'black', rect)
            y = self.window_height - self.margins - element[0]
            rect = pygame.Rect(x, y, self.bar_width, element[0])
            pygame.draw.rect(self.window, element[1], rect)
        pygame.display.update()

    def random_gen(self,x,y):
        return random.randrange(x,y)


class Select_Algorithm:
    def __init__(self, global_info, number, text):
        self.select_button = buttons_class.Button(
            global_info, 0, number*36, text, False, True)
        self.select_button.width = 200
        self.select_button.height = 36
        self.select_button.margin = 10
        self.select_button.button_rect = pygame.Rect(
            self.select_button.x_pos, self.select_button.y_pos, self.select_button.width, self.select_button.height)
        self.select_button.Draw(global_info)

    def check_click(self):
        return self.select_button.check_click()


def main_screen(global_info):
    menu_button = buttons_class.Button(global_info, 0, 1, "", False, True)
    menu_button.button_rect = pygame.Rect(0, 1, 130, 34)

    pygame.draw.rect(global_info.window, 'white',
                     menu_button.button_rect, 2, 3)
    pygame.draw.rect(global_info.window, 'white', pygame.Rect(
        5, 10, 30, 4), border_radius=3)
    pygame.draw.rect(global_info.window, 'white', pygame.Rect(
        5, 16, 30, 4), border_radius=3)
    pygame.draw.rect(global_info.window, 'white', pygame.Rect(
        5, 22, 30, 4), border_radius=3)
    heading = global_info.font1.render("Menu", True, 'white')
    global_info.window.blit(heading, (47, 9))

    pygame.draw.rect(global_info.window, 'white',
                     pygame.Rect(132, 1, 868, 34), 2, 10)
    heading2 = global_info.font1.render(
        "Selected Algorithm : " + global_info.selection, True, 'white')
    global_info.window.blit(heading2, (370, 9))

    play_button = buttons_class.Button(
        global_info, 410, 550, "Play", True, True)
    pause_button = buttons_class.Button(
        global_info, 457, 550, "Pause", True, True)
    reset_button = buttons_class.Button(
        global_info, 520, 550, "Reset", True, True)

    if play_button.check_click():
        global_info.state = "Play"
    if pause_button.check_click():
        global_info.state = "Pause"
    if reset_button.check_click():
        global_info.state = "Reset"

    if menu_button.check_click():
        global_info.screen = "Menu"


def menu_screen(global_info):
    menu_button = buttons_class.Button(global_info, 158, 1, "", False, True)
    menu_button.button_rect = pygame.Rect(158, 1, 41, 34)
    pygame.draw.rect(global_info.window, 'white',
                     menu_button.button_rect, 2, 3)
    pygame.draw.line(global_info.window, 'white', (166, 9), (190, 27), 3)
    pygame.draw.line(global_info.window, 'white', (190, 9), (166, 27), 3)
    pygame.draw.rect(global_info.window, 'white',
                     pygame.Rect(0, 1, 199, 34), 2, 3)
    heading = global_info.font1.render("Select Algorithm", True, 'white')
    global_info.window.blit(heading, (4, 9))
    bubble_sort_button = Select_Algorithm(global_info, 1, "Bubble Sort")
    insertion_sort_button = Select_Algorithm(global_info, 2, "Insertion Sort")
    merge_sort_button = Select_Algorithm(global_info, 3, "Merge Sort")
    quick_sort_button = Select_Algorithm(global_info, 4, "Quick Sort")

    pygame.draw.rect(global_info.window, 'white',
                     pygame.Rect(201, 1, 799, 34), 2, 10)
    heading2 = global_info.font1.render(
        "Selected Algorithm : In progess", True, 'white')
    global_info.window.blit(heading2, (450, 9))

    if menu_button.check_click():
        global_info.screen = "Main"
    elif bubble_sort_button.check_click():
        global_info.screen = "Main"
        global_info.selection = "Bubble Sort"
        global_info.algorithm = display_algorithms.bubble_sort
        global_info.state = "Reset"
    elif insertion_sort_button.check_click():
        global_info.screen = "Main"
        global_info.selection = "Insertion Sort"
        global_info.state = "Reset"
        global_info.algorithm = display_algorithms.insertion_sort
    elif merge_sort_button.check_click():
        global_info.screen = "Main"
        global_info.selection = "Merge Sort"
        global_info.algorithm = display_algorithms.merge_sort
        global_info.state = "Reset"
    elif quick_sort_button.check_click():
        global_info.screen = "Main"
        global_info.selection = "Quick Sort"
        global_info.algorithm = display_algorithms.quick_sort
        global_info.state = "Reset"


def main():

    global_info = global_information(449)
    running = True
    global_info.algorithm = display_algorithms.merge_sort
    global_info.algorithm_object = global_info.algorithm(global_info)
    while running:
        global_info.window.fill('black')
        global_info.timer.tick(global_info.fps)

        if global_info.screen == "Menu":
            menu_screen(global_info)
        elif global_info.screen == "Main":
            main_screen(global_info)
            global_info.draw_data()
            if global_info.state == "Reset":
                global_info.generate_list()
                global_info.algorithm_object = global_info.algorithm(
                    global_info)
                global_info.state = "Pause"
            if global_info.state == "Play" and not global_info.sorted:
                next(global_info.algorithm_object)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
