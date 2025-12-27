#include <iostream>
using namespace std;
int main() {
    bool found = false;
    char keys = ' ';
    do {
        cout << "Did you find your keys?" << endl;
        cout << "Enter 'y' for YES or 'n' for NOT" << endl;
        cin >> keys;
        if (keys == 'y'){
            found = true;
        }
    } while (found == false);
    return 0;
}