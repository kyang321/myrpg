import pyglet

window = pyglet.window.Window()

walking = pyglet.image.load('Link_walking.png')
walking_seq = pyglet.image.ImageGrid(walking, 2, 16)

walking_tex_seq = pyglet.image.TextureGrid(walking_seq)

n=17

@window.event
def on_draw():
    window.clear()
    walking_tex_seq[:][n].blit(0,0)

def update(dt):
    global n
    n += 1
    if n >= 24: # NOTE: Image grids count from left to right BOTTOM TO TOP
        n = 17

pyglet.clock.schedule_interval(update, 1/15.0)

pyglet.app.run()
