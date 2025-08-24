export { };
//INTERFACE
//interface name { any }
interface Person {
    name: string;
    age: number;
    isDeveloper: boolean;
}
// name: interface[] = [{data},{data},...,{n data}]
let persons: Person[] = [
    { name: "Alexis", age: 25, isDeveloper: true },
    { name: "John", age: 30, isDeveloper: false },
    { name: "Angela", age: 35, isDeveloper: true }
];
//methods
// name.method({data})
persons.push({ name: "Valentina", age: 19, isDeveloper: true })
//Tuple 
let personsTuple: [string, number, boolean][] = [];
personsTuple.push(["Alexis", 25, true])
personsTuple.push(["John", 30, false])
personsTuple.push(["Angela", 35, true])
//tuple.method(e => { code })
personsTuple.forEach(person => {
    console.log(`Person: ${person}`);

    let name: string = person[0];
    let age: number = person[1];
    let isDeveloper: boolean = person[2];

    console.log(`name: ${name}`);
    console.log(`age: ${age}`);
    console.log(`isDeveloper ${isDeveloper}`);
});
//Create Tuple 2° form
let personsTuplev2: [string, number, boolean];
personsTuplev2 = ["Gina", 23, false];

//Enumerate
//enum name { data, ..., n data}
enum dayOfTheWeek {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Saturday,
    Sunday
}

let day: dayOfTheWeek = dayOfTheWeek.Monday;
console.log(`Day: ${dayOfTheWeek[day]}`)