# Functions are names for long operations you can define using keyword 'def'

def function_name():
	print("Hello my name is Kabir")

# The code WILL NOT RUN until you CALL the function with brackets
function_name()


# Functions can take variables/parameters/arguments
def kilogram_to_pounds(kilograms): # You pass/give the variable "kilogram" to the function to process
	print(kilograms * 2.2)

kilogram_to_pounds(12)

# Functions do not always have to print, they can also STORE values through 'return'
def kilogram_to_pounds(kilogram):
	return kilogram*2.2 # Now we use 'return' keyword, it DOES NOT print, it stores value we can use later

print("12 kilograms is "+str(kilogram_to_pounds(12))+" pounds")

# We can also try an even or odd function, that will tell user if numberis even or odd
number = int(input("what do you want to check: "))

def even_or_odd(n):
	if n%2==0:
		print("even")
	else:
		print("odd")

even_or_odd(number)