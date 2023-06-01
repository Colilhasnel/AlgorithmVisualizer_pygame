import pygame
import random
import time

pygame.init()

data_array = random.sample(range(1, 450), 100)
rect_array = []

window_height = 550
window_width = 1000

margins = 20

bar_width = (window_width - 2*margins)/(2*len(data_array)-1)
bar_gap = bar_width

max_height = max(data_array)

x = margins
y = window_height/2

for element in data_array:
    y = window_height - margins - element
    rect_array += [(element, pygame.Rect(x, y, bar_width, element))]
    x += bar_width + bar_gap

print(rect_array[1][0])

print(rect_array[1][1][0])
print(rect_array[1][1][3])


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Algorithm Visualizer")

background_color = pygame.Color('black')
bar_color = pygame.Color('white')

clock = pygame.time.Clock()    

k = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(background_color)

    for element in rect_array:
        pygame.draw.rect(window, bar_color, element[1])
    
    if k == 0:
        for i in range(0, len(rect_array)):
            for j in range(0, i):
                if (rect_array[j] > rect_array[i]):
                    temp = rect_array[j]
                    rect_array[j] = rect_array[i]
                    rect_array[i] = temp
                window.fill(background_color)
                for element in rect_array:
                    pygame.draw.rect(window, bar_color, element[1])
                pygame.display.update()
        print("COMPLETE")
        k = 1


    pygame.display.update()


pygame.quit()
