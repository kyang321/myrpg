import time, math
import ability
import pyglet

class Charactor(pyglet.sprite.Sprite):
    def __init__(self, name, hp=500, *args, **kwargs):
        super(Charactor, self).__init__(*args, **kwargs)
        self.name = name
        self.hp = hp
        self.dead = False
        self.status = []

        self.abilities = [None, None, None, None, None]
        self.make_abilities()

        # Time stuff
        self.auto_attack_timer = 0
        self.statusclock = time.time()

        self.delay = False
        self.delay_timer = 0

        self.event_handlers = []

        # Movement
        self.dx = 0.0
        self.dy = 0.0
        self.drotat = 0

    def make_abilities(self):
        self.abilities[1] = ability.Ability('Basic Attack', 20)
        self.abilities[2] = ability.Dot(name='Rend', base_damage=0, tick_damage=20,
                                        duration=6)
        self.abilities[3] = ability.Charge(name='Charge', base_damage=0)
        self.abilities[4] = None

    def damage(self, damage):
        self.hp -= damage

    def status_effect(self):
        '''Goes through the list 'status', goes through the effect of
        each effect and also decreases the cooldown each second.
        '''
        # NOTE: All status effects are tied to a SINGLE timer so they
        # all decrement on the same second.

        if self.status == []:
            return
        elif time.time() - self.statusclock > 1.0 and not self.dead:
            self.statusclock = time.time()
            for n in xrange(len(self.status)):
                status = self.status[n]
                status.effect(self)
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

    def death(self):
        self.dead = True
        self.hp = 0
        print self.name, 'is dead.'
        self.drotat = 3
        return

    def update(self, dt):
        for ability in self.abilities:
            if ability:
                ability.cooldown.update()
        if self.rotation < 90: # This and movment should be in a sep view class
            self.rotation += self.drotat
        if self.hp <= 0 and not self.dead:
            self.death()
        if not self.dead:
            self.status_effect()
            self.x += self.dx
            self.y += self.dy


class NPC(Charactor):
    '''NPC's are charactors that automatically move and attack.'''
    def move(self):
        '''Keeps trying to move closer to it's target until within it's own width.'''
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
    
    def check_delay(self):
        '''When the NPC attacks, its movement pauses for 1 second. self.delay
        is set to True in the ability.
       # '''
        # NOTE: I need to refactor the delay because it's coming from two
        # different modules (ability.basic_attack/charactor.NPC)
        if self.delay:
            self.dx, self.dy = 0, 0
            if time.time() - self.delay_timer >= 1:
                self.delay = False

    def update(self, dt): 
        super(NPC, self).update(dt)
        if not self.dead and not self.target.dead:
            self.move()
            self.check_delay()
            if time.time() - self.auto_attack_timer > 1.0:
                self.abilities[1].cast(self, self.target)
                self.auto_attack_timer = time.time()
