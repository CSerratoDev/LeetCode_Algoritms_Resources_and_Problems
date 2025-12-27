#include <iostream>
using namespace std;
bool IsPlayerDead(int hp){
    if(hp <= 0){
        cout << "He is dead" << endl;
        return true;
    } else {
        cout << "He is live" << endl;
        return false;
    }
}
int main(){
    IsPlayerDead(99);
    return 0;
}