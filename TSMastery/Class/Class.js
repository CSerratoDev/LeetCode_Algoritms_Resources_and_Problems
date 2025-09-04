"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Person = void 0;
// class name { code 
// constructor(){}
// name(): dataType{}
// } 
var Person = /** @class */ (function () {
    function Person(name, age, isDeveloper) {
        this.name = name;
        this.age = age;
        this.isDeveloper = isDeveloper;
    }
    Person.prototype.greeting = function () {
        return "Hello, my name is ".concat(this.name, " and I'm ").concat(this.age, " years old");
    };
    Person.prototype.getAge = function () {
        return this.age;
    };
    Person.prototype.questionDeveloper = function () {
        return this.isDeveloper;
    };
    return Person;
}());
exports.Person = Person;
