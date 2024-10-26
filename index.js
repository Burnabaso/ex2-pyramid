//O(x*i), x*i being the product of number of rows and elements in each row 
function printPyramid(x) {
    //O(x), x being the input by user
    for(var i=1;i<=x;i++){
        var row = [];
        // O(i), i being the number of numbers in a row
        for(var j=0;j<i;j++){
            row.push(2*j+1)
        }
        console.log(row.join(" "))
    }
}

(function () {
  const x = prompt("Enter number of rows: ");
  printPyramid(x);
})();
