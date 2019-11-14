from pico2d import *
import game_framework

class Brick:
    def __init__(self):
        self.image = load_image('brick180X40.png')
        self.x, self.y = 800, 200
        self.speed = 400
        self.dir = 1

    def update(self):
        self.x += self.speed * game_framework.frame_time * self.dir
        if self.x >= 1400:
            self.dir = -1
        elif self.x <= 200:
            self.dir = 1
        clamp(0, self.x, 1600)

    def draw(self):
        self.image.draw(self.x, self.y, 180, 40)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

