import pygame

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Creating Buttons")

fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)


class Button:
    def __init__(self, x_pos, y_pos, text, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.enabled = enabled
        self.Draw()

    def get_button_rect(self):
        this_button_text = font.render(self.text, True, 'black')
        width, height = pygame.Surface.get_size(this_button_text)
        width += 6
        height += 6
        return pygame.Rect(self.x_pos, self.y_pos, width, height)

    def Draw(self):
        this_button_text = font.render(self.text, True, 'black')
        this_button_rect = self.get_button_rect()
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(window, 'dark gray', this_button_rect, 0, 5)
            else:
                pygame.draw.rect(window, 'light gray', this_button_rect, 0, 5)
            pygame.draw.rect(window, 'black', this_button_rect, 2, 5)
        else:
            pygame.draw.rect(window, 'black', this_button_rect, 0, 5)
        window.blit(this_button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        buttton_rect = self.get_button_rect()
        if left_click and buttton_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


new_press = False
button1_enabled = True


running = True
while running:
    window.fill('white')
    timer.tick(fps)

    my_button = Button(50, 50, "Hello World", button1_enabled)
    my_button2 = Button(50, 80, "Click Here", True)
    my_button3 = Button(50, 110, "Donot Click", True)

    if my_button3.check_click() and new_press:
        new_press = False
        if button1_enabled:
            button1_enabled = False
        else:
            button1_enabled = True

    if not my_button3.check_click() and not new_press:
        new_press = True

    if my_button2.check_click():
        display_text = font.render("Great Click", True, 'black')
        window.blit(display_text, (200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
