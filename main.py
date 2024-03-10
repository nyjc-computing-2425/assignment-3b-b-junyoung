stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip("")

# Type your code below
x_pos = stdform.find("x")
std_num = stdform[:x_pos]
power_pos = stdform.find("^")
power = stdform[power_pos + 1:]
print(f"This number in E notation is {std_num}E{power}.")