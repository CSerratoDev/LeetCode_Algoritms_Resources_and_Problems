#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Subnets {
    string ip;
    int numberSubnets;
    int mask;
};

void typeClass(int c){
    switch (c) {
        case 1:
            cout << "Class A\n";
            break;
        case 2:
            cout << "Class B\n";
            break;
        case 3:
            cout << "Class C\n";
            break;
        default:
            cout << "Class undefined\n";
            break;
    }
};

int main() {
    string aux;
    int count = 0;
    vector<int> ipClass;
    Subnets s;

    cout << "Enter Network IP: ";
    cin >> s.ip;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout << "Enter number subnets that you need: ";
    cin >> s.numberSubnets;
    
    //data registered
    for (int i = 0; i < 20; i++) {
        cout<<"*";
    };
    cout << "\nNetwork Registered\n";
    cout << "Network IP: " << s.ip << "\nSubnets: " << s.numberSubnets << endl;
    
    // Convert string -> vector<int>
    for (char i : s.ip) {
        if (i != '.') {
            aux += i;
        } else {
            ipClass.push_back(stoi(aux));
            aux = "";
        }
    }
    // Last digit push
    if (!aux.empty()) {
        ipClass.push_back(stoi(aux));
    }

    //Are there zeros?
    for (int n : ipClass) {
        if (n == 0) {
            typeClass(count);
            break;
        }
        count++;
    }
    
    return 0; 
}