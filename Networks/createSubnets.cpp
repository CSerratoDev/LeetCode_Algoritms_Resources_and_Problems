#include <iostream>
#include <string>
#include <vector>
#include <bitset>
using namespace std;

struct Subnets {
    string ip;
    int numberSubnets;
    int mask;
};

void specialSpace() {
    for (int i = 0; i < 20; i++) {
            cout<<"*";
    };
}

string typeClass(int c){
    switch (c) {
        case 1: return "Class A";
        case 2: return "Class B";
        case 3: return "Class C";
        default: return "Class Undefined";
    }
};

string typeMask(int m){
    if (m == 3) return "255.255.255.0";
    if (m == 2) return "255.255.0.0";
    if (m == 1) return "255.0.0.0";
    return "This mask don't exist";
};

bitset<8> convertToBits(int b) {
    return bitset<8>(b); // int -> bit
};

int main() {
    string aux, mask;
    int count = 0;
    vector<int> ipClass;
    Subnets s;
    cout << "Enter Network IP: ";
    cin >> s.ip;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout << "Enter number subnets that you need: ";
    cin >> s.numberSubnets;
    try {
        //data registered
        specialSpace();
        cout << "\033[31m" << "\nNetwork Registered\n" << "\033[0m";
        cout << "Network IP: " << s.ip << "\nSubnets: " << s.numberSubnets << endl;
        
        // Convert string -> vector<int>
        for (char i : s.ip) {
            if (i != '.' && aux.size() <= 2) {
                aux += i;
            } else if(i == '.') {
                ipClass.push_back(stoi(aux));
                aux = "";
            } else {
                throw runtime_error("");
            }
        }
        // Last digit push
        if (!aux.empty()) {
            ipClass.push_back(stoi(aux));
        };
        // ipClass -> bits
        /* for (size_t i = 0; i < ipClass.size(); ++i) {
            cout << convertToBits(ipClass[i]);
            cout << " | ";
        }*/
        //Are there zeros?
        for (int n : ipClass) {
            if (n <= 127) {
                cout << typeClass(1) << endl;
                mask = typeMask(1);
                break;
            } else if (n <= 191) {
                cout << typeClass(2) << endl;
                mask = typeMask(2);
                break;
            } else if(n >= 192 and n <= 223) {
                cout << typeClass(3) << endl;
                mask = typeMask(3);
                break;
            }
        }
        cout << "Mask: " << mask << endl;
    } catch (const runtime_error& e) {
        cerr << "\nThis Network IP don't exits" << e.what() << endl;
    }
    return 0; 
}