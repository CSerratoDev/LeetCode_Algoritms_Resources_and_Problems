#include <iostream>
#include <fstream>
using namespace std;

void drawMaps(char Input, int HeroPositionX, int HeroPositionY, char map[5][5]) {
    ifstream GameMapRead("Garden.txt");
    string line;
    int row = 0;
    int column = 1;
    int count = 1;
    bool foundPlayer = false;
    if(GameMapRead.is_open()){
        while (getline(GameMapRead, line)){
            for (int i = 0; i < 5; i++){
                cout << line[i];
                if(line[i] == 'H'){
                    row = i + 1;
                    column = count;
                    foundPlayer = true;
                }
            }
            cout << endl;
            count = count + 1;
        }
        if (foundPlayer) {
            cout << "Player in row: " << row << " column: " << column;
        }
    } else {
        cout << "An error ocurred while opening the file" << endl;
    }
    cout << endl;
}

int main() {
    int HeroPositionX = 0;
    int HeroPositionY = 0;
    char map[5][5] = {
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','H','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
    };
    ofstream GameMap("Garden.txt");
    if(GameMap.is_open()){
        for(int row = 0; row < 5; row++) {
            for(int column = 0; column < 5; column++){
                GameMap << map[row][column];
            }
            GameMap << endl;
        }
    }
    GameMap.close();

    char Input = ' ';
    bool isGameOver = false;

    drawMaps(Input ,HeroPositionX, HeroPositionY, map);

    while(isGameOver == false){
        cin >> Input;
        drawMaps(Input, HeroPositionX, HeroPositionY, map);
    }
    return 0;
}