import pyglet
from pyglet.gl import *
from game import resources, charactor

# CREATE WINDOW OBJECT
window = pyglet.window.Window(1000,600)
main_batch = pyglet.graphics.Batch()


# Load the charactor objects
player = charactor.Player(name='Player', img=resources.warr_image, batch=main_batch,
                          x=510, y=0)
skelaton = charactor.NPC(name='Skelaton', hp=50, img=resources.skel_image, 
                         x=window.width-200-10, y=0, batch=main_batch)
player.target = skelaton
skelaton.target = player

objects = [player, skelaton]

# Load HP indicators
skel_hp = pyglet.text.Label(str(skelaton.hp), font_name='Times New Roman',
                            font_size=24, x=window.width-200/2-10, 
                            y= 350+ 10, color=(255,0,0,255),
                            anchor_x='center', anchor_y='center')

# Load the background image
bg_image = pyglet.resource.image('cave.jpg')

fps_display = pyglet.clock.ClockDisplay()

for obj in objects:
    for handler in obj.event_handlers:
        window.push_handlers(handler)

@window.event
def on_draw():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    window.clear()
    bg_image.blit(200, -20)

    main_batch.draw()

    skel_hp.text = str(skelaton.hp)
    skel_hp.draw()

    fps_display.draw()

def update(dt):
    for obj in objects:
        obj.update(dt)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
