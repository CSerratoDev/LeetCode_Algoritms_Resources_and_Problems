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
// function name(params : dataType, optional: dataType) : dataType that return { your code }
function greeting(name: string, saludo?: string) : string {
    if (saludo){
        return `Hello ${name}, ${saludo}`
    } else {
        return `Hello ${name}`
    }
}
console.log(greeting("Valeria", "good day!"));

/*Multiple parameter*/
// function name(...collection: datatype[]): dataType that return { your code }
function sumOptimal(...nums: number[]) : number {
    return nums.reduce((aux, next_num) => aux + next_num );
}
console.log(`Result: ${sumOptimal(1,2,3,4,5)}`); // 15