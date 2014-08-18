import pyglet

window = pyglet.window.Window()

@window.event
def on_mouse_motion(x, y, dx, dy):
    print 'x: %d y: %d dx: %d dy: %d' % (x, y, dx, dy)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
