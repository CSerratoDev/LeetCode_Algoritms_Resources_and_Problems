#include <iostream>
using namespace std;
int select(int option){
    string message = "Nice decision!";
    string message2 = "Maybe it will happen again :/";
    switch(option){
        case 1:
            cout << "You hit him and knocked him out" << endl;
            cout << message << endl;
            break;
        case 2:
            cout << "You tripped and I hit you more times" << endl;
            cout << message2 << endl;
            break;
        case 3:
            cout << "911!... He was arrested" << endl;
            cout << message << endl;
            break;
        default:
            cout << "You came out of the game" << endl;
            break;
    }
    return 0;
}
int main(){
    cout << "They just beat you up for no reason, what will you do now?" << endl;
    cout << "Option 1) To Hit!" << endl;
    cout << "Option 2) To Run out!" << endl;
    cout << "Option 3) Call the police" << endl;
    cout << "Enter an option: ";
    int option;
    cin >> option;
    select(option);
    return 0;
}