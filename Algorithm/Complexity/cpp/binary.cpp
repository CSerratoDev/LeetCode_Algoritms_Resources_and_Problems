#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <limits>

using namespace std;

bool binary(const vector<int>& arr, int start, int end, int objective) {
    if (start > end) return false;

    int middle = (start + end) / 2;
    cout << "Finding " << objective 
        << " between " << arr[start] 
        << " and " << arr[end - 1] << endl;

    if (arr[middle] == objective) {
        return true;
    } else if (arr[middle] < objective) {
        return binary(arr, middle + 1, end, objective);
    } else {
        return binary(arr, start, middle - 1, objective);
    }
};

int main() {
    int size, objective;
    cout << "Size: ";
    cin >> size;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout << "Objective: ";
    cin >> objective;

    srand(time(0));
    vector<int> arr(size);
    for (int i = 0; i < size; i++){
        arr[i] = rand() % 101;
    }

    sort(arr.begin(), arr.end());

    bool found = binary(arr, 0, size - 1, objective);

    cout << "Array: ";
    for (int num : arr ) cout << num << " ";
    cout << endl;

    cout << "Element " << objective
        << (found ? " Is Here" : "Is NOT here")
        << " in the list" << endl; 

    return 0;
}