function solution(n) {
    let answer = 0;
    
    let sumNum = 0;
    let detract = 0;
    for (let i = 0; i < n + 1; i++) {
        while (n < sumNum + i) {
            detract += 1;
            sumNum -= detract;
        }
        sumNum += i;
        if (sumNum === n) answer++;
    }
    return answer;
}