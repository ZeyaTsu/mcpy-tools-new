function volume(){
    var first_x = document.getElementById('first_x').value;
    var first_y = document.getElementById('first_y').value;
    var first_z = document.getElementById('first_z').value;

    var second_x = document.getElementById('second_x').value;
    var second_y = document.getElementById('second_y').value;
    var second_z = document.getElementById('second_z').value;
    
    var vector_x = second_x - first_x
    if (vector_x < 0) {
        vector_x = vector_x * (-1)
    }
    vector_x += 1

    var vector_y = second_y - first_y
    if (vector_y < 0) {
        vector_y = vector_y * (-1)
    }
    vector_y += 1

    var vector_z = second_z - first_z
    if (vector_z < 0) {
        vector_z = vector_z * (-1)
    }
    vector_z += 1
    
    var volume_result = vector_x * vector_y * vector_z
    document.getElementById('volume-result').innerHTML = volume_result
}

function perimeter(){
    var first_x = document.getElementById('first_x').value;
    var first_y = document.getElementById('first_y').value;
    var first_z = document.getElementById('first_z').value;

    var second_x = document.getElementById('second_x').value;
    var second_y = document.getElementById('second_y').value;
    var second_z = document.getElementById('second_z').value;
    
    var vector_x = second_x - first_x
    if (vector_x < 0) {
        vector_x = vector_x * (-1)
    }

    var vector_y = second_y - first_y
    if (vector_y <= 0) {
        vector_y = vector_y * (-1)
    }
    vector_y += 1

    var vector_z = second_z - first_z
    if (vector_z < 0) {
        vector_z = vector_z * (-1)
    }
    
    var perimeter_result = ((vector_z + vector_x)*2)*vector_y
    document.getElementById('perimeter-result').innerHTML = perimeter_result
}

function converter(){
    var block = document.getElementById('blocks').value
    var chunk = document.getElementById('chunks').value

    if (chunk == false) {
        var converter_result = block / 16
        document.getElementById('base_value').innerHTML = block
        var first_type = "blocks"
        var second_type = "chunks"
    }
    if (block == false) {
        var converter_result = chunk * 16
        document.getElementById('base_value').innerHTML = chunk
        var first_type = "chunks"
        var second_type = "blocks"
    }
    if (block ==  false && chunk == false) {
        var first_type = ""
        var second_type = ""
        var converter_result = ""
        document.getElementById('equals').innerHTML = "Can't calculate."
    }
    else {
        document.getElementById('equals').innerHTML = "equals to"
        document.getElementById('converter_result').innerHTML = converter_result
        document.getElementById('type').innerHTML = first_type
        document.getElementById('second_type').innerHTML = second_type
    }
}

function mineshaft(){
    var x_coords = document.getElementById('first_x').value
    var z_coords = document.getElementById('first_z').value

    var mineshaft_x = x_coords * -1
    var mineshaft_z = z_coords * -1

    document.getElementById('x-coords').innerHTML = mineshaft_x
    document.getElementById('z-coords').innerHTML = mineshaft_z
}