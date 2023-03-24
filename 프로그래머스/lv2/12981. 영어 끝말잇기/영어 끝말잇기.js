function solution(n, words) {
    let word, turn, check, last, who;
    
    turn = Array.from({length:n}, () => 0);
    check = {};
    last = words[0];
    turn[0]++;
    check[words[0]] = 1;
    who = 0;
    for (let i=1; i < words.length; i++) {
        who = (who + 1) % n;
        turn[who]++;
        word = words[i];
        if (last.charAt(last.length-1) != word.charAt(0) || check[word]) return [who + 1, turn[who]];
        check[word] = 1;
        last = word
    }

    
    
    
    return [0, 0];
}