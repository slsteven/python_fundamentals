#selection sort

#start with linear selection
#iterate through array and find minimum value
#swap variable position with minimum value

my_list = [6, 5, 2, 8, 3, 1, 4, 7, 9]
print "length of list %s" % len(my_list)
def selection_sort(my_list):
	leng = len(my_list)
	for i in range(leng):
		min = my_list[i]
		val_index = i
		#print "i %s" % i
		for j in range(i,leng):
			#print "j %s" % j
			if my_list[j] <= min:
				min = my_list[j]
				min_index = j
			if j == leng-1:
				#value of index is = i
				#min_index = index of the found min in my list
				after_swap = swap(my_list, val_index, min_index)
	print after_swap



def swap(my_list, val_index, min_index):

	temp = my_list[val_index]
	my_list[val_index] = my_list[min_index]
	my_list[min_index] = temp
	return my_list



selection_sort(my_list)