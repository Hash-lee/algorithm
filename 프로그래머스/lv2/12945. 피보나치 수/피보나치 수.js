function solution(n) {
    if (n === 0) return 0;
    if (n === 1) return 1;
    let left = 0;
    let right = 1;
    let idx = 1;
    let temp;
    for (idx; idx < n; idx++) {
        temp = (left + right) % 1234567;
        left = right;
        right = temp;
    }
    return right;
}