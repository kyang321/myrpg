import pyglet
import resources, ability, charactor

class Ability_Bar(object):
    def __init__(self, num_icons, batch, window):
        self.num_icons = num_icons
        self.batch = batch
        self.window = window
        self.ability_bar = self.ability_boxes() 

    def ability_boxes(self):
        abilities = []
        bindings = []
        for i in xrange(self.num_icons):
            box_size = 48
            new_sprite = pyglet.sprite.Sprite(img=resources.skill_box_image,
                                              x=self.window.width/2 - box_size*2 
                                                + i*box_size,
                                              y=48, batch=self.batch,
                                              group=pyglet.graphics.OrderedGroup(0))
            abilities.append(new_sprite)

        for m in xrange(self.num_icons):
            n = m+1
            label = pyglet.text.Label(str(n), font_name='Times New Roman',
                                      font_size=36, batch=self.batch,
                                      x=abilities[m].x, y=abilities[m].y, 
                                      anchor_x='center', anchor_y='center',
                                      group=pyglet.graphics.OrderedGroup(1))
            bindings.append(label)

        return abilities + bindings


class HP(pyglet.text.Label):
    def __init__(self, charactor, batch):
        super(HP, self).__init__()
        self.charactor = charactor
        self.font_name = 'Times New Roman'
        self.font_size = 24
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.color = (255, 0, 0, 255)
        self.batch = batch
        self.event_handlers = []

    def update(self, dt):
        self.hp = self.charactor.hp
        self.x = self.charactor.x
        self.y = self.charactor.y + 100

def health_bar(player, boss):
    x_pos = int(player.hp/500.0 * 800)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0,1,2,0,2,3],
                                ('v2i', (    0, 850,
                                         x_pos, 850,
                                         x_pos, 900,
                                             0, 900)),
                                ('c4B', (10, 225, 10, 255) * 4))

    x_pos2 = 1600-int(boss.hp/500.0 * 800)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0,1,2,0,2,3],
                                ('v2i', (x_pos2, 850,
                                           1600, 850,
                                           1600, 900,
                                         x_pos2, 900)),
                                ('c4B', (225, 10, 10, 255) * 4))

