function findMax() {
    let max = -Infinity;
    for(let i = 0; i< arguments.length; i++){
        if (arguments[i]> max) {
            max = arguments[i];
        }
    }
    return max;
}

// Tenemos un constructor llamado arguments
// El contiene una lista de argumentos usados cuando la funcion es llamada o invocada
x = findMax(1,2,3,42,512,3,1)

console.log(x);