function solution(s) {
    let answer = '';
    let arr = s.split(" ");
    let int_arr = arr.map(x => parseInt(x));
    return Math.min(...int_arr) + " " + Math.max(...int_arr);
}