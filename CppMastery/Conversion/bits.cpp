#include <iostream>
#include <bitset>

using namespace std;

int main() {
    int x = 10;
    bitset<8> bits(x); // int -> bit
    cout<< "Binary (Bits): " << bits << endl;
    /*
    if (bits[3]) {
        cout << "Bit: Active" << endl;
    } else {
        cout << "Bit: Desactive" << endl;
    }
    */
    int num = static_cast<int>(bits.to_ulong()); // bit -> int
    cout << "Number: " << num << endl; 
    return 0;
}