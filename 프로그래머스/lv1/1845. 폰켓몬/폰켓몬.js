function solution(nums) {
    let total = nums.length / 2;
    let dict = {};
    for (let i = 0; i < nums.length; i++) {
        let s = String(nums[i]);
        if (dict.s) {
            dict.s++;
        } else {
            dict[s] = 1;
        }
    }
    return Math.min(Object.keys(dict).length, total);
}