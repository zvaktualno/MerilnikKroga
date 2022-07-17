import pygame as pg


class Slider:
    def __init__(self, pos, w, h):

        x, y = pos
        self.circle_x = x
        self.volume = 50
        self.sliderRect = pg.Rect(x, y, w, h)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), self.sliderRect)
        pg.draw.circle(screen, (255, 240, 255), (self.circle_x,
                       (self.sliderRect.h / 2 + self.sliderRect.y)), self.sliderRect.h * 1.5)

    def get_volume(self):
        return self.volume

    def set_volume(self, num):
        self.volume = num

    def update_volume(self, x):
        if x < self.sliderRect.x:
            self.volume = 0
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.volume = 100
        else:
            self.volume = int((x - self.sliderRect.x) /
                              float(self.sliderRect.w) * 100)

    def on_slider(self, pos):
        x, y = pos
        if self.on_slider_hold(pos) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False

    def on_slider_hold(self, pos):
        x, y = pos
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2)) * (y - (self.sliderRect.y + self.sliderRect.h / 2)))\
                <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handle_event(self, screen, x):
        if x < self.sliderRect.x:
            self.circle_x = self.sliderRect.x
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.circle_x = self.sliderRect.x + self.sliderRect.w
        else:
            self.circle_x = x
        self.draw(screen)
        self.update_volume(x)
        print(self.volume)
