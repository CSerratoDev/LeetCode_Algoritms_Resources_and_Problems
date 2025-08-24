"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// name: interface[] = [{data},{data},...,{n data}]
var persons = [
    { name: "Alexis", age: 25, isDeveloper: true },
    { name: "John", age: 30, isDeveloper: false },
    { name: "Angela", age: 35, isDeveloper: true }
];
//methods
// name.method({data})
persons.push({ name: "Valentina", age: 19, isDeveloper: true });
//Tuple 
var personsTuple = [];
personsTuple.push(["Alexis", 25, true]);
personsTuple.push(["John", 30, false]);
personsTuple.push(["Angela", 35, true]);
//tuple.method(e => { code })
personsTuple.forEach(function (person) {
    console.log("Person: ".concat(person));
    var name = person[0];
    var age = person[1];
    var isDeveloper = person[2];
    console.log("name: ".concat(name));
    console.log("age: ".concat(age));
    console.log("isDeveloper ".concat(isDeveloper));
});
//Create Tuple 2° form
var personsTuplev2;
personsTuplev2 = ["Gina", 23, false];
//Enumerate
//enum name { data, ..., n data}
var dayOfTheWeek;
(function (dayOfTheWeek) {
    dayOfTheWeek[dayOfTheWeek["Monday"] = 0] = "Monday";
    dayOfTheWeek[dayOfTheWeek["Tuesday"] = 1] = "Tuesday";
    dayOfTheWeek[dayOfTheWeek["Wednesday"] = 2] = "Wednesday";
    dayOfTheWeek[dayOfTheWeek["Thursday"] = 3] = "Thursday";
    dayOfTheWeek[dayOfTheWeek["Saturday"] = 4] = "Saturday";
    dayOfTheWeek[dayOfTheWeek["Sunday"] = 5] = "Sunday";
})(dayOfTheWeek || (dayOfTheWeek = {}));
var day = dayOfTheWeek.Monday;
console.log("Day: ".concat(dayOfTheWeek[day]));
