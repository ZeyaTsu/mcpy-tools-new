"""
mcpytools-module-version
"""
import math

def convert_chunks_blocks(block=None, chunk=None):
    if block != None and chunk == None:
        res = block / 16
        return res 
    elif block == None and chunk != None:
        resp = chunk * 16
        return resp

def mineshaft_mirror(x_coords, z_coords):
    x_coords = x_coords * -1
    z_coords = z_coords * -1

    return x_coords, z_coords

def perimeter(x_coords, z_coords, y_coords,second_x_coords, second_y_coords, second_z_coords): 
    x_fi = x_coords - second_x_coords
    if x_fi < 0:
        x_fi *= -1
    x_fi += 1

    y_fi = y_coords - second_y_coords
    if y_fi < 0:
        y_fi *= -1
    y_fi += 1

    z_fi = z_coords - second_z_coords
    if z_fi < 0:
        z_fi *= -1
    z_fi += 1

    perimeter = 2*(x_fi + z_fi) * y_fi
    return perimeter

def volume(x_coords, z_coords, y_coords,second_x_coords, second_y_coords, second_z_coords): 
    x_fi = x_coords - second_x_coords
    if x_fi < 0:
        x_fi *= -1
    x_fi += 1

    y_fi = y_coords - second_y_coords
    if y_fi < 0:
        y_fi *= -1
    y_fi += 1

    z_fi = z_coords - second_z_coords
    if z_fi < 0:
        z_fi *= -1
    z_fi += 1

    volume = x_fi * z_fi * y_fi
    return 

def distance(first_x_coords, first_z_coords, second_x_coords, second_z_coords, walking_method):
    if walking_method == "run":
            vel = 5.6
    if walking_method == "elyta":
            vel = 7.2
        
    vector_x = second_x_coords - first_x_coords
    if vector_x < 0:
        vector_x *= -1
    vector_x += 1

    vector_z = second_z_coords - first_z_coords
    if vector_z < 0:
        vector_z *= -1
    vector_z += 1

    distance = int(math.sqrt((vector_x - 2)**2 + (vector_z -2)**2))
    time = distance // vel
    return time