#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream MyFile("GameData.txt");
    if(MyFile.is_open()){
        MyFile << "Hello World!" << endl;
        MyFile << "Created by cserratodev";
    }
    MyFile.close();

    ifstream MyFileRead("GameData.txt");
    string line;

    if(MyFileRead.is_open()){
        while (getline(MyFileRead, line)) {
            cout << line << endl;
        }
    } else {
        cout << "An error ocurred while opening the file" << endl;
    }
    return 0;
}