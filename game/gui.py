import pyglet

class HP(pyglet.text.Label):
    def __init__(self, charactor, batch):
        super(HP, self).__init__()
        self.charactor = charactor
        self.font_name = 'Times New Roman'
        self.font_size = 48
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.color = (255, 0, 0, 255)
        self.batch = batch
        self.event_handlers = []

    def update(self, dt):
        self.hp = self.charactor.hp
        self.x = self.charactor.x
        self.y = self.charactor.y + 200
