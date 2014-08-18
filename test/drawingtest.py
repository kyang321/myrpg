import pyglet

window = pyglet.window.Window()

def gradient_box():
    for i in range(100):
        for j in range(100):
            color = i + j
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (i, j)),
                ('c3B', (color, color, color))
            )

@window.event()
def on_draw():
    window.clear()

    pyglet.gl.glColor4f(1.0, 0, 0, 1.0)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0,1,2,0,2,3],
            ('v2i', (100, 100,
                     150, 100,
                     150, 150,
                     100, 150))
            )



pyglet.app.run()
