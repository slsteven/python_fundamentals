#python fundamentals

x = [1,2,4,5,6]

#tuple
my_tuple = ("this", 2, "is", "apple")
# print my_tuple[2]
# for data in my_tuple:
# 	print data


#tuple unpacking

# (a, b, c, d) = my_tuple
# print a
# print b
# print c
# print d

#---------------------------------------
#dictionaries
# weekend = {"mon": 1, "tues": 2, "wed": 3}

# for keys,valu in weekend.items():
# 	print keys, valu


# x = {}
# print x.fromkeys([weekend], "NULL")


#---------------------------------------
#dicts with lists and tuples
# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }

# for key, data in context.items():
#      #print data
#      for value in data:
#           print "Question #", value["id"], ": ", value["content"]
#           print "----"


#---------------------------------------
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]

# country_specials = zip(countries, dishes)
# print country_specials

# x = dict(country_specials)
# print x

for val in "string":
  if val == "i":
    continue
    print val
  print(val)























