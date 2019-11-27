from pico2d import *
import random

class Ball:
    def __init__(self):
        self.image = load_image('ball41X41.png')
        self.hp = 100
        self.x, self.y = random.randint(100, 1100), random.randint(200, 800)

    def draw(self):
        self.image.clip_draw(0, 0, 43, 43, self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 22, self.y - 22, self.x + 22, self.y + 22
