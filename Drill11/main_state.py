import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []
brick = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls
    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 0)


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
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # fill here for collision check
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)

    for ball in balls:
        if collide(grass, ball):
            ball.stop()

    for ball in balls:
        if collide(brick, ball):
            ball.speed = brick.speed
            ball.dir = brick.dir
            ball.y = brick.y + 40
            ball.x += ball.speed * game_framework.frame_time * ball.dir

    if collide(boy, brick):
        if boy.jumping or boy.falling:
            boy.jumping = False
            boy.falling = False
        if boy.y > brick.y:
            boy.x += brick.speed * game_framework.frame_time * brick.dir
            boy.y = 260
        else:
            boy.y -= game_framework.frame_time * 200

    elif not collide(boy, brick):
        boy.y -= game_framework.frame_time * 200
        if boy.y <= 90:
            boy.y = 90

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






