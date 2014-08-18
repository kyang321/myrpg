import time, math
import ability
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
                status = self.status[n]

                status.effect()
                print 'Duration on %s is %d seconds.' % (status.name, status.duration)
                status.duration -= 1
                if status.duration <= 0:
                    print '%s is over.' % (status.name)
                    del self.status[n]
    def distance_from_target(self):
        '''Returns a float of the distance between self and self's target'''
        x1 = self.x
        x2 = self.target.x
        y1 = self.y
        y2 = self.target.y
        
        distance = math.sqrt(float((x2-x1)**2 + (y2-y1)**2))

        return distance

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
    '''NPC's are charactors that automatically move and attack.'''
    '''
    def __init__(self, target = None):
        super(NPC, self).__init__(*args, **kwargs)
        self.target = target 
    '''

    def move(self):
        if self.distance_from_target() >= self.width:
            if self.x < self.target.x:
                self.dx = 2.5
            elif self.x > self.target.x:
                self.dx = -2.5

            if self.y < self.target.y:
                self.dy = 2.5
            elif self.y > self.target.y:
                self.dy = -2.5
        else:
            self.dx = 0
            self.dy = 0

    def update(self, dt): 
        super(NPC, self).update(dt)
        if not self.dead and not self.target.dead:
            self.move()
            if time.time() - self.clock > 1.0:
                ability.basic_attack.cast(self, self.target)
                self.clock = time.time()
