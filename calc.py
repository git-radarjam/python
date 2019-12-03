import sys
equation = sys.argv[1:]
# print(equation)
# print(len(equation))

# Addition
def add(num1, num2):
	return float(num1) + float(num2)

# Subtraction
def sub(num1, num2):
	return float(num1) - float(num2)

# Multiplication
def mult(num1, num2):
	return float(num1) * float(num2)

# Division
def div(num1, num2):
	return float(num1) / float(num2)

def main():
	# Check if we only pass in 1 argument, it is the same as entering a number in the calculator
	# and hitting = to return the same number
	if len(equation) == 1:
		print("Answer: "+ equation[0])
		quit(0)
	ans = None
	for opIndex in range(len(equation)):
		# Checking if the value at index x is a +
		if equation[opIndex] == "+":
			# If the value of ans is None, or still default, we know it is the first part of an equation
			# Therefore we want to set ans to be the answer of the first part
			if ans == None:
				ans = add(equation[opIndex-1],equation[opIndex+1])
			# If it is not, we want to add ans to the next part of the equation
			else:
				ans = add(ans, equation[opIndex+1])
		elif equation[opIndex] == "-":
			if ans == None:
				ans = sub(equation[opIndex-1], equation[opIndex+1])
			else:
				ans = sub(ans, equation[opIndex+1])
		elif equation[opIndex] == "x":
			if ans == None:
				ans = mult(equation[opIndex-1], equation[opIndex+1])
			else:
				ans = mult(ans, equation[opIndex+1])
		elif equation[opIndex] == "/":
			try:
				if ans == None:
					ans = div(equation[opIndex-1], equation[opIndex+1])
				else:
					ans = div(ans, equation[opIndex+1])
			except:
				print("NaN")
				quit(1)
	print("Answer: " + str(ans))
        
main()
