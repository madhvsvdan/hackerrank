function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    console.log(arr.reverse().join(' '))
}
