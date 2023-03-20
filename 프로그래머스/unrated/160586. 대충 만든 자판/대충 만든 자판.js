function solution(keymap, targets) {
    var answer = [];
    for (let i=0; i < targets.length; i++) {
        var make_word = 0;
        var flag = 0;
        for (let w=0; w < targets[i].length; w++) {
            var make_alp = 101;
            if (flag)
                break;
            for (let j=0; j < keymap.length; j++) {
                for (let k=0; k<keymap[j].length; k++) {
                    if (keymap[j][k]==targets[i][w] && k < make_alp) {
                        make_alp = k+1;
                    }
                }
            }
            if (make_alp==101) {
                flag=1;
                break;
            } else {
                make_word += make_alp;    
            }
        }
        if (flag) {
            answer.push(-1);
        } else {
            answer.push(make_word)    
        }
    }
    return answer;
}