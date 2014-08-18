import pyglet
from pyglet.gl import *

winWidth = 800
winHeight = 600
window = pyglet.window.Window(winWidth, winHeight)
image = pyglet.resource.image('sWar.png')
image.width = 200
image.height = 350

@window.event
def on_draw():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window.clear()
    image.color = (255,0,0)
    image.blit(winWidth - image.width - 10,0)

pyglet.app.run()
