import pygame
from core.scripts.config import size
from core.scripts.config import fonT

class Button:
    def __init__(self, text: str, color1: tuple, color2: tuple,
                 x: int, y: int, width: int, height: int, data: list = [], image: str = None):
        """
        Класс кнопки на экране
        :param text: текст внутри кнопки
        :param color1: цвет в виде кортежа RGB без фокуса мыши
        :param color2: цвет в виде кортежа RGB при наведении мыши
        :param x: X координата вернего левого края кнопки
        :param y: Y координата вернего левого края кнопки
        :param width: ширина кнопки в пикселях
        :param height: высота кнопки в пикселях
        """
        self.text_btn = text
        self.color1, self.color2 = color1, color2
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.data = data
        if image:
            self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),
                                       (size, size))

    def draw(self, screen: pygame.display, pos_x: int, pos_y: int, outline_color=None):
        if outline_color:
            # отрисовка границы кнопки, если таковая имеется
            pygame.draw.rect(screen, outline_color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            try:
                if self.image:
                    screen.blit(self.image, (self.x, self.y))
            except:
                pass

        if self.mouse_on_btn(pos_x, pos_y):
            pygame.draw.rect(screen, self.color2, (self.x, self.y, self.width, self.height), 0)
            try:
                if self.image:
                    screen.blit(self.image, (self.x, self.y))
            except:
                pass
        else:
            pygame.draw.rect(screen, self.color1, (self.x, self.y, self.width, self.height), 0)
            try:
                if self.image:
                    screen.blit(self.image, (self.x, self.y))
            except:
                pass

        font = pygame.font.Font(fonT, 55)
        text = font.render(self.text_btn, True, (0, 0, 0))
        if self.mouse_on_btn(pos_x, pos_y):
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2) + 5))
        else:
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def mouse_on_btn(self, pos_x: int, pos_y: int) -> bool:
        if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
            return True
        return False
    
    def get_data(self):
        return [self.data[0] - 1, self.data[1] - 1] 
    
color_main = (92, 13, 172)
additional_color = (159, 105, 214)
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_main
        self.text = text
        self.font = pygame.font.Font(fonT, 55)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = additional_color if self.active else color_main
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

