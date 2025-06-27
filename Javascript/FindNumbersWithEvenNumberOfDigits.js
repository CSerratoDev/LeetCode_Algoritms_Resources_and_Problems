let findNumsWithEvenNumberOfDigits = function(nums) {  
    return nums.reduce((count, num) => {
        return count +  (num.toString().length % 2 === 0 ? 1 : 0);
    }, 0);
}
console.log(`Total: ${findNumsWithEvenNumberOfDigits([12, 345, 2, 6, 7896])}`);