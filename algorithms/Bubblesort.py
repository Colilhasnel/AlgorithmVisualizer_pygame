import pygame
import random
import time


def draw_screen():
    window.fill(background_color)
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


pygame.init()

data_array = random.sample(range(1, 450), 100)

for i, num in enumerate(data_array):
    data_array[i] = [num, 'white']

window_height = 550
window_width = 1000

margins = 5*window_width/100
bar_width = (window_width - 2*margins)/(2*len(data_array)-1)
bar_gap = bar_width

max_height = max(data_array)


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bubble Sort")

background_color = pygame.Color('black')
bar_color = pygame.Color('white')

clock = pygame.time.Clock()

k = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(background_color)

    draw_screen()
    pygame.display.update()
    if k == 0:
        Bubble_sort()
        k = 1

    pygame.display.update()


pygame.quit()
