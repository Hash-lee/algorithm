function solution(n,a,b)
{
    let A, B;
    [A, B] = [a-1, b-1].sort()
    let answer = 0;
    
    while (true) {
        answer++;
        if (A % 2) A = A - 1;
        if (B % 2) B = B - 1;
        
        if (A === B) break;
        else {
            if (A) A = Math.floor((A - 1) / 2) + 1;
            if (B) B = Math.floor((B - 1) / 2) + 1;
        }
    }
    return answer;
}