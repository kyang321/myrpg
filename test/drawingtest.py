import pyglet

window = pyglet.window.Window()

@window.event()
def on_draw():
    window.clear()
    for i in range(50):
        for j in range(50):
            color = int(2.56 * (i + j))
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (i, j)),
                ('c3B', (color, color, color))
            )



pyglet.app.run()
