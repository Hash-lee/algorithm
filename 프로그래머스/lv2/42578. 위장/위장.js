function solution(clothes) {
    let dict = {};
    for (let i=0; i<clothes.length; i++) {
        let a, b;
        a = clothes[i][0];
        b = clothes[i][1];
        if (dict[b]) {
            dict[b] = dict[b] + 1;
        } else {
            dict[b] = 1;
        }
    }
    let keys = Object.keys(dict);
    let total = 1;
    for (let i=0; i<keys.length; i++) {
        let value = keys[i];
        total = total * (dict[value] + 1);
    }
    return total-1;
}