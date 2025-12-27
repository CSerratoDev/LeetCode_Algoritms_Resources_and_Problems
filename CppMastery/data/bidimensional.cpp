#include <iostream>
using namespace std;
int main() {
    string Names[3] = {"Ale", "Alexis", "Chris"};
    for(int i = 0; i < 3 ; i ++) {
        cout << Names[i] << " ";
    }
    cout << endl;

    int ids[5][3] = {
        {0,1,2},
        {3,4,5},
        {6,7,8},
        {9,10,11},
        {12,13,14}
    };

    for(int j = 0; j < 5; j++) {
        for(int k = 0; k < 3; k++){
            cout << ids[j][k] << " ";
        }
        cout << endl;
    }
    return 0;
}