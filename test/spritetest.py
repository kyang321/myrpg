import pyglet

window = pyglet.window.Window()

rockout = pyglet.image.load('linkattack.png')
rockout_seq = pyglet.image.ImageGrid(rockout, 2, 7)

rockout_tex_seq = pyglet.image.TextureGrid(rockout_seq)

n=0

@window.event
def on_draw():
    window.clear()
    rockout_tex_seq[:7][n].blit(0,0)

def update(dt):
    global n
    n += 1
    if n >= 7: #this doesn't seem to restart the loop as intended
        n = 0

pyglet.clock.schedule_interval(update, 1/1.0)

pyglet.app.run()
