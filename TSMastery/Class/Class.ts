// class name { code 
// constructor(){}
// name(): dataType{}
// } 
export class Person {
    public name: string; // Accessible from anywhere
    protected age: number; // Accessible from the class and subclasses
    private isDeveloper: boolean; // Accessible only from the classroom

    constructor(name: string, age: number, isDeveloper: boolean) {
        this.name = name;
        this.age = age;
        this.isDeveloper = isDeveloper;
    }

    public greeting(): string{ //Public method
        return `Hello, my name is ${this.name} and I'm ${this.age} years old`;
    }

    protected getAge(): number { //Protected method
        return this.age;
    }

    private questionDeveloper(): Boolean {
        return this.isDeveloper;
    }

}