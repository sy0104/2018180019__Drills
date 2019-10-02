from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
right = True

while True:
    clear_canvas()
    grass.draw(400, 30)

    if right:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        x += 10
        if x >= 800:
            right = False
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        x -= 10
        if x <= 0:
            right = True

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()

close_canvas()
