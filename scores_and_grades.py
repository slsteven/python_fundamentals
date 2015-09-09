
print "Scores and grades"
for i in range (5):
	x = raw_input("enter a number between 60 and 100: ")
	if (int(x) >= 60 and int(x) <=69):
		print "score %s; Your grade is D" % x
	if (int(x) >= 70 and int(x) <=79):
		print "score %s; Your grade is C" % x
	if (int(x) >= 80 and int(x) <=89):
		print "score %s; Your grade is B" % x
	if (int(x) >= 90 and int(x) <=100):
		print "score %s; Your grade is A" % x 
print "End of the program. Bye"
