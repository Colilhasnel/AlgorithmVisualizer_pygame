import pygame
import random
import buttons_class
import display_algorithms

pygame.init()

MARGIN_TOP = 20
MARGIN_LEFT = 210
MARGIN_RIGHT = 20


class global_information:
    fps = 120
    window_height = 550
    window_width = 1000
    state = "Pause"
    sorted = False
    selection = "Merge Sort"  # Algorithm text
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
        step = 450//self.data_size
        self.data_array = random.sample(range(1, 450, step), self.data_size)
        self.max_height = max(self.data_array)
        self.bar_width = (self.window_width - MARGIN_LEFT - MARGIN_RIGHT) / \
            (2*len(self.data_array)-1)
        self.bar_gap = self.bar_width
        self.colors = []
        for i in range(0,self.data_size):
            self.colors.append('white')
        self.sorted = False

    def draw_data(self, j=None):
        if (j == None):
            for index, element in enumerate(self.data_array):
                x = MARGIN_LEFT + index * \
                    (self.bar_width + self.bar_gap)
                y = self.window_height - MARGIN_TOP - element
                rect = pygame.Rect(x, y, self.bar_width, element)
                pygame.draw.rect(self.window, self.colors[index], rect)
        else:
            index = j
            element = self.data_array[j]
            x = MARGIN_LEFT + index * \
                (self.bar_width + self.bar_gap)
            # y = self.window_height - self.margins - 450
            # rect = pygame.Rect(x,y,self.bar_width, 450)
            # pygame.draw.rect(self.window, 'black', rect)
            y = self.window_height - MARGIN_TOP - element
            rect = pygame.Rect(x, y, self.bar_width, element)
            pygame.draw.rect(self.window, self.colors[index], rect)
        pygame.display.update()

    def random_gen(self, x, y):
        return random.randrange(x, y)


class select_algorithm_button:
    def __init__(self, global_info, number, text, function_object):
        self.select_button = buttons_class.Button(
            global_info, 0, number*36, text, False, True)
        self.select_button.width = 200
        self.select_button.height = 36
        self.select_button.margin = 10
        self.select_button.button_rect = pygame.Rect(
            self.select_button.x_pos, self.select_button.y_pos, self.select_button.width, self.select_button.height)
        self.function = function_object
        self.select_button.Draw(global_info)

    def check_click(self):
        return self.select_button.check_click()


def static_screen(global_info):
    menu_button = buttons_class.Button(global_info, 0, 1, "", False, True)
    menu_button.button_rect = pygame.Rect(0, 1, 130, 34)

    pygame.draw.rect(global_info.window, 'white',
                     pygame.Rect(MARGIN_LEFT, 1, global_info.window_width - MARGIN_LEFT, 34), 2, 10)
    heading = global_info.font1.render(
        "Selected Algorithm : " + global_info.selection, True, 'white')
    global_info.window.blit(heading, (370, 9))

    algorithms_menu(global_info)

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


def algorithms_menu(global_info):

    algorithm_buttons = {}

    algorithm_buttons["Bubble Sort"] = select_algorithm_button(
        global_info, 0, "Bubble Sort", display_algorithms.bubble_sort)
    algorithm_buttons["Insertion Sort"] = select_algorithm_button(
        global_info, 1, "Insertion Sort", display_algorithms.insertion_sort)
    algorithm_buttons["Merge Sort"] = select_algorithm_button(
        global_info, 2, "Merge Sort", display_algorithms.merge_sort)
    algorithm_buttons["Quick Sort"] = select_algorithm_button(
        global_info, 3, "Quick Sort", display_algorithms.quick_sort)
    algorithm_buttons["Selection Sort"] = select_algorithm_button(
        global_info, 4, "Selection Sort", display_algorithms.selection_sort)
    algorithm_buttons["Radix Sort"] = select_algorithm_button(
        global_info, 5, "Radix Sort", display_algorithms.radix_sort)

    for key, value in algorithm_buttons.items():
        if value.check_click():
            global_info.selection = key
            global_info.algorithm = value.function
            global_info.state = "Reset"


def main():

    global_info = global_information(150)
    running = True
    global_info.algorithm = display_algorithms.merge_sort
    global_info.algorithm_object = global_info.algorithm(global_info)
    while running:
        global_info.window.fill('black')
        global_info.timer.tick(global_info.fps)

        static_screen(global_info)

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
