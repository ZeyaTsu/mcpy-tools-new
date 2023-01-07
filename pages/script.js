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