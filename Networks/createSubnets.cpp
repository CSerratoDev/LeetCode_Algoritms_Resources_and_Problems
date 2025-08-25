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

void typeClass(int c){
    switch (c) {
        case 1:
            cout << "\nClass A";
            break;
        case 2:
            cout << "\nClass B";
            break;
        case 3:
            cout << "\nClass C";
            break;
        default:
            cout << "\nClass undefined";
            break;
    }
};

string typeMask(int m){
    string mask;
    if (m == 3) {
        return mask = "255.255.255.0";
    } else if (m == 2) {
        return mask = "255.255.0.0";
    } else if (m == 1) {
        return mask = "255.0.0.0";
    } else {
        return "This mask don't exist";
    }
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
        for (int i = 0; i < 20; i++) {
            cout<<"*";
        };
        cout << "\nNetwork Registered\n";
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
        for (size_t i = 0; i < ipClass.size(); ++i) {
            cout << convertToBits(ipClass[i]);
            cout << " | ";
        }
        //Are there zeros?
        for (int n : ipClass) {
            if (n == 0) {
                typeClass(count);
                mask = typeMask(count);
                break;
            }
            count++;
        }
        cout<< "\nMask: " << mask << endl;
    } catch (const runtime_error& e) {
        cerr << "\nThis Network IP don't exits" << e.what() << endl;
    }
    return 0; 
}