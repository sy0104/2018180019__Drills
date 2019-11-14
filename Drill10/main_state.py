import random
import json
import os

from pico2d import *
import game_framework
import game_world

from grass import Grass
from bird import Bird


name = "MainState"


def enter():
    global bird
    bird = Bird()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(bird, 0)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






