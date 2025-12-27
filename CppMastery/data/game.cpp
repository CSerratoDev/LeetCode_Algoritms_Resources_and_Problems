#include <iostream>
using namespace std;

void drawMaps(int HeroPositionX, int HeroPositionY, char map[5][5]) {
    for (int i = 0; i < 5; i = i + 1) {
        for(int j = 0; j < 5; j = j + 1){
            if(i != HeroPositionY){
                cout << map[j][i];
            } else {
                if ( j != HeroPositionX){
                    cout << map[j][i];
                } else {
                    cout << 'H';
                }
            }
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    int HeroPositionX = 0;
    int HeroPositionY = 0;
    char map[5][5] = {
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
    };
    char Input = ' ';
    bool isGameOver = false;

    drawMaps(HeroPositionX, HeroPositionY, map);

    while(isGameOver == false){
        cin >> Input;
        if (Input == 'd'){
            HeroPositionX = HeroPositionX + 1;
        } else if (Input == 'a') {
            HeroPositionX = HeroPositionX - 1;
        } else if (Input == 'w') {
            HeroPositionY = HeroPositionY - 1;
        } else if (Input == 's'){
            HeroPositionY = HeroPositionY + 1;
        } else if (Input == 'p') {
            isGameOver = true;
        }
        
        drawMaps(HeroPositionX, HeroPositionY, map);
    }
    return 0;
}