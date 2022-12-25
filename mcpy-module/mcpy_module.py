"""
mcpytools-module-version
"""

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
    return volume


"""
stronghold code
"""

def first_stronghold_step(first_angle:float, facing:str):
    match facing:
        case 'north':
            coords = -310
        case 'south':
            coords = 310
        case 'west':
            coords = -310
        case 'east':
            coords = 310
