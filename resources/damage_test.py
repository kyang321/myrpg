import pyglet
from pyglet.window import key

window = pyglet.window.Window()

# Instead of individually calling images, this could be
# replaced with sprite sheets.
image1 = pyglet.resource.image('sWar.png')
image2 = pyglet.resource.image('sWar_damaged.png')
sprites = [image1]

batch = pyglet.graphics.Batch()

def update(sprites, repeat):
    anim = pyglet.image.Animation.from_image_sequence(sprites, 0.5, repeat)
    sprite = pyglet.sprite.Sprite(anim, batch=batch)

update(sprites, True)

@window.event()
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        # Handles animation by defining what sprites go into
        # the animation. DON'T WORRY ABOUT EFFICIENCY UNTIL
        # IT'S A PROBLEM!
        sprites = [image2]
        update(sprites, False)

@window.event()
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        sprites = [image2, image1]
        update(sprites, False)

@window.event()
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
