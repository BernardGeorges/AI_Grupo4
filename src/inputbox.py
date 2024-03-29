import pygame as pg


pg.init()
infores =pg.display.Info()
mw= (infores.current_w / 1920)
mh = (infores.current_h /1080)
width = 1920* mw
height = 1080* mh
screen = pg.display.set_mode((width, height))
COLOR_INACTIVE = pg.Color((178,178,178))
COLOR_ACTIVE = pg.Color((255,255,255))
FONT = pg.font.Font(None, 40)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.first = True

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active=True
            self.color = COLOR_ACTIVE
            if self.first:
                self.text= ''
                self.first=False
            self.txt_surface = FONT.render(self.text, True, self.color)
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    pass
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
    def deactivate(self):
        self.active = False
        self.color=COLOR_INACTIVE
        self.txt_surface = FONT.render(self.text, True, self.color)
