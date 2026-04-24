#include <iostream>
#include <string>
using namespace std;

string cesarEncrypt(string text , int shift) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        char c = text[i];
        if (isupper(c)) {
            result += char(int(c + shift - 65) % 26 + 65);
        } else if (islower(c)) {
            result += char(int(c + shift - 97) % 26 + 97);
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string text;
    int shift;
    cout << "Enter text to encrypt: ";
    getline(cin, text);
    cout << "Enter shift value: ";
    cin >> shift;
    cout << "Encrypted text: " << cesarEncrypt(text, shift) << endl;
    return 0;
}