import pygame
import random
import buttons_class
import display_algorithms
from enum import Enum


class anime_state(Enum):
    PLAY = 1
    PAUSE = 0
    RESET = 2


class colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    GREY = (200, 200, 200)
    CYAN = (0,255,255)
    ORANGE = (255,165,0)


pygame.init()

MARGIN_TOP = 20
MARGIN_LEFT = 210
MARGIN_RIGHT = 20


class global_information:
    fps = 120
    window_height = 550
    window_width = 1000
    state = anime_state.RESET
    sorted = False
    selection = "Merge Sort"  # Algorithm text
    algorithm = None  # selected algorithm function
    algorithm_object = None  # generator object
    anime_controls = []
    algorithm_buttons = {}

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
        for _ in range(0, self.data_size):
            self.colors.append(colors.WHITE)
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
            y = self.window_height - MARGIN_TOP - 450
            rect = pygame.Rect(x, y, self.bar_width, 450)
            pygame.draw.rect(self.window, colors.BLACK, rect)
            y = self.window_height - MARGIN_TOP - element
            rect = pygame.Rect(x, y, self.bar_width, element)
            pygame.draw.rect(self.window, self.colors[index], rect)
        pygame.display.update()

    def get_anime_rect(self):
        x = MARGIN_LEFT
        y = self.window_height - MARGIN_TOP - 450
        width = self.window_width - MARGIN_LEFT - MARGIN_RIGHT
        height = 450
        rect = pygame.Rect(x, y, width, height)
        return rect

    def random_gen(self, x, y):
        return random.randrange(x, y)


GLOBAL_INFO = global_information(150)


class select_algorithm_button:
    def __init__(self, number, text, function_object):
        self.select_button = buttons_class.Button(
            GLOBAL_INFO, 0, number*36, text, False, True)
        self.select_button.width = 200
        self.select_button.height = 36
        self.select_button.margin = 10
        self.select_button.button_rect = pygame.Rect(
            self.select_button.x_pos, self.select_button.y_pos, self.select_button.width, self.select_button.height)
        self.function = function_object
        self.select_button.Draw(GLOBAL_INFO)

    def check_click(self):
        return self.select_button.check_click()


def static_screen():
    pygame.draw.rect(GLOBAL_INFO.window, colors.BLACK, pygame.Rect(
        MARGIN_LEFT, 1, GLOBAL_INFO.window_width-MARGIN_LEFT, 34))
    pygame.draw.rect(GLOBAL_INFO.window, colors.WHITE,
                     pygame.Rect(MARGIN_LEFT, 1, GLOBAL_INFO.window_width - MARGIN_LEFT, 34), 2, 10)
    heading = GLOBAL_INFO.font1.render(
        "Selected Algorithm : " + GLOBAL_INFO.selection, True, colors.WHITE)
    GLOBAL_INFO.window.blit(heading, (370, 9))

    GLOBAL_INFO.anime_controls.append(buttons_class.Button(
        GLOBAL_INFO, 410, 550, "Play", True, True))
    GLOBAL_INFO.anime_controls.append(buttons_class.Button(
        GLOBAL_INFO, 457, 550, "Pause", True, True))
    GLOBAL_INFO.anime_controls.append(buttons_class.Button(
        GLOBAL_INFO, 520, 550, "Reset", True, True))


def algorithms_menu():

    GLOBAL_INFO.algorithm_buttons["Bubble Sort"] = select_algorithm_button(
        0, "Bubble Sort", display_algorithms.bubble_sort)
    GLOBAL_INFO.algorithm_buttons["Insertion Sort"] = select_algorithm_button(
        1, "Insertion Sort", display_algorithms.insertion_sort)
    GLOBAL_INFO.algorithm_buttons["Merge Sort"] = select_algorithm_button(
        2, "Merge Sort", display_algorithms.merge_sort)
    GLOBAL_INFO.algorithm_buttons["Quick Sort"] = select_algorithm_button(
        3, "Quick Sort", display_algorithms.quick_sort)
    GLOBAL_INFO.algorithm_buttons["Selection Sort"] = select_algorithm_button(
        4, "Selection Sort", display_algorithms.selection_sort)
    GLOBAL_INFO.algorithm_buttons["Radix Sort"] = select_algorithm_button(
        5, "Radix Sort", display_algorithms.radix_sort)


def check_controls():

    if GLOBAL_INFO.anime_controls[0].check_click():
        GLOBAL_INFO.state = anime_state.PLAY
    if GLOBAL_INFO.anime_controls[1].check_click():
        GLOBAL_INFO.state = anime_state.PAUSE
    if GLOBAL_INFO.anime_controls[2].check_click():
        GLOBAL_INFO.state = anime_state.RESET
    
    for i in range(0,3):
        GLOBAL_INFO.anime_controls[i].Draw(GLOBAL_INFO)

    for key, value in GLOBAL_INFO.algorithm_buttons.items():
        value.select_button.Draw(GLOBAL_INFO)
        if value.check_click():
            GLOBAL_INFO.selection = key
            GLOBAL_INFO.algorithm = value.function
            GLOBAL_INFO.state = anime_state.RESET
            pygame.draw.rect(GLOBAL_INFO.window, colors.BLACK, pygame.Rect(
                MARGIN_LEFT, 1, GLOBAL_INFO.window_width-MARGIN_LEFT, 34))
            pygame.draw.rect(GLOBAL_INFO.window, colors.WHITE,
                             pygame.Rect(MARGIN_LEFT, 1, GLOBAL_INFO.window_width - MARGIN_LEFT, 34), 2, 10)
            heading = GLOBAL_INFO.font1.render(
                "Selected Algorithm : " + GLOBAL_INFO.selection, True, colors.WHITE)
            GLOBAL_INFO.window.blit(heading, (370, 9))


def main():

    running = True
    GLOBAL_INFO.algorithm = display_algorithms.merge_sort
    GLOBAL_INFO.algorithm_object = GLOBAL_INFO.algorithm(GLOBAL_INFO)
    static_screen()
    algorithms_menu()
    while running:
        GLOBAL_INFO.timer.tick(GLOBAL_INFO.fps)

        check_controls()

        if GLOBAL_INFO.state == anime_state.PAUSE:
            pygame.draw.rect(GLOBAL_INFO.window, colors.BLACK,
                             GLOBAL_INFO.get_anime_rect())
            GLOBAL_INFO.draw_data()
        if GLOBAL_INFO.state == anime_state.RESET:
            GLOBAL_INFO.generate_list()
            GLOBAL_INFO.algorithm_object = GLOBAL_INFO.algorithm(
                GLOBAL_INFO)
            GLOBAL_INFO.state = anime_state.PAUSE
        if GLOBAL_INFO.state == anime_state.PLAY and not GLOBAL_INFO.sorted:
            next(GLOBAL_INFO.algorithm_object)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update() 

    pygame.quit()


if __name__ == "__main__":
    main()
