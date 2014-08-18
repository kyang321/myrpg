import pyglet

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
        self.y = self.charactor.y + 200

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

