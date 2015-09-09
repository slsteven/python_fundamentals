users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


for person, val in users.items():
	num = 0
	print person
	for person in val:
		num += 1
		leng = len(person['first_name']) + len(person['last_name'])
		print " %s" % num, person['first_name'], person['last_name'], "- %s" % leng 
		