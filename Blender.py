import bpy
import mathutils
from math import radians
from math import *
import os


def uvMapperCube(cube):
    """ Put image to an object"""
    # used names
    matname = "cube"
    texname = "texture"
    # new material
    if not matname in bpy.data.materials:
        material = bpy.data.materials.new(matname)
        material.diffuse_color = (0, .5, .4)
        cube.data.materials.append(material)
    # new texture
    texUV = bpy.data.textures.new(texname, type="IMAGE")
    image_path = os.path.expanduser("/Users/christodoulos/Desktop/texture.jpg")
    image = bpy.data.images.load(image_path)
    texUV.image = image
    # connect textur with material
    bpy.data.materials[matname].texture_slots.add()
    bpy.data.materials[matname].active_texture = texUV
    bpy.data.materials[matname].texture_slots[0].texture_coords = "GLOBAL"
    bpy.data.materials[matname].texture_slots[0].mapping = "CUBE"


bpy.ops.mesh.primitive_cube_add()
cube= bpy.context.object
bpy.data.objects["Cube"].name = "cube"
cube.select = True
cube.location = (0.0,0.0,0.998344)
uvMapperCube(cube)

marks = 0
moves = 0
i = 0

def render_and_save(moves,marks,i):
    bpy.ops.object.camera_add()
    camera = bpy.context.object#bpy.data.objects["Camera"]
    bpy.data.objects["Camera"].name = "camera"
    camera.select = True
    x = 7.48113
    y = -6.49764
    z = 5.34367
    r = sqrt((x*x)+(y*y))
    rad1 = radians(63.6)
    rad2 = 0.0
    rad3 = radians(46.7)
    di = sqrt((rad1*rad1)+(rad3*rad3))
    camera.location = ((r*cos(pi/50 * i)),(r*sin(pi/50 * i)),z)
    camera.rotation_euler = (di,rad2 , di)
    camera.dimensions = (2,2,2)
    pointyobj = bpy.data.objects['camera']
    targetobj = bpy.data.objects['cube']
    ttc = pointyobj.constraints.new(type='TRACK_TO')
    ttc.target = targetobj
    ttc.track_axis = 'TRACK_NEGATIVE_Z'
    ttc.up_axis = 'UP_Y'
    ttc.use_target_z
    bpy.context.scene.camera = bpy.data.objects['camera']
    bpy.context.scene.render.filepath = "/Users/christodoulos/Desktop/RenderImage/Camera1/{}.jpg".format(moves)
    bpy.context.scene.render.resolution_percentage = 100
    bpy.ops.render.render(write_still=True, use_viewport=True) 
    bpy.data.objects['camera'].select = True
    bpy.ops.object.delete() 
    bpy.ops.object.camera_add()
    camera = bpy.context.object
    #bpy.data.objects["Camera"]
    bpy.data.objects["Camera"].name = "camera"
    camera.select = True
    x1 = -4.54677
    y1 = -5.09675
    z1 = 2.6873
    r1 = sqrt((x1*x1)+(y1*y1))
    rad4 = radians(68)
    rad5 = 0.0
    rad6 = radians(-43.5)
    dia = sqrt((rad4*rad4)+(rad6*rad6))
    camera.location = ((r1*cos(pi/50 * i)),(r1*sin(pi/50 * i)),z1)
    camera.rotation_euler = (dia, rad5, dia)
    camera.dimensions = (2,2,2)
    pointyobj1 = bpy.data.objects['camera']
    ttc1 = pointyobj1.constraints.new(type='TRACK_TO')
    ttc1.target = targetobj
    ttc1.track_axis = 'TRACK_NEGATIVE_Z'
    ttc1.up_axis = 'UP_Y'
    ttc1.use_target_z
    bpy.context.scene.camera = bpy.data.objects['camera']
    bpy.context.scene.render.filepath = "/Users/christodoulos/Desktop/RenderImage/Camera2/{}.jpg".format(marks)
    bpy.context.scene.render.resolution_percentage = 100
    bpy.ops.render.render(write_still=True, use_viewport=True) 
    bpy.data.objects['camera'].select = True
    bpy.ops.object.delete()

while moves < 101 and marks <101:
    render_and_save(moves,marks,i)
    moves += 1
    marks += 1
    i += 1
