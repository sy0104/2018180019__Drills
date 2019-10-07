from pico2d import *

open_canvas()
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')
hide_cursor()


def handle_events():
    global running
    global x, y
    global dx, dy
    global x1, y1
    global x2, y2
    global stop

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            dx, dy = event.x, KPU_HEIGHT // 2 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x1, y1 = dx, dy
            x2 = (x1 - x) / 20
            y2 = (y1 - y) / 20
            stop = 0

    pass


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dx, dy = 0, 0
x2, y2 = 0, 0
x1, y1 = 0, 0
frame = 0
stop = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.clip_draw(0, 0, 50, 52, dx, dy)

    if x1 > x:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    x += x2
    y += y2
    stop += 1
    if stop == 20:
        stop = 0
        x2, y2 = 0, 0

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()


close_canvas()

