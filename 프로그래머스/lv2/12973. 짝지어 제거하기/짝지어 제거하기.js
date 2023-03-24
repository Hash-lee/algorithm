function solution(s)
{
    if (s.length % 2) return 0;
    let temp, alp, c, flag, stack;

    
    flag = 1
    stack = s.split("");
    while (flag && 0 < stack.length) {
        flag = 0;
        temp = [stack.pop()];
        c = 1
        while (0 < stack.length) {
            alp = stack.pop();
            if (c && temp[c-1] === alp) {
                c--;
                temp.pop();
                flag = 1
            } else {
                temp.push(alp);
                c++;
            }
        }
        stack = temp.slice();
    }
    if (stack.length) return 0;
    return 1;
}