# DIY program that will tell you if you are allowed to watch a certain kind of movie based on age given
# The user will input the age

# Here are the ranges:
# 0-12 : "Children's movie"
# 12-18 : "Teen movie"
# 18+ : "Adult movie"

# input_from_user = int(input("Enter your age : "))

age = int(input('age'))
if age < 12:
	print('log in with your child profile on Netflix i will tell ur mom and dad')
elif age > 12 and age < 18:
	print('teen movie')
else:
	print('adult movie')
