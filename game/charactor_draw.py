import pyglet
import resources, charactor

''' Currently this module is not being used.'''


class Charactor_Draw(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Charactor_Draw, self).__init__(*args, **kwargs)
        self.charactor = charactor

