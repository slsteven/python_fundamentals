#python bubble sort
import time
start_time = time.time()


arr = [6, 5, 1, 3, 8, 7, 2, 4]


def bubble_sort(arr):
	newarr = []
	count = 0
	leng = len(arr)
	for i in range(leng -1):
  		partial = arr[i:i+2]
  		# print partial
 		if 	partial[0] > partial[1]:
      	   		count += 1
      			arr[i], arr[i+1] = arr[i+1], arr[i]
      			
      	
  	if (count > 1):
  		bubble_sort(arr)
  
 	else:
   		print(arr)
 


bubble_sort(arr);

print("--- %s seconds ---" % (time.time() - start_time))