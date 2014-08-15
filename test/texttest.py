import pyglet

window = pyglet.window.Window(800,600)

class Ability(pyglet.text.Label):
    def __init__(self, text, y):
        pyglet.text.Label.__init__(self, batch = main_batch)
        self.text = text
        self.font_name = 'Times New Roman'
        self.font_size = 24
        self.x = 20
        self.anchor_y = 'center'
        self.y = y

main_batch = pyglet.graphics.Batch()

height_level = range(window.height-50, 0, -75)

ability1 = Ability('Hello world!', height_level[0])
ability2 = Ability('Hello world!', height_level[1])
ability3 = Ability('Hello world!', height_level[2])
ability4 = Ability('Hello world!', height_level[3])
ability5 = Ability('Hello world!', height_level[4])
ability6 = Ability('Hello world!', height_level[5])

@window.event
def on_draw():
    window.clear()
    main_batch.draw()

pyglet.app.run()
