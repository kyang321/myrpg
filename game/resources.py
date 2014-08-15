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
skel_image.width = 200
skel_image.height = 350
center_image(skel_image)

warr_image = pyglet.resource.image('warrior.png')
warr_image.width = 845/3
warr_image.height = 858/3 
#warr_image = warr_image.get_transform(flip_x=True) #FLIPS THE IMAGE, SAVE FOR LATER
center_image(warr_image)

#LOAD IN GUI ELEMENTS
skill_box_image = pyglet.resource.image('skillbox.png')
center_image(skill_box_image)

