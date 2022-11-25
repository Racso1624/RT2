from material import *
from sphere import *
from vector import *
from raytracer import *
from color import *

red = Material(difusse=Color(255, 0, 0), albedo = [1.3, 0.1, 0], spec = 50)
white = Material(difusse=Color(255, 255, 255), albedo = [1.3, 0.1, 0], spec = 50)
orange = Material(difusse=Color(255, 165, 0), albedo = [1.3, 0.1, 0], spec = 50)
black = Material(difusse=Color(0, 0, 0), albedo = [1.3, 0.1, 0], spec = 50)
silver = Material(difusse=Color(192, 192, 192), albedo = [1.3, 0.1, 0], spec = 30)

r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
r.scene = [
    
    Sphere(V3(-2.5, -0.4, -8), 0.4, white),
    Sphere(V3(-1.5, -0.4, -8), 0.4, white),
    Sphere(V3(-2, 0, -8), 0.7, silver),
    Sphere(V3(-2.5, 0.5, -8), 0.4, white),
    Sphere(V3(-1.5, 0.5, -8), 0.4, white),
    Sphere(V3(-2, -0.8, -8), 0.5, white),

]
r.render()
r.write('RT2.bmp')