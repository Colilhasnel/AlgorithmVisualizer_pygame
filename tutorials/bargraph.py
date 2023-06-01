import pygame

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bar Graph")

background_color = pygame.Color('blue')
bar_color = pygame.Color('red')

data = [50, 80, 120, 200, 100]

bar_width = 50
bar_gap = 20

max_height = max(data)
max_width = (bar_width + bar_gap)*len(data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(background_color)

    x = (window_width - max_width)/2
    y = (window_height - max_height)/2

    for value in data:
        rect = pygame.Rect(x,y+max_height - value, bar_width, value)
        pygame.draw.rect(window, bar_color, rect)
        x+= bar_width + bar_gap
    
    pygame.display.update()

pygame.quit()