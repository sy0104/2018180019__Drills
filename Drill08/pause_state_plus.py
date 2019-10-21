import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
pause = False

def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


    pass


def draw():
    global pause
    clear_canvas()
    #main_state.draw()

    image.draw(400, 300, 400, 400)
    delay(0.01)
    update_canvas()



def update():
    pass




def resume():
    pass





