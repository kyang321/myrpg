import pyglet
from pyglet.window import key


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

walking = pyglet.image.load('Link_walking.png')
walking_seq = pyglet.image.ImageGrid(walking, 2, 16)
walking_tex_seq = pyglet.image.TextureGrid(walking_seq)

left = walking_tex_seq[16:24]
right = walking_tex_seq[25:]

direction = left

anim = pyglet.image.Animation.from_image_sequence(direction, .075, True)
sprite = pyglet.sprite.Sprite(anim)
sprite_dx = 1.5

@window.event()
def on_key_press(symbol, modifiers):
    global sprite_dx
    if symbol == key.A:
        direction = left
        sprite_dx = -1.5
    elif symbol == key.D:
        direction = right
        sprite_dx = 1.5

@window.event()
def on_key_release(symbol, modifiers):
    global sprite_dx
    if symbol == key.A or symbol == key.D:
        sprite_dx = 0

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def update(dt):
    anim = pyglet.image.Animation.from_image_sequence(left, .075, True)
    sprite = pyglet.sprite.Sprite(anim)

    sprite.x += sprite_dx
    sprite.direction = direction

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()

# NOTE: currently duplicating new objects every refresh
