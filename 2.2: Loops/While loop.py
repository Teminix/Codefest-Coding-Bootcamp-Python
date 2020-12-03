# Loops are bits of code that can be executed repetitively
# While loop will run some code as long as a condition is satisfied

x = 0

while x < 10:
	x = x + 1
	if x == 4:
		break
	print("The current number is "+str(x))