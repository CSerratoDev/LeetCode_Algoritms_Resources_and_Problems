#include <iostream>
using namespace std;

void drawMaps(int HeroPosition, char map[5]) {
    for (int i = 0; i < 5; i = i + 1) {
        if(i != HeroPosition){
            cout << map[i];
        } else {
            cout << 'H';
        }
    }
    cout << endl;
}

int main() {
    int HeroPosition = 0;
    char map[5] = {'1','1','1','1','1'};
    char Input = ' ';
    bool isGameOver = false;

    drawMaps(HeroPosition, map);

    while(isGameOver == false){
        cin >> Input;
        if (Input == 'd'){
            HeroPosition = HeroPosition + 1;
        } else if (Input == 'a') {
            HeroPosition = HeroPosition - 1;
        } else if (Input == 'p') {
            isGameOver = true;
        }
        
        drawMaps(HeroPosition, map);
    }
    return 0;
}