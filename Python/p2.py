total = 2
previous = 1
current = 2

while current <= 4000000:
	temp = current
	current = previous + current
	previous = temp
	
	if current % 2 == 0:
		total = total + current

print "The total is %s" % total

"""
    Post-mortem
    1. while is of the form: while expr:
    2. for is of the form: for i in range(x, y):
"""