import pygame


pygame.init()

window = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
# fps = 60
# timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)


class Button:
    def __init__(self, x_pos, y_pos, text, draw_self, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.rendered_text = font.render(self.text, True, 'black')
        self.draw_self = draw_self
        self.enabled = enabled
        self.border_color = 'black'
        self.button_color = 'light gray'
        self.button_click_color = 'dark gray'
        if self.draw_self:
            self.width, self.height = pygame.Surface.get_size(self.rendered_text)
            self.margin = 5
            self.width += 2*self.margin
            self.height += 2*self.margin
            self.button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
            self.Draw()

    def Draw(self):
        if self.check_click():
            pygame.draw.rect(window, self.button_click_color, self.button_rect, 0, 5)
        else:
            pygame.draw.rect(window, self.button_color, self.button_rect, 0, 5)
        pygame.draw.rect(window, self.border_color, self.button_rect, 2, 5)
        window.blit(self.rendered_text, (self.x_pos + self.margin, self.y_pos + self.margin))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and self.button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
