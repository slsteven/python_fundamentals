import random

count_heads = 0
count_tails = 0
for i in range(10):
	random_num = round(random.random())
	if random_num == 0:
		count_tails += 1
		print "Attempt #%s: Throwing a coin...It's tail! ...Got %s tail(s) so far and %s head(s) so far" % (i, count_tails, count_heads)
	if random_num == 1:
		count_heads += 1
		print "Attempt #%s: Throwing a coin...It's head! ...Got %s tail(s) so far and %s head(s) so far" % (i, count_tails, count_heads)
print "End of program"