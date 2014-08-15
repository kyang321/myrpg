import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex

# LOAD IN CHARACTOR SPRITES
# Need a more integrated way to do this
skel_image = pyglet.resource.image('sWar.png')
skel_image.width = 200
skel_image.height = 350

warr_image = pyglet.resource.image('warrior.png')
warr_image.width = 845/3
warr_image.height = 858/3 
warr_image = warr_image.get_transform(flip_x=True)


