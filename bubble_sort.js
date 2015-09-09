var arr = [6, 5, 1, 3, 8, 7, 2, 4];


function bubble_sort(arr){
var newarr = [];
var count = 0;
  for(var i = 0; i < arr.length-1; i++){
  var temp;
    partial = arr.slice(i,i+2);
    if(partial[0] > partial[1]){
      count +=1;
      temp = arr[i];
      arr[i] = arr[i+1];
      arr[i+1] = temp;    
    }

  }
if (count > 1){
  bubble_sort(arr);
  }
 else{
   console.log(arr);
 }
}

bubble_sort(arr);