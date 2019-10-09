from pico2d import *
import math
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global gotoX, gotoY
    global fromX, fromY
    global isMove
    global px, py
    global cnt

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            fromX, fromY = px, py
            gotoX, gotoY = event.x, KPU_HEIGHT - 1 - event.y
            isMove = True
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

frame = 0
isMove = False
gotoX, gotoY = 0, 0
fromX, fromY = 0, 0
mx, my = 0, 0
i = 0
px, py = KPU_WIDTH // 2, KPU_HEIGHT // 2
cnt = 0
hide_cursor()



def move(p1, p2):
    global px, py
    global i
    global cnt
    global isMove

    t = cnt / 100

    px = (1 - t) * p1[0] + t * p2[0]
    py = (1 - t) * p1[1] + t * p2[1]

    cnt = cnt + 5

    if cnt > 100 :
        isMove = False
        cnt = 0
    pass


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    arrow.clip_draw(0, 0, 50, 52, x, y)

    if isMove:
        move((fromX, fromY), (gotoX, gotoY))

        if gotoX < mx:
            character.clip_draw(frame * 100, 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, px, py)
    else:
        character.clip_draw(frame * 100, 300, 100, 100, px, py)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()