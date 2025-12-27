#include <iostream>
using namespace std;
int main() {
    float PI = 3.1416;
    int radio;
    cout << "Enter radio:" << endl;
    cin >> radio;
    float area = (4*PI) * (radio * radio);
    cout << "Area: " << area << endl;
    return 0;
}