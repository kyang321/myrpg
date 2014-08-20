import pyglet
from pyglet.gl import *
from game import resources, charactor, gui, load, player

pyglet.options['debug_gl'] = 0

# CREATE WINDOW OBJECT
window = pyglet.window.Window(1600, 900, vsync=0)
main_batch = pyglet.graphics.Batch()


# Load the charactor objects
player = player.Player('Player', img=resources.warr_image, 
                       x=200, y=200, batch=main_batch)
skelaton = charactor.NPC('Skelaton', hp=500, img=resources.skel_image, 
                         x=window.width-200, y=200, batch=main_batch)
player.target = skelaton
skelaton.target = player

# Load HP indicators
skel_hp = gui.HP(skelaton, batch=main_batch)
player_hp = gui.HP(player, batch=main_batch)

# Load skill bars
ability_gui = load.ability_boxes(4, batch=main_batch, window=window)

# Load the background image
bg_image = pyglet.resource.image('room.png')

fps_display = pyglet.clock.ClockDisplay()

objects = [player, skelaton, skel_hp, player_hp]

for obj in objects:
    for handler in obj.event_handlers:
        window.push_handlers(handler)


@window.event
def on_draw():
    window.clear()
    bg_image.blit(0, -50)

    main_batch.draw()

    skel_hp.text = str(skelaton.hp)
    skel_hp.draw()

    player_hp.text = str(player.hp)
    player_hp.draw()

    gui.health_bar(player, skelaton)

    fps_display.draw()

def update(dt):
    for obj in objects:
        obj.update(dt)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
