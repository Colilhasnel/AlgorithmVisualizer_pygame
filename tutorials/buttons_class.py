import pygame


pygame.init()

window = pygame.display.set_mode((800,600), pygame.RESIZABLE)
# fps = 60
# timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 24)

class Button:
    def __init__(self, x_pos, y_pos, text, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.enabled = enabled
        self.Draw()

    def get_button_rect(self):
        this_button_text = font.render(self.text, True, 'black')
        width , height = pygame.Surface.get_size(this_button_text)
        width += 6
        height += 6
        return pygame.Rect(self.x_pos, self.y_pos, width, height)

    def Draw(self):
        this_button_text = font.render(self.text, True, 'black')
        this_button_rect = self.get_button_rect()
        if self.check_click():
            pygame.draw.rect(window, 'dark gray', this_button_rect, 0, 5)
        else:
            pygame.draw.rect(window, 'light gray', this_button_rect, 0 ,5)
        pygame.draw.rect(window, 'black', this_button_rect, 2, 5)
        window.blit(this_button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        buttton_rect = self.get_button_rect()
        if left_click and buttton_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
