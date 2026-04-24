#include <iostream>
#include <string>
using namespace std;

string vigenereEncrypt(string text, string key) {
    string result = "";
    int keyIndex = 0;
    for (int i = 0; i < text.length(); i++) {
        char c = text[i];
        if (isupper(c)) {
            result += char(int(c + key[keyIndex] - 2 * 65) % 26 + 65);
            keyIndex = (keyIndex + 1) % key.length();
        } else if (islower(c)) {
            result += char(int(c + key[keyIndex] - 2 * 97) % 26 + 97);
            keyIndex = (keyIndex + 1) % key.length();
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string text, key;
    cout << "Enter text to encrypt: ";
    getline(cin, text);
    cout << "Enter key: ";
    getline(cin, key);
    cout << "Encrypted text: " << vigenereEncrypt(text, key) << endl;
    return 0;
}