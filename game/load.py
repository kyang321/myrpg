import pyglet
import resources, charactor, gui, player

def load_objects(batch, window):
    objects = []

    # Load the charactor objects
    player_char = player.Player('Player', img=resources.warr_image, 
                           x=200, y=200, batch=batch)
    skelaton = charactor.NPC('Skelaton', hp=500, img=resources.skel_image, 
                             x=window.width-200, y=200, batch=batch)
    player_char.target = skelaton
    skelaton.target = player_char

    # Load HP indicators
    skel_hp = gui.HP(skelaton, batch=batch)
    player_hp = gui.HP(player_char, batch=batch)


    objects = [player_char, skelaton, skel_hp, player_hp]
    
    return objects

def load_gui(batch, window, player_char, skelaton):
    # Load the background image
    bg_image = pyglet.resource.image('room.png')

    fps_display = pyglet.clock.ClockDisplay()

    return bg_image, fps_display
