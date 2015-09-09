my_list = [6, 50, 22, 8, 30, 1, 4, 7, 9];


function selection_sort(arr){

  for(var i = 0; i< arr.length; i++){
    var val_index = i; //store index of i
    var min = arr[i];  //store value of min
    for(var j =i; j<arr.length; j++){
     //use two loops. 1 to hold variable and the other to loop through arr for comparison
     //find min, store index 
      if(arr[j] <= min){
        min = arr[j];
        min_index = j;
        }    
        if(j == arr.length-1){
          after_swap = swap(arr, val_index, min_index);
          console.log(after_swap);
          }
      }
    }
}

function swap(arr, val_index, min_index){
  temp = arr[val_index];
  arr[val_index] = arr[min_index];
  arr[min_index] = temp;
  return arr;
}


selection_sort(my_list);