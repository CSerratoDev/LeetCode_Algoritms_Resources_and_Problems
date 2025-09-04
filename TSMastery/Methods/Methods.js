/* Function associated with a class or object, and operates on its properties, use the keyword this */
// function name(params : dataType) : dataType that return { your code } 
function printMessage(message) {
    console.log(message);
}
printMessage("Hello, I am a message");
function sum(a, b) {
    return a + b;
}
var result = sum(2, 3);
console.log("Sum: ".concat(result));
function greeting(name, saludo) {
    if (saludo) {
        return "Hello ".concat(name, ", ").concat(saludo);
    }
    else {
        return "Hello ".concat(name);
    }
}
console.log(greeting("Valeria", "good day!"));
/*Multiple parameter*/
// function name(...colección: datatype[]): datatype { code }
function sumOptimal() {
    var nums = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        nums[_i] = arguments[_i];
    }
    return nums.reduce(function (aux, next_num) { return aux + next_num; });
}
console.log("Result: ".concat(sumOptimal(1, 2, 3, 4, 5)));
