from pico2d import *
import random

####################### Game object class
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


####################### initialization code
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.size = random.randint(0, 1)    # 0: 21X21 , 1: 41X41
        self.speed = random.randint(5, 20)
        if self.size == 0:
            self.image = load_image('ball21X21.png')
        else:
            self.image = load_image('ball41X41.png')

    def draw(self):
            self.image.draw(self.x, self.y)

    def update(self):
        if self.size == 0 and self.y > 21 // 2 + 60:
            self.y -= self.speed
            if self.y < 21 // 2 + 60:
                self.y = 21 // 2 + 54
        elif self.size == 1 and self.y > 41 // 2 + 60:
            self.y -= self.speed
            if self.y < 41 // 2 + 60:
                self.y = 41 // 2 + 54


open_canvas()

team = [Boy() for i in range(11)]
balls = [Ball() for j in range(20)]
grass = Grass()

running = True

###################### game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    for ball in balls:
        ball.update()

    update_canvas()

    delay(0.05)


###################### finalization code
close_canvas()
