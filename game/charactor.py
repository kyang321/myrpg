import ability
import time
import pyglet
from pyglet import clock
from pyglet.window import key


class Charactor(pyglet.sprite.Sprite):
    def __init__(self, name, hp=100, *args, **kwargs):
        super(Charactor, self).__init__(*args, **kwargs)
        self.name = name
        self.hp = hp
        self.dead = False
        self.status = []
        self.abilities = [None, ability.basic_attack, ability.rend, None, None]

        self.clock = time.time()
        self.statusclock = time.time()
        self.event_handlers = []

    def update(self, dt):
        if self.hp <= 0 and not self.dead:
            self.dead = True
            print self.name, 'is dead.'

        if time.time() - self.statusclock > 1.0 and not self.dead:
            self.statusclock = time.time()
            for n in xrange(len(self.status)):
                status = self.status[n][0]
                duration = self.status[n][1]

                status.effect()
                duration -= 1
                if duration <= 0:
                    del status[n]




class Player(Charactor):
    '''Grants keyboard input to controlled Charactor.'''
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)


        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def on_key_press(self, symbol, modifiers):
        if symbol == key._1:
            self.abilities[1].cast(self, self.target)
        elif symbol == key._2:
            self.abilities[2].cast(self, self.target)
        elif symbol == key._3:
            self.abilities[3].cast(self, self.target)
        elif symbol == key._4:
            self.abilities[4].cast(self, self.target)


class NPC(Charactor):
    '''Currently the only difference between an NPC and a Player is
    that NPCs will auto-attack while Players can control their inputs.
    '''

    def update(self, dt): 
        super(NPC, self).update(dt)
        if time.time() - self.clock > 1.0 and not self.dead and not self.target.dead:
            ability.basic_attack.cast(self, self.target)
            self.clock = time.time()
