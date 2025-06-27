#include <iostream> // for cout and endl
#include <vector> // for use std::vector
#include <algorithm> // for use std::max

using std::cout;
using std::endl;
using std::vector;

int findMaxConsecutiveOnes(const vector<int>& nums){
    int max = 0;
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] == 1) {
            count++;
            max = std::max(max, count);
        } else {
            count = 0; // reset count
        }
    }
    return max;
}

int main() {
    vector<int> nums = {1, 1, 0, 1, 1, 1};
    int result = findMaxConsecutiveOnes(nums);
    cout << "The maximum number is: " << result << endl;
    return 0;
}
