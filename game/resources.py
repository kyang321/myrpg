import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex

def center_image(image):
    '''set's an image's anchor point to its center'''
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

# LOAD IN CHARACTOR SPRITES
# Need a more integrated way to do this
skel_image = pyglet.resource.image('sWar.png')
center_image(skel_image)

skel_image_damaged = pyglet.resource.image('sWar_damaged.png')
center_image(skel_image_damaged)


warr_image = pyglet.resource.image('warrior.png')
#warr_image = warr_image.get_transform(flip_x=True) #FLIPS THE IMAGE, SAVE FOR LATER
center_image(warr_image)

warr_image_damaged = pyglet.resource.image('warrior_damaged.png')
center_image(warr_image_damaged)

#LOAD IN GUI ELEMENTS
skill_box_image = pyglet.resource.image('skillbox.png')
center_image(skill_box_image)


# Load in telegrah
telegraph_image = pyglet.resource.image('basic_attack_telegraph.png')
center_image(telegraph_image)
telegraph_image.anchor_y = -20
