import ability
import time
import pyglet
from pyglet import clock
from pyglet.window import key


class Charactor(pyglet.sprite.Sprite):
    def __init__(self, name, hp=500, *args, **kwargs):
        super(Charactor, self).__init__(*args, **kwargs)
        self.name = name
        self.hp = hp
        self.dead = False
        self.status = []
        self.abilities = [None, ability.basic_attack, ability.rend, None, None]

        # Time stuff
        self.clock = time.time() # two clocks bc auto attack and status clash
        self.statusclock = time.time()
        self.event_handlers = []

        # Movement
        self.dx = 0.0
        self.dy = 0.0

    def status_effect(self):
        if self.status == []:
            return
        elif time.time() - self.statusclock > 1.0 and not self.dead:
            self.statusclock = time.time()
            for n in xrange(len(self.status)):
                status = self.status[n][0]
                duration = self.status[n][1]

                status.effect()
                print 'Duration on %s is %d seconds.' % (status.name, duration)
                self.status[n][1] -= 1
                if duration <= 0:
                    print '%s is over.' % (status.name)
                    del self.status[n]
                    

    def update(self, dt):
        if self.hp <= 0 and not self.dead:
            self.dead = True
            print self.name, 'is dead.'
            return
        if not self.dead:
            self.status_effect()
            self.x += self.dx
            self.y += self.dy



class NPC(Charactor):
    '''Currently the only difference between an NPC and a Player is
    that NPCs will auto-attack while Players can control their inputs.
    '''
    def update(self, dt): 
        super(NPC, self).update(dt)
        if time.time() - self.clock > 1.0 and not self.dead and not self.target.dead:
            ability.basic_attack.cast(self, self.target)
            self.clock = time.time()
