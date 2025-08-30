/* Function associated with a class or object, and operates on its properties, use the keyword this */
// function name(params : dataType) : dataType that return { your code } 
function printMessage(message: string): void {
    console.log(message);
}
printMessage("Hello, I am a message");

function sum(a: number, b: number):number {
    return a + b;
}
let result : number = sum(2,3);
console.log(`Sum: ${result}`);