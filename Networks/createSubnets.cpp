#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
using namespace std;

struct Subnets {
    string ip;
    int numberSubnets;
    int mask;
};

void specialSpace() {
    for (int i = 0; i < 30; i++) {
            cout<<"*";
    };
    cout << endl;
}

vector<vector<int>> createSubnetRange(int networks, int numberSubnets) {
    vector<vector<int>> result;
    int subnetSize = networks / numberSubnets;
    for (int i = 0; i < numberSubnets; i++) {
        int networksAddress = i * subnetSize;
        int firstHost = networksAddress + 1;
        int lastHost = networksAddress + subnetSize - 2;
        int broadcastAddress = networksAddress + subnetSize - 1;
        result.push_back({networksAddress, firstHost, lastHost, broadcastAddress});
    }
    return result;
};

vector<vector<int>> networks(int mask, int numberSubnets) {
    //Starts at 0 
    int base = 2;
    int rangeBits = 32 - mask;
    int networks = static_cast<int>(pow(base, rangeBits));
    int hosts = networks - 2;
    return createSubnetRange(networks, numberSubnets);
};

string typeClass(int c){
    switch (c) {
        case 1: return "Class A";
        case 2: return "Class B";
        case 3: return "Class C";
        default: return "Class Undefined";
    }
};

string typeMask(int m){
    /*
    if (m == 3) return "255.255.255.0";
    if (m == 2) return "255.255.0.0";
    if (m == 1) return "255.0.0.0";
    return "This mask don't exist";
    */
    if(m < 0 || m > 32) {
        return "This mask don't exist";
    }

    bitset<32> mask((~0u) << (32 - m));

    string result;
    for(int i=3; i>=0; i--) {
        unsigned int octet = (mask.to_ulong() >> (i*8)) & 0xFF;
        result += to_string(octet);
        if(i>0) result += ".";
    }
    return result;
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
    cout << "Enter mask: ";
    cin >> s.mask;
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
                mask = typeMask(s.mask);
                break;
            } else if (n <= 191) {
                cout << typeClass(2) << endl;
                mask = typeMask(s.mask);
                break;
            } else if(n >= 192 and n <= 223) {
                cout << typeClass(3) << endl;
                mask = typeMask(s.mask);
                break;
            }
        }
        cout << "Mask: " << mask << endl;
        specialSpace();
        if(s.numberSubnets <= 32) {
            vector<vector<int>> subnets = networks(s.mask, s.numberSubnets);
            cout<<"Subnets Generated" << endl;
            for (size_t i = 0; i < subnets.size(); i++) {
                cout << "Subnet " << i << " -> "
                    << "Network: " << subnets[i][0]
                    << ", First Host: " << subnets[i][1]
                    << ", Last Host: " << subnets[i][2]
                    << ", Broadcast: " << subnets[i][3] << endl;
            }
            specialSpace();
        } else {
            cerr << "\nThat number of subnets is an invalid range";
        }
    } catch (const runtime_error& e) {
        cerr << "\nThis Network IP don't exits" << e.what() << endl;
    }
    return 0; 
}