import pyglet
import resources, charactor

''' Currently this module is not being used.'''


class Charactor_Draw(pyglet.sprite.Sprite):
    def __init__(self, charactor=None, *args, **kwargs):
        super(Charactor_Draw, self).__init__(*args, **kwargs)
        self.charactor = charactor
        self.drotate = 0

    def damage(self):
        pass

    def death(self):
        self.drotate = 3

    def update(self):
        if self.rotation < 90:
            self.rotation += self.drotate
        self.x = self.charactor.x
        self.y = self.charactor.y


