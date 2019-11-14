import game_framework
from pico2d import *
import game_world

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 1픽셀당 3cm
RUN_SPEED_KMPH = 20.0 # 속도 20km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed  1초당 날개짓 1번
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.frame_x = 0
        self.frame_y = 0

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = int(self.frame) % 5
        self.frame_y += 1

        if self.dir == 1:
            self.velocity = RUN_SPEED_PPS
        else:
            self.velocity = -RUN_SPEED_PPS

        if self.x >= 1400:
            self.dir = 0
        elif self.x <= 200:
            self.dir = 1

        if self.frame_y == 2:
            self.frame_y = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame_x * 183, self.frame_y * 168, 183, 168, self.x, self.y, 200, 200)
        else:
            self.image.clip_composite_draw(self.frame_x * 183, self.frame_y * 168, 183, 168,
                                           0.0, 'h', self.x, self.y, 200, 200)


