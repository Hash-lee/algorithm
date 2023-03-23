function solution(s) {
    let iter, delCount;
    
    function toBi(num) {
        let result = [];
        while (0 < num) {
            if (num % 2) {
                num = (num - 1) / 2;
                result.push('1');
            } else {
                num = num / 2;
                result.push('0');
            }
        }
        return result.reverse().join("");
    }
    function delZero(snum, n) {
        let temp = '';
        for (let i=0; i < snum.length; i++) {
            if (snum[i] === '1') {
                temp += '1';
            } else {
                n += 1;
            }
        }
        return [toBi(temp.length), n];
    }
    
    iter = 0;
    delCount = 0;
    while (s != '1') {
        iter += 1;
        [s, delCount] = delZero(s, delCount);
    }
    let answer = [iter, delCount];
    
    return answer;
}