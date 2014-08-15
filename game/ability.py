import time

class Ability(object):
    '''Base class for abilities'''
    def __init__(self, name, base_damage, cooldown=1.5, *args, **kwargs):
        self.name = name
        self.base_damage = base_damage

    def cast(self, caster, target):
        print '%s uses %s on %s.' % (caster.name, self.name, caster.target.name)
        if not target.dead:
            print '%s deals %d damage' % (self.name, self.base_damage)
            target.hp -= self.base_damage
        else:
            print 'Target is dead.'

class Dot(Ability):
    def __init__(self, tick_damage, duration, *args, **kwargs):
        super(Dot, self).__init__(*args, **kwargs)
        self.tick_damage = tick_damage
        self.duration = duration

    def cast(self, target):
        target.status.append([self, self.duration])

    def effect(self, target):
        target.hp -= self.tick_damage

basic_attack = Ability('Basic Attack', 10)
rend = Dot(name='Rend', base_damage = 0, tick_damage=10, duration=3)


