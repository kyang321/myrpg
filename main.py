import pyglet
from pyglet.gl import *
from game import resources, charactor, gui, load, player

pyglet.options['debug_gl'] = 0

# CREATE WINDOW OBJECT
window = pyglet.window.Window(1600, 900, vsync=0)
main_batch = pyglet.graphics.Batch()

objects = load.load_objects(main_batch, window)

for obj in objects:
    for handler in obj.event_handlers:
        window.push_handlers(handler)

bg_image, health_bars, fps = load.load_gui(main_batch, window, objects[0], objects[1])

@window.event
def on_draw():
    window.clear()

    bg_image.blit(0, -50)
    main_batch.draw()
    health_bars
    fps.draw()


def update(dt):
    for obj in objects:
        obj.update(dt)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
