function processData(input) {
  //Enter your code here
  input = input.split('\n');
  let i, j;

  for (i = 1; i < input.length; i++) {
    var splitWord = input[i].split('');

    var even = '';
    var odd = '';

    for (j = 0; j < splitWord.length; j++) {
      if (j % 2 === 0) {
        even = even + splitWord[j];
      } else {
        odd = odd + splitWord[j];
      }
    }
    console.log(even + ' ' + odd);
  }
}
