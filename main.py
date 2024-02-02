from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            orgin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0.9,1)),
            highlight_color=color.blue)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)


app = Ursina()

e1 = Entity(model="FBX/test item.fbx", texture="Tex/Sniper.png",  scale=.01, position=(1, 1, 1))


for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
app.run()