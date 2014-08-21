import time

class Ability(object):
    '''Base class for abilities'''
    def __init__(self, name, base_damage, range=100, cooldown=1.0, *args, **kwargs):
        self.name = name
        self.base_damage = base_damage
        self.range = range
        self.cooldown = cooldown
        self.time = time.time()

    def is_in_range(self, caster):
        return caster.distance_from_target() < self.range

    def is_off_cooldown(self):
        return time.time() - self.time > self.cooldown

    def cast(self, caster, target):
        #print '%s uses %s on %s.' % (caster.name, self.name, caster.target.name)
        if target.dead:
            print 'Target is dead.'
        elif not self.is_off_cooldown():
            print 'Ability %s is on cooldown' % (self.name)
        elif not self.is_in_range(caster):
            print 'Target is out of range.'
        else:
            #not target.dead and self.is_in_range(caster):
            print '%s deals %d damage' % (self.name, self.base_damage)
            caster.delay = True
            caster.delay_timer = time.time()
            target.hp -= self.base_damage
            self.time = time.time()

class Dot(Ability):
    def __init__(self, tick_damage, duration, *args, **kwargs):
        super(Dot, self).__init__(*args, **kwargs)
        self.tick_damage = tick_damage
        self.base_duration = duration
        self.duration = duration

    def cast(self, caster, target):
        if self.is_in_range(caster) and self not in target.status:
            self.duration = self.base_duration
            target.status.append(self)
            print '%s uses %s on %s.' % (caster.name, self.name, caster.target.name)

    def effect(self, target):
        target.hp -= self.tick_damage

class Charge(Ability):
    def __init__(self, *args, **kwargs):
        super(Charge, self).__init__(*args, **kwargs)
        self.baseduration = 1
        self.duration = 1

    def cast(self, caster, target):
        self.duration = self.base_duration
        self.target = caster
        if self.is_in_range(caster) and self not in target.status:
            caster.status.append(self)

    def effect(self, target):
        self.target.dx *= 10
        self.target.dy *= 10
