import pyglet
import resources, ability, charactor

def ability_boxes(num_icons, batch=None, window=None):
    '''Generate GUI for ability icons'''
    abilities = []
    for i in xrange(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.skill_box_image,
                                          x=window.width/2 - 96 + i*48,
                                          y=48, batch=batch)
        abilities.append(new_sprite)
    return abilities

