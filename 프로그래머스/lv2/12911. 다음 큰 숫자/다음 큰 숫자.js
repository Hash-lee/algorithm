function solution(n) {
    function countOne(num) {
        let one = 0;
        while (0 < num) {
            if (num % 2) {
                num -= 1;
                one += 1;
            }
            num /= 2;
        }
        return one;
    }
    let count = countOne(n);
    let target = n + 1;
    while (true) {
        if (countOne(target) === count) return target;
        target++;
    }
}