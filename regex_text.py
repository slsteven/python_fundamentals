import re

str = 'pii1iigii2ii'
match = re.search(r'\d+', str)
# If-statement after search() tests if it succeeded
if match:
	print 'found', match.group() ## 'found word:cat'
else:
 	print 'did not find'
print "hello"