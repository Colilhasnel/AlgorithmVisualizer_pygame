import pygame
import random
import buttons_class

pygame.init()

window = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)

data_array = random.sample(range(1, 450), 100)

for i, num in enumerate(data_array):
    data_array[i] = [num, 'white']

window_height = 550
window_width = 1000

margins = 5*window_width/100
bar_width = (window_width - 2*margins)/(2*len(data_array)-1)
bar_gap = bar_width

max_height = max(data_array)

def swap():
    pass

def display():
    play_button = buttons_class.Button(410, 550, "Play", True, True)
    pause_button = buttons_class.Button(457, 550, "Pause", True, True)
    reset_button = buttons_class.Button(520, 550, "Reset", True, True)
    draw_screen()
    if play_button.check_click():
        Bubble_sort()


def draw_screen():
    for index, element in enumerate(data_array):
        x = margins + index*(bar_width + bar_gap)
        y = window_height - margins - element[0]
        rect = pygame.Rect(x, y, bar_width, element[0])
        pygame.draw.rect(window, element[1], rect)


def Bubble_sort():
    n = len(data_array)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            data_array[j][1] = 'red'
            data_array[j+1][1] = 'red'
            draw_screen()
            pygame.display.update()
            if (data_array[j][0] > data_array[j+1][0]):
                temp = data_array[j]
                data_array[j] = data_array[j+1]
                data_array[j+1] = temp
            data_array[j][1] = 'white'
            data_array[j+1][1] = 'white'
            draw_screen()
            pygame.display.update()
        data_array[n-i-1][1] = 'green'

