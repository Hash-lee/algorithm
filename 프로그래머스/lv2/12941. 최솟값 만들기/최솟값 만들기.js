function solution(A,B) {
    let answer = 0;
    A.sort(function (a, b) {
        return a - b;
    });
    B.sort(function (a, b) {
        return a - b;
    });
    B.reverse();
    
    for (let i=0; i < A.length; i++) {
        answer += (A[i] * B[i]);
    }
    return answer;
}