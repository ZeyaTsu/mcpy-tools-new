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

function stronghold(){
    var First_Angle = document.getElementById('first_angle').value
    var Facing = document.getElementById('list').value

    switch (Facing) {
        case 'north':
            var coords = -310
            document.getElementById('step').innerHTML = "Please go to X: 0 Z: -310 and redo the steps above."
            break
        case 'south':
            var coords = 310
            document.getElementById('step').innerHTML = "Please go to X: 0 Z: 310 and redo the steps above."
            break
        case 'east':
            var coords = 310
            document.getElementById('step').innerHTML = "Please go to X: 310 Z: 0 and redo the steps above."
            break
        case 'west':
            var coords = -310 
            document.getElementById('step').innerHTML = "Please go to X: -310 Z: 0 and redo the steps above."
            break           
    }
    var Second_Angle = document.getElementById('second_angle').value

    var final_first_angle = 90 - First_Angle
    var final_second_angle = 90 - Second_Angle

    var we_first_angle = First_Angle
    var we_second_angle = Second_Angle

    function north_south(final_first_angle, coords,final_second_angle){
        console.log('north_south')
        console.log(coords)
        var h1 = final_first_angle * (Math.PI/180)
        var h2 = final_second_angle * (Math.PI/180)

        var xNorthFind = -(coords / (Math.tan(h1) - Math.tan(h2)))
        var zNorthFind = (coords * Math.tan(h1)) / (Math.tan(h1) - Math.tan(h2))

        document.getElementById('x_coords').innerHTML = xNorthFind
        document.getElementById('z_coords').innerHTML = zNorthFind
    }

    function west_east(we_first_angle, coords, we_second_angle){
        console.log('west_east')
        h3 = we_first_angle * (Math.PI/180)
        h4 = we_second_angle * (Math.PI/180)
        
        var xWestFind = (coords * Math.tan(h3)) / (Math.tan(h3) - Math.tan(h4))
        var zWestFind = -(coords / (Math.atan(h3) - Math.tan(h4)))

        document.getElementById('x_coords').innerHTML = xWestFind
        document.getElementById('z_coords').innerHTML = zWestFind
    }
    switch (Facing) {
        case 'north':
            north_south(final_first_angle, coords, final_second_angle);
            break
        case 'south':
            north_south(final_first_angle, coords, final_second_angle);
            break
        case 'east':
            west_east(we_first_angle, coords, we_second_angle);
            break
        case 'west':
            west_east(we_first_angle, coords, we_second_angle);    
            break      
    }
}